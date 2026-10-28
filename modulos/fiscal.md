# Reforma Tributária Logix — Fiscal

Fonte: <https://tdn.totvs.com/pages/releaseview.action?pageId=989567541>

## 1. Visão Geral

A **Reforma Tributária** traz um cenário de mudanças significativas nas regras tributárias brasileiras, exigindo das empresas uma adaptação rápida e precisa para garantir conformidade e eficiência operacional.

## 2025

### Pacote 22/09

#### Crédito Presumido

- Conforme NT 2025.002 v1.20, para o crédito presumido existe uma tabela específica de códigos ( [cCredPres](https://dfe-portal.svrs.rs.gov.br/DFE/TabelaCreditoPresumido) ), que define os percentuais, vigência, critérios de aplicação e vinculação para esse tributo.
- Foi desenvolvido o cadastro **OBF25200** onde pode ser incluído/importado as informações referentes aos códigos de **crédito presumido:**

**Conversores OBF00660**

Conversor criado para criação da tabela.

- **OBF12000 - Prepara informações para livros fiscais:** Inclusão de gravação dos novos campos e tributos nas tabelas de integração para documentos de entradas, saídas, serviços e frete.
- **OBF12002 - Transferência de Informações Fiscais para Histórico:** Inclusão de gravação dos novos campos e tributos nas tabelas de integração **.**

**Novos Tributos**

**IS -** Imposto Seletivo

**CBS -** Contribuição Social sobre Bens e Serviços

**IBS_UF -** Imposto sobre Bens e Serviços Estadual

**IBS_MUN -** Imposto sobre Bens e Serviços Municipal

**Conversores OBF00654 e OBF00656**

Conversor criado para gerar os novos campos nas tabelas de entradas, saídas e históricos fiscais.

- **OBF25100 - Consulta de Documentos Fiscais** é uma ferramenta completa para consulta e análise de documentos fiscais armazenados nas tabelas de integração fiscal. Abrange todos os tipos de operações fiscais: **entradas** , **saídas** , **serviços tomados** e **serviços prestados** . O programa oferece três níveis de consulta hierárquicos que permitem navegação detalhada e progressiva através dos dados fiscais.

### Pacote 17/11

#### OBF26000 - Cockpit dos Eventos

O **Cockpit** tem como objetivo centralizar o gerenciamento completo dos **eventos fiscais eletrônicos** relacionados à Nota Fiscal Eletrônica ( **NF-e** ) e à Nota Fiscal de Consumidor Eletrônica ( **NFC-e** ).

Ele concentra, em um único ambiente, todas as funcionalidades necessárias para **cadastro, inclusão, consulta, geração, transmissão e cancelamento** de eventos, garantindo a conformidade com os padrões técnicos definidos pela **SEFAZ** e proporcionando maior rastreabilidade e controle sobre o ciclo de vida das notas fiscais eletrônicas.

- OBF26100 - Cadastro de Eventos
- OBF26200 - Central de Eventos
- OBF26300 - Inclusão Manual de Eventos

### Pacote 08/12

#### OBF12000 - Prepara informações para livros fiscais

#### OBF12020 - Livro de Entradas

#### OBF12002 - Transferência de Informações Fiscais para Histórico entrada e saídas

Alterado para integrar as notas fiscais de débito e crédito, abrangendo tanto notas fiscais de entrada quanto notas de saída. A alteração implementa novos controles para identificação dos tipos de crédito e débito conforme LC 214/25 e NT reforma tributária.

#### OBF25100 - Consulta de Documentos fiscais

**Tela - Detalhes da Nota Fiscal -** Incluído na tela de detalhes da nota fiscal o campo **Tipo,** campo específico para nota fiscal de débito e crédito (LC 214/25 e NT reforma tributária).

Documento Técnico: [DBACKRTLGX-1244 - DT Integração das notas fiscais de débito e crédito](https://tdn.totvs.com/pages/viewpage.action?pageId=1008235380)

## 2026

### Pacote 02/02

#### CBS/IBS - Tributação Regular

Alterado a integração OBF12000 para atender os novos tributos relacionados ao IBS e CBS regular tanto para entradas quanto para saídas, consulta dos documentos fiscais, relatórios gerados pelo OBF25100 e extrator do TAF para não considerar esse tributo tanto no arquivo quando no relatório.

[Mais informações](https://tdn.totvs.com/x/lr7LPQ)

#### CBS/IBS - Crédito Presumido

Alterado a integração OBF12000 para atender os novos tributos relacionados ao crédito presumido tanto para entradas quanto para saídas, consulta dos documentos fiscais e relatórios gerados pelo OBF25100.

[Mais informações](https://tdn.totvs.com/x/aL3LPQ)

### Pacote 23/02

#### CNPJ Alfanumérico

Alterado a validação do CNPJ para considerar corretamente os caracteres alfanuméricos;

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=963023435)

#### OBF25200 - Cadastro Crédito Presumido

Alterado o para tratar a importação do arquivo texto quando for utilizado o banco de dados **Informix** .

[Mais informações](https://tdn.totvs.com/display/LLOG/26480743+DBACKFISUST-6148+-+DT+OBF25200+-+Erro+-201+-+A+syntax+error+has+ocurred+ao+importar+arquivo)

### Pacote 16/03

#### Documentos Fiscais - Grupo CBS/IBS Diferido

Alterado a integração OBF12000 para atender os novos tributos relacionados ao crédito Diferido para notas fiscais de entradas, consulta dos documentos fiscais e relatórios gerados pelo OBF25100.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1043713991)

#### Documento Fiscal - CBS/IBS - Grupo Antecipação de Pagamento/Multa e juros

Alterado a integração OBF12000 para atender os novos tributos relacionados ao Grupo de antecipação de pagamento / Multa e Juros para notas fiscais de entradas e saída, consulta dos documentos fiscais e relatórios gerados pelo OBF25100.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1040986894)

#### Documento Fiscal - Indicador Móvel Bem Usado e Indicador de Doação

Alterado a integração OBF12000 para atender os novos tributos relacionados ao indicador de Móvel bem usado e doação para notas fiscais de entradas e saída, consulta dos documentos fiscais e relatórios gerados pelo OBF25100.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1042909352)

#### OBF26300 - Zoom do campo Nota Fiscal

Alterado o programa Inclusão de Eventos (OBF26300), para corrigir os campos utilizados no arquivozoom_nf_origem_obf_fat, para que não ocorra erro no zoom do campo Nota Fiscal.

[Mais informações](https://tdn.totvs.com/display/LLOG/26512561+DBACKFISUST-6183+-+DT+OBF26300+-+Zoom+do+campo+Nota+Fiscal)

#### OBF25100 - Consulta de documentos fiscais - Detalhes

Alterado o programa para exibir os detalhes da nota de saída corretamente, independentemente do tipo de cadastro do cliente no **VDP10000** .

### Pacote 06/04

#### Documentos Fiscais - NBS

Alterado a integração de saídas para preencher o campo NBS com valor gravado na nota fiscal de saída.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1050284818)

#### Documento Fiscal - CBS/IBS - Grupo Estorno de Crédito e Ajuste de competência

Alterado a integração OBF12000 para atender os novos tributos relacionados ao Grupo de estorno de crédito e ajuste de competência para notas fiscais de entradas e saída, consulta dos documentos fiscais e relatórios gerados pelo OBF25100.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1051258053)

#### Adequações na Integração e Consulta de Documentos Fiscais

Realizado ajustes gerais na integração OBF12000, consulta dos documentos fiscais e relatórios gerados pelo OBF25100.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1045394445)

