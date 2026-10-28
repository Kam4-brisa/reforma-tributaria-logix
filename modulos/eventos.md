# Reforma Tributária Logix — Eventos

Fonte: <https://tdn.totvs.com/pages/releaseview.action?pageId=1009450038>

## 1. Visão Geral

A **Reforma Tributária** traz um cenário de mudanças significativas nas regras tributárias brasileiras, exigindo das empresas uma adaptação rápida e precisa para garantir conformidade e eficiência operacional. **Os Eventos da Reforma Tributária** são, na verdade, uma nova funcionalidade fiscal e um conjunto de ações e etapas para a implementação das mudanças aprovadas pela Emenda Constitucional 132/2023.

**O que são os novos eventos da NF-e?**
São registros e informações adicionais que serão vinculados aos documentos fiscais eletrônicos (como a NF-e), que se tornam cruciais no novo sistema tributário de consumo (IBS e CBS).

**Qual a função deles no novo sistema tributário?**
Suporte à Apuração Automática: Fornecer ao Fisco (governo) os dados necessários para o cálculo automático (apuração assistida) dos débitos e créditos dos novos tributos (IBS e CBS) de cada contribuinte, em tempo real ou quase real.
Registro de Situações Específicas: Documentar ocorrências que afetam o cálculo do imposto, como:

- Perecimento, perda, roubo ou furto de mercadorias;
- Destinação de item para consumo pessoal (que pode impactar o crédito);
- Manifestações sobre pedidos de transferência de crédito, etc.

Eles representam uma mudança do modelo onde o contribuinte apurava o imposto para um modelo onde o Fisco pré-calcula e o contribuinte confere, com base em informações mais detalhadas e padronizadas. O envio correto e a validação desses eventos pelas empresas são fundamentais para a conformidade fiscal no novo regime.

Os novos eventos estão distribuídos nos módulos do Backoffice Logix, conforme imagem abaixo:

Confira as liberações já realizadas:

## 2025

### Pacote 17/11

#### OBF26000 - Cockpit dos Eventos

OBF26000 - Cockpit Eventos IBS/CBS! Esta ferramenta foi desenvolvida para auxiliar sua empresa no cumprimento das entregas e exigências dos eventos relacionados à Reforma Tributária no Brasil. Este guia abrangente foi criado para ajudá-lo a compreender e utilizar todas as funcionalidades do centralizador de eventos, garantindo que sua organização esteja totalmente preparada para os desafios que a reforma tributária apresenta.

Ele concentra, em um único ambiente, todas as funcionalidades necessárias para **cadastro, inclusão, consulta, geração, transmissão e cancelamento** de eventos, garantindo a conformidade com os padrões técnicos definidos pela **SEFAZ** e proporcionando maior rastreabilidade e controle sobre o ciclo de vida das notas fiscais eletrônicas.

- OBF26100 - Cadastro de Eventos
- OBF26200 - Central de Eventos
- OBF26300 - Inclusão Manual de Eventos

Importante

Nesse pacote, liberado em 17/11/2025, foram tratados apenas a inclusão manual dos eventos:

- **112110** - Informação de efetivo pagamento integral para liberar crédito presumido do adquirente;
- **112120** - Importação em ALC/ZFM não convertida em isenção;
- **112130** - Perecimento, perda, roubo ou furto durante o transporte contratado pelo fornecedor;
- **112140** - Fornecimento não realizado com pagamento antecipado;
- **211110** - Solicitação de Apropriação de crédito presumido;
- **211120** - Destinação de item para consumo pessoal;
- **211124** - Perecimento, perda, roubo ou furto durante o transporte contratado pelo adquirente;
- **211128** - Aceite de débito na apuração por emissão de nota de crédito;
- **211130** - Imobilização de item;
- **211140 -** Solicitação de Crédito de Combustível Destinatário
- **211150** - Solicitação de apropriação de crédito para bens e serviços que dependem de atividade do adquirente;
- **212110** - Manifestação sobre pedido de transferência de crédito de IBS em operações de sucessão;
- **212120** - Manifestação sobre pedido de transferência de crédito de CBS em operações de sucessão;
- **110001** - Cancelamento de Evento.

Digitação manual sem integração com parceiros - TSS/Neogrid.

### Pacote 08/12

#### OBF26000 - Cockpit dos Eventos

Neste pacote foi liberado a **transmissão dos eventos via TSS** , incluindo **envio** e **processamento do retorno** .

Liberado também a inclusão Manual do evento **112150- Atualização da Data de Previsão de Entrega.**

### Pacote 22/12

#### OBF26000 - Cockpit dos Eventos

1. Neste pacote foi liberado a **transmissão dos eventos via TC2** , incluindo **envio** e **processamento do retorno** .

**2. Geração de XML por empresa ou pasta por evento**

**Critério de Definição de Diretório:**

O sistema define automaticamente onde gerar os arquivos XML dos eventos seguindo uma hierarquia de configurações:

**Prioridade 1 - Configuração por Empresa LOG00098:**

- Sistema verifica primeiro se existe parâmetro "EVT" configurado para a empresa específica com o caminho onde deve ser gravado o xml
- Quando configurado, utiliza o caminho definido para aquela empresa
- Permite configuração individualizada por empresa

**Prioridade 2 - Pasta por evento (Todas as Empresas):**

- Quando não existe parâmetro "EVT" por empresa, verifica o cadastro de eventos OBF26100
- Se o campo "Caminho do XML" estiver preenchido no cadastro de eventos
- Todos os XMLs do evento serão gerados no mesmo diretório
- Aplicável para todas as empresas do sistema

**Fluxo de Validação:**

- Sistema verifica se existe parâmetro "EVT" configurado para a empresa no LOG00098
- Se configurado: utiliza caminho específico da empresa
- Se não configurado: verifica campo "Caminho do XML" no cadastro de eventos
- Se preenchido: utiliza pasta central para todas as empresas
- Gera XML no diretório apropriado conforme hierarquia identificada
- Estas regras de geração são utilizadas para os transmissores TSS e TC2.

## 2026

### Pacote 12/01

#### OBF26000 - Cockpit dos Eventos

1. Alterações referente a **transmissão dos eventos via TC2** , incluindo **envio** e **processamento do retorno** .

2. Neste pacote foram liberados as manutenções abaixo:

- [26055074 DBACKFISUST-5868 DT OBF26300: Ao incluir o evento do PAT, o zoom do Aviso de Recebimento não abre e é exibida mensagem.](https://tdn.totvs.com/pages/viewpage.action?pageId=1032145276)
- [DBACKRTLGX-3632 DT OBF26000: Ajustes na inclusão e cancelamento dos eventos](https://tdn.totvs.com/pages/viewpage.action?pageId=1032154114)

### Pacote 02/02

#### Eventos Ajustes Gerais

#### Correção do Indicador de Aceite (OBF26300)

Ajuste no programa OBF26300 para carregar automaticamente as informações de aceite, sincronizando com as configurações estabelecidas no cadastro do evento (OBF26100)

#### Rastreabilidade de Eventos

Inclusão do campo Programa na opção Detalhes do OBF26200

[Mais informações](https://tdn.totvs.com/x/7B7ePQ)

Importante

Para o processamento do **Cockpit de Eventos** na Release **12.1.2503** , é **obrigatório** que o ambiente esteja atualizado com o **pacote Framework 2507 – Fix 03** .
