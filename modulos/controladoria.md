# Reforma Tributária Logix — Controladoria

Fonte: <https://tdn.totvs.com/pages/releaseview.action?pageId=1016684320>

## 1. Visão Geral

A **Reforma Tributária** traz um cenário de mudanças significativas nas regras tributárias brasileiras, exigindo das empresas uma adaptação rápida e precisa para garantir conformidade e eficiência operacional.

## Pacote 11/08

- **PAT10028 ou PAT100281 - Informações básicas do bem**

Foi preparado para que, quando ocorrer imobilização da Nota Fiscal de Entrada de Ativo Imobilizado, possam ser informados os valores de CBS e IBS para o inventário no Patrimônio:

Para inventários incluídos com data retroativa, também poderão ser informados os valores de CBS e IBS:

- **PAT100281 - Baixa inventário**

Ao ser efetuada uma baixa, será feita a atualização dos valores dos tributos CBS e IBS para o inventário:

## Pacote 22/09

- **PAT10030 - Importa dados do suprimentos sem ordem de serviço**

Ao imobilizar a Nota Fiscal de Entrada, irá atualizar os valores de CBS e IBS dos inventários.

Importação dos valores dos tributos referentes a Nota Fiscal:

Ao consultar o inventário no PAT100281:

Para acompanhamento e auditoria nos valores de CBS e IBS dos inventários, foi desenvolvido o relatório **PAT10168 - Relatório de inventário - CBS e IBS** , que permite realizar filtro informando várias empresas em um mesmo processamento ou solicitar apenas para a empresa corrente, listando os bens de inventário e suas parcelas. É possível gerar os dados também em planilha.

Relatório gerado:

Possui opção em gerar em planilha:

## Pacote 17/11

Todo o controle dos eventos será feito na página centralizadora **OBF26000 - Cockpit Eventos** do módulo Fiscal do Logix.

- **Conforme NT 2025.002 v1.30 -** Deverá ser gerado o evento 211130 - Imobilização de item. O Patrimônio foi alterado para a geração manual do evento 211130 e seu respectivo cancelamento.

- **PAT101042 - Relacionamento notas de entrada com o inventário**

Ao ser informado o relacionamento do inventário com a Nota Fiscal de Entrada, será armazenada a chave de acesso da Nota Fiscal.

## Pacote 08/12

O relatório de **Eventos da NF-e – Ativo Imobilizado** tem como objetivo apresentar uma visão consolidada entre os **inventários do módulo de Patrimônio** e os **eventos eletrônicos transmitidos à SEFAZ** relacionados à **imobilização de itens** (evento211130 – Inclusão do Ativo Imobilizado) e ao **cancelamento da imobilização** (evento 110001 – Cancelamento da Inclusão do Ativo Imobilizado).

Serão selecionados os inventários que possuam a incidência de créditos de IBS e CBS conforme a **Lei Complementar nº 214/2025 (Reforma Tributária)** .

- **PAT10028 - Manutenção de bens e PAT100281 - Manutenção das parcelas do bem**

Estas rotinas foram ajustadas para verificar o status de envio do evento 211130 e 110001 na opção de exclusão do inventário. Se o inventário tiver evento com status conforme abaixo:

**1 - Evento 211130 - pendente de envio** - será permitido a exclusão do inventário.

**2 - Enviado, aguardando retorno de autorização** - não será permitida a exclusão.

**3 - Autorizado - será permitido a exclusão do inventário** - será gerado um evento 110001 de cancelamento.

**4 - Cancelamento enviado, aguardando retorno de autorização** - não será permitida exclusão.

**5 - Cancelamento autorizado** - será permitida a exclusão.

**R - Evento rejeitado** - será apresentada pergunta para confirmação da exclusão.

## Pacote 23/02

**Funcionalidades Principais:**

- Adequação dos programas e telas da Contabilidade para o CNPJ Alphanumérico :

**Hoje**

Contamos com 14 posições numéricas – NN.NNN.NNN/NNNN-NN

Raiz da Empresa – NN.NNN.NNN

Estabelecimento – /NNNN

Dígitos verificadores – NN

**Alteração**

Continuará com 14 posições, agora alfanuméricas – SS.SSS.SSS/SSSS-NN

Raiz da Empresa – SS.SSS.SSS

Estabelecimento – /SSSS

Dígitos verificadores – NN

## Pacote 06/04

**PAT10062 - Importação dos gastos com ordem de serviço**

- Foi ajustado para importar os valores de CBS e IBS para as ordens de serviço de imobilizado em andamento.

**PAT10104 - Manutenção das parcelas da ordem de serviço**

- Possibilita apresentar os valores de CBS e IBS das ordens de serviço.

**PAT100312 - Imobilização de ordem de serviço**

