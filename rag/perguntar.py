"""Pergunta ao Groq sobre a Reforma Tributária Logix, usando os .md deste repositório como base (RAG).

Uso:
    set GROQ_API_KEY=gsk_...            (Windows)   |   export GROQ_API_KEY=gsk_...   (Linux/Mac)
    python perguntar.py "Como gerar o evento 211130 no Patrimônio?"
    python perguntar.py                  (modo interativo)

Só usa a biblioteca padrão do Python. Os módulos são baixados do GitHub a cada execução,
então o script sempre responde com o conteúdo que está no repositório.
Variáveis opcionais: GROQ_MODEL (modelo do Groq), RAG_TOP_K (quantos trechos enviar).
"""
import json, math, os, re, sys, unicodedata, urllib.request
from collections import Counter

REPO = "Kam4-brisa/reforma-tributaria-logix"
BRANCH = "main"
MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
TOP_K = int(os.environ.get("RAG_TOP_K", "8"))
MAX_CHUNK = 1800


def http_get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": "rag-logix", **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def carregar_modulos():
    lista = json.loads(http_get(f"https://api.github.com/repos/{REPO}/contents/modulos?ref={BRANCH}"))
    return {f["name"]: http_get(f["download_url"]) for f in lista if f["name"].endswith(".md")}


def dividir(nome, texto):
    """Quebra o .md em trechos por seção, guardando o caminho de títulos (módulo > ano > pacote > item)."""
    titulos, buf, trechos = {}, [], []

    def fechar():
        corpo = "\n".join(buf).strip()
        buf.clear()
        if not corpo:
            return
        caminho = " > ".join(titulos[k] for k in sorted(titulos))
        while corpo:
            parte, corpo = corpo[:MAX_CHUNK], corpo[MAX_CHUNK:]
            trechos.append({"arquivo": nome, "caminho": caminho, "texto": parte})

    for linha in texto.splitlines():
        m = re.match(r"^(#{1,5}) (.+)", linha)
        if m:
            fechar()
            nivel = len(m.group(1))
            titulos = {k: v for k, v in titulos.items() if k < nivel}
            titulos[nivel] = m.group(2).strip()
        else:
            buf.append(linha)
    fechar()
    return trechos


def tokens(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9_]+", s)


class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.docs = [Counter(d) for d in docs]
        self.lens = [len(d) for d in docs]
        self.avg = sum(self.lens) / max(len(docs), 1)
        df = Counter(t for d in self.docs for t in d)
        n = len(docs)
        self.idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}
        self.k1, self.b = k1, b

    def score(self, q):
        out = []
        for d, l in zip(self.docs, self.lens):
            s = 0.0
            for t in q:
                if t in d:
                    tf = d[t]
                    s += self.idf[t] * tf * (self.k1 + 1) / (tf + self.k1 * (1 - self.b + self.b * l / self.avg))
            out.append(s)
        return out


def perguntar_groq(pergunta, trechos):
    chave = os.environ.get("GROQ_API_KEY")
    if not chave:
        sys.exit("Defina a variável de ambiente GROQ_API_KEY.")
    contexto = "\n\n---\n\n".join(f"[{i}] {t['caminho']}\n{t['texto']}" for i, t in enumerate(trechos, 1))
    msgs = [
        {"role": "system", "content":
            "Você responde dúvidas sobre a Reforma Tributária no ERP TOTVS Logix. "
            "Use SOMENTE os trechos de documentação fornecidos. Cite os trechos usados como [n]. "
            "Se a resposta não estiver nos trechos, diga que não encontrou na documentação. Responda em português."},
        {"role": "user", "content": f"Trechos da documentação:\n\n{contexto}\n\nPergunta: {pergunta}"},
    ]
    body = json.dumps({"model": MODEL, "messages": msgs, "temperature": 0.2}).encode()
    req = urllib.request.Request("https://api.groq.com/openai/v1/chat/completions", data=body, headers={
        "Authorization": f"Bearer {chave}", "Content-Type": "application/json", "User-Agent": "rag-logix"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]


def buscar(indice, bm25, pergunta, k=TOP_K):
    notas = bm25.score(tokens(pergunta))
    melhores = sorted(range(len(notas)), key=notas.__getitem__, reverse=True)[:k]
    return [indice[i] for i in melhores if notas[i] > 0]


def main():
    print("Carregando documentação do GitHub...", file=sys.stderr)
    indice = [t for nome, txt in sorted(carregar_modulos().items()) for t in dividir(nome, txt)]
    bm25 = BM25([tokens(t["caminho"] + " " + t["texto"]) for t in indice])
    print(f"{len(indice)} trechos indexados.", file=sys.stderr)

    def responder(p):
        achados = buscar(indice, bm25, p)
        if not achados:
            print("Nada encontrado na documentação para essa pergunta.")
            return
        print("\n" + perguntar_groq(p, achados))
        print("\nFontes:")
        for i, t in enumerate(achados, 1):
            print(f"  [{i}] {t['caminho']}")

    if len(sys.argv) > 1:
        responder(" ".join(sys.argv[1:]))
        return
    while p := input("\nPergunta (vazio sai): ").strip():
        responder(p)


if __name__ == "__main__":
    main()