### Pacote 27/04

#### OBF25000 - Cockpit Fiscal e Conferência da Apuração Assistida

Foi disponibilizada a funcionalidade de conferência da apuração assistida, com o objetivo de apoiar a validação dos valores apurados de IBS e CBS.

A rotina permite a geração de relatórios em Planilha com visões **resumida (por documento)** e **detalhada (por item)** , possibilitando maior rastreabilidade das informações. Também foram incorporadas opções de **totalizações e resumos analíticos** , como por CST, classificação tributária, crédito presumido, UF e município, facilitando a análise e conferência dos dados.

[Guia do usuário: OBF25000 – Cockpit Fiscal](https://tdn.totvs.com/pages/viewpage.action?pageId=1058458129)

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1046414601)

#### Ajuste na gravação das informações de incidência, CST e Classificação Tributária

Alterado a integração de entradas para que se os campos declaradoestiver preenchido, o sistema utilizará obrigatoriamente ovalor informado pelo usuário.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1054129527)

#### Documento Fiscal - NFAg (Modelo 75)

Alterado a integração OBF12000 para atender os novos tributos relacionados ao modelo nacional de documento fiscal eletrônico (modelo 75) para notas fiscais de entradas e saída, consulta dos documentos fiscais e relatórios gerados pelo OBF25100.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1053177928)

#### Adequações na Integração e Consulta de Documentos Fiscais

Alterado o programa Inclusão de Eventos (OBF26300),para buscar os dados da série selecionada em tela.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1056132070)