- A imobilização das ordens de serviço, com valores de CBS e IBS, foi ajustada para informar as notas fiscais relacionadas. Também será atualizado o relacionamento do inventário e parcela e Nota Fiscal e poderá consultar no botão "Entrada", na tela **PAT10104 - Manutenção das parcelas da ordem de serviço.** Ao informar "Quantidade de inventários" maior que 1, será aberta tela para informar aviso de recebimento e sequência do item da nota. Poderá acessar no zoom das notas para selecionar a Nota Fiscal.

Ao ser selecionado, irá buscar as informações da Nota Fiscal:

**PAT100288 - Transferência entre parcelas**

- Feita alteração na rotina de transferência entre parcelas para atualizar os valores de CBS e IBS. Esta rotina é chamada pelo **PAT100281 - Manutenção das parcelas de bens do patrimônio,** no botão "Transferir".

## Pacote 18/05

**PAT100312 - Imobilização de ordem de serviço**

A rotina de imobilização das ordens de serviço foi ajustada para possibilitar o registro das Notas Fiscais com as ordens de serviço (OS), quando as ordens de serviço possuírem inventários relacionados no **PAT10140 - Relacionamento entre inventário e ordem de serviço.**

Traz informado o **Aviso de recebimento** , sequência do item na **Nota Fiscal** e informações da Nota Fiscal para cada parcela da OS. Caso não traga automaticamente o aviso de recebimento e sequência do item na Nota Fiscal, estes poderão ser informados manualmente para cada parcela da OS.

Ao consultar as parcelas da OS no **PAT10104 - Parcelas da OS** , no botão "Entrada" é possível verificar qual Nota Fiscal/Aviso de Recebimento está relacionado com o inventário e parcela:

**Notas de transferência entre unidades de inventários**

Realizado ajuste na rotina de transferência entre unidades para que os valores de CBS e IBS do inventário da empresa origem sejam transferidos para o inventário da empresa destino.

**PAT10103 - Transferências de Inventário**

Ajustada a rotina de transferência de inventários para atualizar valores de CBS e IBS do inventário da empresa origem para o inventário na empresa destino.

**PAT10081 - Cancelamento de Transferências de inventário**

Feito ajuste na rotina de cancelamento de transferência de inventário para excluir valores de CBS e IBS para o inventário destino, no cancelamento da transferência de inventário feito entre empresas.

**PAT100281 - Transferência de parcelas do bem**

Rotina de transferência entre parcelas de inventários foi alterada paraverificar a existência do evento 211130 e tratar cada transferência parcial ou total conforme o **status de envio** **do evento** . Esta funcionalidade de transferência encontra-se no **PAT100281 - Manutenção das parcelas do inventário** .

Para inventário que possui evento 211130 - Imobilização de itens - com **status de envio** como " **Enviado, aguardando retorno de autorização** " ou " **Cancelamento enviado, aguardando autorização** ", a transferência não será permitida. Será emitida mensagem informativa em tela e o processamento da transferência será cancelado.

Para eventos com **status de envio** igual a **Pendente de envio** ou **Rejeitado,** o evento do inventário e parcela origem será excluído na transferência.

Para eventos com **status** de envio igual a **Autorizado** , será gerado um evento de **cancelamento - 110001** - para o inventário e parcela origem.

## Pacote 08/06

Neste pacote estão incluídas algumas alterações conforme abaixo descritas:

- **PAT10062 - Importação dos gastos com ordens de serviço**

A rotina **PAT10062 - Importação dos gastos com ordens de serviço** - irá sempre gerar o relacionamento da OS - ordem de serviço - com a nota fiscal de entrada de acordo com a data de início da reforma tributária. A data de início da reforma tributária será informada no **LOG00087 - Manutenção de parâmetros** . É necessário processar o conversor **PAT00189.CNV** para gerar o parâmetro **data_inicio_rt_pat** no PROCESSO ADM/FINANC - PATRIMONIO - REFORMA TRIBUTÁRIA.

Caso a data de início da reforma tributária no patrimônio não seja informada, a rotina de importação PAT10062 irá verificar a data do CIAP e, se o objetivo do grupo de despesa do item da nota fiscal de entrada de imobilizado for igual a 6 - Imobilizado CIAP, então será gerado o relacionamento entre nota e ordem de serviço no **PAT101042 - Notas de entrada para geração de inventário** .

- **PAT101042 - Notas de entrada para geração de inventário**

A rotina **PAT101042 - Notas de entrada para geração de inventário** foi alterada para não gerar evento 211130 - Imobilização de item - na inclusão do relacionamento da nota fiscal de entrada com o inventário e parcela. Nas opções de excluir e modificar, continuará verificando o status de envio do evento. Caso o evento 211130 esteja com status 3 - autorizado, será gerado o evento de cancelamento 110001. A rotina **PAT101042 - Notas de entrada para geração de inventário -** pode ser acessada pelo botão "Entrada" no **PAT100281 - Parcelas do inventário** e **PAT10104 - Parcelas da OS.**

