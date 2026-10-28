# Reforma Tributária Logix — Impactos e Entregas por módulo

Conteúdo extraído do TDN (TOTVS) — [Reforma Tributária Logix - Impactos](https://tdn.totvs.com/pages/releaseview.action?pageId=976158223) — em Markdown, para ser consultado por IAs (NotebookLM, Groq, ChatGPT, Claude etc.).

## Módulos

| Módulo | Markdown | Página (GitHub Pages) |
| --- | --- | --- |
| Controladoria (Patrimônio) | [controladoria.md](modulos/controladoria.md) | [abrir](https://kam4-brisa.github.io/reforma-tributaria-logix/modulos/controladoria.html) |
| CNPJ Alfanumérico | [cnpj-alfanumerico.md](modulos/cnpj-alfanumerico.md) | [abrir](https://kam4-brisa.github.io/reforma-tributaria-logix/modulos/cnpj-alfanumerico.html) |
| Entradas | [entradas.md](modulos/entradas.md) | [abrir](https://kam4-brisa.github.io/reforma-tributaria-logix/modulos/entradas.html) |
| Eventos | [eventos.md](modulos/eventos.md) | [abrir](https://kam4-brisa.github.io/reforma-tributaria-logix/modulos/eventos.html) |
| Financeiro | [financeiro.md](modulos/financeiro.md) | [abrir](https://kam4-brisa.github.io/reforma-tributaria-logix/modulos/financeiro.html) |
| Fiscal | [fiscal.md](modulos/fiscal.md) | [abrir](https://kam4-brisa.github.io/reforma-tributaria-logix/modulos/fiscal.html) |
| Importação | [importacao.md](modulos/importacao.md) | [abrir](https://kam4-brisa.github.io/reforma-tributaria-logix/modulos/importacao.html) |
| Suprimentos | [suprimentos.md](modulos/suprimentos.md) | [abrir](https://kam4-brisa.github.io/reforma-tributaria-logix/modulos/suprimentos.html) |
| Vendas e Faturamento | [vendas-faturamento.md](modulos/vendas-faturamento.md) | [abrir](https://kam4-brisa.github.io/reforma-tributaria-logix/modulos/vendas-faturamento.html) |

Suprimentos ainda está como "Em Breve" no TDN.

## NotebookLM

Em **Adicionar fonte → Site**, cole os links da coluna "Página (GitHub Pages)".

## Groq (RAG)

```bash
python rag/perguntar.py "Como gerar o evento 211130 no Patrimônio?"
```

Precisa da variável `GROQ_API_KEY` (chave em <https://console.groq.com/keys>). Sem dependências além do Python 3.
O script baixa os `.md` deste repositório, busca os trechos mais relevantes (BM25, bom para códigos como `PAT10028`, `OBF26000`) e manda só eles para o modelo, que responde citando as fontes.

## Outras IAs

Link direto de cada arquivo em texto puro:
`https://raw.githubusercontent.com/Kam4-brisa/reforma-tributaria-logix/main/modulos/<arquivo>.md`