### Pacote 18/05

#### Ajuste SINIEF 49/25 e Notas de Crédito/Débito

Foi alterado os programas para Notas de Crédito (finNFe=5) conforme o Ajuste SINIEF 49/25, os programas de integração e consulta para permitir a escrituração híbrida e a rastreabilidade entre notas de devolução.

[Mais Informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1066120616)

### Pacote 08/06

#### OBF25500 - Conferência da Apuração Assistida - Resumo por Alíquota

Foi alterado o programa para gerar o **resumo por alíquota** com base nos documentos fiscais e valores do relatório de documentos. Nele, os valores são agrupados pororigem do documento fiscale alíquota, facilitando a análise tributária.

[Mais Informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1046414601)

#### Documentos Fiscais saída - Grupo CBS/IBS Diferido

Alterado o programa Integração para Obrigações Fiscais (OBF12000), para entradas, fretes e saídas, incluindo as informações relacionadas ao grupo do diferimento para IBS e CBS. Também foi alterado o programa OBF25100 de consulta dos documentos fiscais, permitindo visualizar os valores de Perc. Diferido e Valor Diferido referente aos tributos CBS, IBS_MUN e IBS_UF no relatório do programa gerado em planilha.

[Mais Informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1043713991)

#### Documento Fiscal - NFAg (Modelo 75)

Alterado a integração OBF12000 para atender os novos tributos relacionados ao modelo nacional de documento fiscal eletrônico (modelo 75) para notas fiscais de entradas e saída, consulta dos documentos fiscais e relatórios gerados pelo OBF25100.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1053177928)

#### NFSe Via - Documento Fiscal

Alterado os programas de integração OBF12000 e OBF25000, consulta de documentos fiscais. Para atender este novo modelo de nota.

[Mais informações](https://tdn.totvs.com/x/2zlxPw)

#### Documento Fiscal - NFS-e Nacional/Layout Unico

Foram feitas adequações no módulo de Obrigações Fiscais (OBF) do Logix para a recepção e processamento dos dados da NFSe Nacional, garantindo a integridade das informações fiscais e a plena conformidade com a legislação.

[Mais informações](https://tdn.totvs.com/x/XKuZPw)

#### OBF25100 gera xml (excel) sem dados do IPI

Alterado o programa Consulta de Documentos Fiscais (OBF25100), para gerar os dados do IPI corretamente na planilha.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1068936845)

### Pacote 20/07

#### OBF26000 - Automatização dos eventos

A Central de Eventos foi atualizada com o novo sistema de automação. Seguem as modificações realizadas nos programas do módulo:

**OBF26000 (Cockpit centralizador):** Incluído atalho rápido para as novas rotinas de automação de eventos.

**OBF26100 (Cadastro):** Passou a gravar a origem da nota (Entrada/Saída) conforme o evento, orientando os programas posteriores.

**OBF26200 (Consulta):** Ganhou filtro por tipo de inclusão (manual/automática) e avisos mais claros sobre eventos de cancelamento.

**OBF26300 (Motor de Processamento):** Reestruturado para rodar no modo manual ou automático, centralizou o tratamento de erros (com logs /JOB) e limitou a sequência máxima de eventos em 99.

**OBF26400 e OBF26410 (Cenários e Auditoria):** Permite criar regras dinâmicas de automação por chaves (item, cliente, etc.) com numeração anti-duplicidade e rastreabilidade total de alterações.

**OBF26500 (Gerador / JOB0003):** Novo programa para simular cenários (modo Prévia) ou efetivar gravações (modo Oficial). Pode ser disparado manualmente ou de forma agendada via **JOB0003** , gerando sempre relatórios de conferência e inconsistências.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1066119175)

#### OBF26000 - Implementação do novo status de envio '6 - Em fila, aguardando envio'

A solução passa a controlar o fluxo de envio de eventos com o novo status6 - Em fila, aguardando envio, preservando a ordem de envio e evitando concorrência indevida para o mesmo evento e mesma chave de acesso. A liberação automática do próximo item da fila ocorre apenas após retorno definitivo, garantindo consistência no processo de transmissão e retorno.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1078598670)

### Pacote 10/08

#### Adequações NT 2025.002 v.1.40/v.1.50

Alterado o programa de Cadastro de Eventos(OBF26100) e de Inclusão de Eventos (OBF26300) para atender às exigências da **Nota Técnica 2025.002 v1.40** , relacionada à Reforma Tributária do Consumo para NF-e e NFC-e.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1079785933)

#### Imposto Seletivo

Alterado os seguintes programas para prever no Imposto seletivo a Integração de documentos Fiscais(OBF12000) entradas e saídas, Consulta de Documentos Fiscais(OBF25100), Histórico dos Documentos Fiscais(OBF12002), Conferência da Apuração Assistida(OBF25500)

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1074621503)

#### Documento Fiscal - NFGás (Modelo 76)

Alterado a integração OBF12000 para atender os novos tributos relacionados ao modelo nacional de documento fiscal eletrônico (modelo 76) para notas fiscais de entradas.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1102927323)

#### Evento 211130 - OS e Parcela

Alterado o programa Inclusão de Eventos (OBF26300),para apresentar o número da OS e parcela do bem que está sendo gerado o evento.

[Mais informações](https://tdn.totvs.com/display/LLOG/DBACKRTLGX-5475+DT+OBF26300+e+OBF26200+novas+colunas+Numero+da+OS+e+Numero+da+Parcela)

### Pacote 31/08

#### Grupo de Compra Governamental - IBS 2027

Alterado os programas Integração de documentos Fiscais(OBF12000) entradas e saídas, Consulta de Documentos Fiscais(OBF25100), Histórico dos Documentos Fiscais(OBF12002), Conferência da Apuração Assistida(OBF25500) para prever as operações de **compras governamentais** , incluindo o tratamento diferenciado do IBS e da CBS.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1107380043)

#### Automatização dos Eventos - Eventos PAT e CRE

Alterado os programas de Inclusão Manual de Eventos (OBF26300), permitindo a geração automática dos eventos da Reforma Tributária relacionados ao Patrimônio e ao Contas a Receber

[Mais informações](https://tdn.totvs.com/x/oqkwQg)

#### NF-e ABI

Alterado os seguintes programas para prever Documento Fiscal **NF-e ABI** , modelo **77** , a Integração de documentos Fiscais(OBF12000) entradas e saídas, Consulta de Documentos Fiscais(OBF25100), Histórico dos Documentos Fiscais(OBF12002), Conferência da Apuração Assistida(OBF25500)

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1107376529)

### Pacote 21/09

#### Eventos ECONF

Alterado os programas do OBF26000 para contemplar os eventos ECONF ( **110750 e 110751)** na inclusão manual, geração do XML e integração (envio/retorno) dos eventos pelos transmissores TSS e TC2.

[Mais informações](https://tdn.totvs.com/x/fJHMQg)

#### Grupo Zona Franca de Manaus(ZFM) e das Áreas de Livre Comércio(ALC)

Alterado os programas Integração de documentos Fiscais(OBF12000) entradas e saídas, Consulta de Documentos Fiscais(OBF25100), Histórico dos Documentos Fiscais(OBF12002) para prever as operações da ZFM e ALC.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1114970479)

#### Documentos Fiscais - NFSe Locação

Alterado os programas Integração de documentos Fiscais(OBF12000) de entradas, Consulta de Documentos Fiscais(OBF25100), Histórico dos Documentos Fiscais(OBF12002) para prever as operações de NFSe de Locação.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1105497898)

#### OBF25100 - Não apresenta documentos fiscais com registro de entrada diferente de 1

Alterados os programas **Processamento das Informações para os Livros Fiscais** **(OBF12000)** , **Consulta de Documentos Fiscais (OBF25100)** e **Conferência da Apuração Assistida (OBF25500)** ,para verificar o registro de entrada da nota fiscal de serviço pelo parâmetro "Registro entrada serviços outros", cadastrado no programa **Padrões Recebimento/Compras (SUP1180)** .

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1113819399)

#### Integração das Notas Fiscais de Débito e Crédito com ICMS/IPI

O programa **Processamento das Informações para os Livros Fiscais (OBF12000)** foi alterado para integrar os tributos **ICMS** e/ou **IPI** , além de **IBS** , **CBS** e **IS** , para as notas fiscais de débito e crédito,

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1117678408)

### Pacote 26/10

#### Grupo Zona Franca de Manaus(ZFM) e das Áreas de Livre Comércio(ALC) - Frete

Alterado os programas Integração de documentos Fiscais(OBF12000) entradas e saídas, Consulta de Documentos Fiscais(OBF25100), Histórico dos Documentos Fiscais(OBF12002) para prever as operações da ZFM e ALC.

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1114970479)

#### Documentos Fiscais - Grupo Monofásico

Alterados os programas **Processamento das Informações para os Livros Fiscais** **(OBF12000)** , **Consulta de Documentos Fiscais (OBF25100)** e **Conferência da Apuração Assistida (OBF25500)** , para prever as operações do Grupo do Monofásico

[Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=1138244683)