A geração automática do evento **211130 - Imobilização de item** será feita no fiscal ou na rotina de JOB.

- **PAT100288 - Transferência entre parcelas de inventário**

Feito ajuste na rotina **PAT100281 - Parcelas de inventário -** opção "Transferir" para não exigir chave de acesso na transferência entre parcelas de inventário. Estava ocorrendo a mensagem: "Chave de acesso do AR: 99999 não informada. Ver PAT101042" e cancelando a transferência.

## Pacote 10/08

Neste pacote estão incluídas algumas alterações conforme abaixo descritas:

- **PAT10104 - Parcelas da ordem de serviço**

A rotina **PAT10104 - Parcelas da ordem de serviço -** foi ajustada para não permitir cancelar a imobilização quando a parcela da OS - Ordem de serviço - tiver um evento **211130 - Imobilização de item** com status de envio igual a **2 - Enviado, aguardando retorno de autorização** ou possua um cancelamento do evento 211130 - Imobilização com status de envio como **4 - Cancelamento enviado, aguardando retorno de autorização** .

**OBF26000 - Cockpit eventos IBS/CBS - Opção Enviar**

Feito ajuste na rotina de envio do evento **211130 - Imobilização de item** - para apresentar o XML do evento com os valores corretos das ordens de serviço, relacionados aos inventários e parcelas. Deverá ser processado conversor **PAT00190.CNV** para alteração na tabela **PAT_EVENTO_ORIGEM** .

O evento acima refere-se a OS 300726 :

Ao fazer o envio gera o XML:

## Pacote 31/08

Neste pacote estão incluídas algumas alterações conforme abaixo descritas:

- **OBF26500/PAT80006 - Geração automática do evento 211130 - Imobilização de item**

Neste pacote houve a geração do evento **211130 - Imobilização de item** de forma automática, através da rotina do fiscal **OBF26500 - Gerador de eventos** . É necessário incluir regras na rotina **OBF26400 - Configuração de cenários.**

Após a inclusão das regras, processar o **OBF26500 - Gerador de eventos** para o evento do patrimônio **211130 - Imobilização de item** :

Caso seja marcado o campo "Tipo" como **Prévia** , somente será gerado um relatório com as inconsistências encontradas. O evento do patrimônio somente é gerado se o campo "Tipo" for marcado como **Oficial** .

Ao processar, serão gerados os eventos **211130** para as notas de entrada de imobilizado, conforme o período informado em tela.

Os eventos podem ser consultados no **OBF26000 - Cockpit de eventos.**

O **OBF26500** foi alterado para ser processado via **JOB0003** (Agendador de Tarefas Logix). Deverão ser informado os parâmetros para o **OBF26500** e o evento do patrimônio **211130 - Imobilização de item** :

**Automatização de Eventos PAT.**

- **OBF26200 - Eventos 211130 - Imobilização de item - tratamento do novo status: "6 - Em fila, aguardando envio"**

Fizemos ajustes nas rotinas abaixo listadas para verificar o novo status de envio do evento "6 - Em fila, aguardando envio", na função de exclusão:

- **PAT10028/PAT100281 - Manutenção do bem** – Ao excluir o inventário, verificar se existe evento **211130 - Imobilização de item** com status **6 - Em fila, aguardando** **envio** e permitir a exclusão do inventário e a exclusão do evento 211130.
- **PAT100288 - Transferência de parcelas do bem** – Ao transferir uma parcela de inventário, permitir a exclusão do evento **211130 - Imobilização de item** com status **6 - Em fila, aguardando** **envio** .
- **PAT10169 - Relatório de eventos do ativo imobilizado** – Ajustar para listar a descrição do status de envio **6 - Em fila, aguardando** **envio** na coluna "Situação evento" do relatório.
- **PAT10104 - Parcelas da ordem de serviço** – No momento de cancelar a imobilização da parcela da OS, verificar se tem evento **211130 - Imobilização de item** com status **6 - Em fila, aguardando** **envio** e permitir a exclusão do evento. Também foi ajustada a função de cancelamento da imobilização para **não excluir o relacionamento com a nota fiscal de entrada** .

A opção ' **Entrada** ' irá abrir a rotina para informação das notas relacionadas a OS - ordem de serviço, sem primeiramente entrar na opção **Incluir** :

## Pacote 12/10

Neste pacote ocorreu alteração no :

- **PAT10169 - Relatório de eventos do Imobilizado x Inventários** :

Foi ajustado para listar o número da ordem de serviço, quando o inventário tiver o evento **211130 - Imobilização de itens** gerado e foi imobilizado com valores de ordens de serviço.

Também será possível selecionar as ordens de serviços dos inventários que tenham evento **211130 - Imobilização de itens** - gerados.

Relatório gerado:
