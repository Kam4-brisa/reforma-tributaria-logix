# Reforma Tributária Logix — Financeiro

Fonte: <https://tdn.totvs.com/pages/releaseview.action?pageId=1009450308>

## 1. Visão Geral

A **Reforma Tributária** traz um cenário de mudanças significativas nas regras tributárias brasileiras, exigindo das empresas uma adaptação rápida e precisa para garantir conformidade e eficiência operacional.

No módulo de Vendas existe uma demanda que depende do módulo do Financeiro no que diz respeito ao **Evento** **112110 - Efetivo pagamento integral para liberar crédito presumido do adquirente** . Esse evento tem a função de informar que o pagamento integral da operação foi realizado, visando a liberação do crédito presumido para o adquirente, no contexto da apuração do IBS e da CBS (Reforma Tributária), sendo o autor do evento a Empresa emitente da NF-e.

## Pacote 17/11/2025

[Documento de referência OBF26000 - Cockpit Eventos](https://tdn.totvs.com/pages/viewpage.action?pageId=1015546114)

Para que seja possível gerar os eventos relativos a quitação integral da Nota Fiscal, de forma manual, acessar o **OBF26000 - Cockpit Eventos** - do módulo Fiscal do Logix,

Através da opção **"OBF26000 - Cockpit Eventos \ Inclusão Manual"** , ao acessar essa opção será aberta a tela "Inclusão de eventos" a qual será possível incluir os eventos de quitação.

**Critérios para a geração do evento de Quitação**

No momento da inclusão do evento, alguns critérios serão avaliados, sendo eles:

- Notas Fiscais que possuam crédito presumido calculado;
- Notas Fiscais que possuam chave de acesso;
- XML da Nota Fiscal Eletrônica sido transmitido;
- XML da Nota Fiscal Eletrônica tenha protocolo;
- XML da Nota Fiscal Eletrônica **não** deve estar em situação: Inutilizado, Denegado ou Cancelado;
- Duplicatas totalmente liquidadas;
- Se houver renegociação de títulos, todos deverão ter sido liquidados;
- O último evento gerado não poderá ser de quitação, a não ser que o mesmo tenha sido rejeitado.

Caso a Nota Fiscal informada se enquadre em todos esses critérios, será possível gerar o evento para ela.

Através da opção **"OBF26000 - Cockpit Eventos \ Central de Eventos"** do cockpit, ao acessar essa opção será aberta a tela onde é possível consultar todos os eventos incluídos, com filtros que permitem selecionar os eventos de Quitação e/ou Cancelamento de quitação com informações como: Evento, Status de Envio, Origem, Data de inclusão, Nota Fiscal, Chave da NFe, entre outros.

Além de consultar, existem os botões:

" **Enviar** " - Realiza a geração do XML e envio dos eventos selecionados.

" **Cancelar** " - Gera o evento de cancelamento de envio para os eventos selecionados. O evento de cancelamento será gerado conforme critérios que serão validados antes do processamento efetivo.

Existe nessa tela, na última coluna dos dados consultados, uma **lupa** que apresenta detalhes sobre o evento consultado, a seguinte tela é apresentada.

Os dados do XML gerado podem ser acessados através da aba " **2 - XML** ".

É possível consultar os títulos relacionados ao evento de Quitação através do botão " **Consultar títulos** " disponível na aba " **1 - Dados gerais** ".

Nessa tela também existe uma lupa na coluna " **Detalhe** ", onde ao acessar, será aberto detalhes sobre o título que poderão ser consultados.

**Situação de Notas Fiscais x Eventos de Quitação - FIN10208.**

Criação do relatório **FIN10208 - Situação de Notas Fiscais x Eventos de Quitação** utilizado para demonstrar a Situação de Notas Fiscais x Eventos de Quitação e Cancelamento de Quitação, que atenderá as seguintes necessidades:

- Garantir a integridade dos eventos gerados no sistema;
- Acompanhar os eventos de Quitação e Cancelamento de Quitação a fim de validar se estão consistentes, de acordo com a situação atual da Nota Fiscal;
- Conferir eventos rejeitados ou pendentes de envio.

O relatório avalia o último evento gerado para a Nota Fiscal, para então realizar os filtros informados em tela, e enfim trazer a situação desse evento em comparação com a situação atual da Nota Fiscal, podendo ela estar Liquidada ou Aberta. O relatório demonstra informações necessárias para avaliar a situação atual da Nota Fiscal x Último Evento gerado para acompanhamento e geração de eventos quando identificado a necessidade. Abaixo o layout para conferência.

Relatório gerado em planilha.

## Pacote 23/02/2026

**Funcionalidades Principais:**

- Adequação dos programas e telas do financeiro para o CNPJ Alphanumérico :

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

## Pacote 06/04/2026

[Manutenção dos Tributos CBS/IBS/IS - FIN10209](https://tdn.totvs.com/pages/viewpage.action?pageId=1041788645)

Criado o programa para consulta dos impostos relacionados aos títulos e permite também realizar a inclusão dos impostos e manutenção nos mesmos.

**Importante** : Os dados dos tributos precisam estar relacionados ao título mas também a Nota Fiscal de origem, considerando que é possível ter mais do que uma Nota Fiscal de origem para os documentos.

**Considerações Gerais:**

As seguintes condições são validadas ao utilizar esse programa:

- Permitido incluir manualmente valores para os tributos;
- Permitido informar somente tipos de títulos com o parâmetro"Efetuar retenção de IBS/CBS/IS?" marcado;
- Permitido modificar ou excluir somente se a inclusão foi realizada manualmente;
- Para títulos que possuam baixas, não será permitido modificar os dados ou excluir;
- Os dados da aba "1 - Previsão" contém os dados relacionados aos impostos calculados na Nota Fiscal;
- Os dados da aba "2 - Tributo" contém os valores calculados para cada baixa realizada. Esses dados ficam disponíveis apenas para consulta.

**FIN10050 - Manutenção de títulos no Contas a Receber**

Ao realizar a inclusão de um título, ao final da inclusão, perguntar “Deseja informar os tributos IBS Mun, IBS UF, CBS, IS?”. Se sim, a inclusão do título é finalizada e a tela de inclusão de tributos é aberta para que as informações de impostos previstos possa ser informada. Essa mensagem será apresentada somente se o parâmetro "Efetuar retenção de IBS/CBS/IS?" no FIN10007 - Tipos de títulos, estiver marcado.

Criado um novo botão, "Consultar IBS/CBS" onde ao ser chamado na consulta, a tela de consulta traz os valores já consultados.

## Pacote 18/05/2026

Este pacote contempla as seguintes liberações:

- Integração dos impostos calculados nas Notas Fiscais a partir do módulo de Vendas.
- Alteração na estrutura das tabelas cre_previsao_ibs_cbs, cre_previsao_ibs_cbs_hist, cre_tributo_ibs_cbs e cre_tributo_ibs_cbs_hist.
- FIN10007 - Alteração no cadastro de Tipos de Títulos.

[Tipos de Títulos - FIN10007](https://tdn.totvs.com/pages/viewpage.action?pageId=283403542)

Foi incluído, na aba "2 - Complementos", o campo "Efetuar retenção de IBS/CBS/IS?" para indicar seos tipos de títulosdeverão efetuar ou não retenção dos novos tributos.

## Pacote 29/06/2026

Este pacote contempla as seguintes liberações:

- Baixas manuais e escriturais dos tributos IBS/CBS/IS

[Formas de Baixas - FIN10004](https://tdn.totvs.com/display/LLOG/Formas+de+Baixas+-+FIN10004)

- Foi incluído na tela principal o campo "Reter IBS/CBS/IS?" para indicar se as baixas efetuadas pela forma de baixa deverão efetuar ou não retenção dos novos tributos.

[Portadores - FIN10016](https://tdn.totvs.com/display/LLOG/Portadores+-+FIN10016)

- Foi incluído, na aba "2 - Parâmetros Gerais", o campo "Reter IBS/CBS/IS?" para indicar se as baixas efetuadas pelo portador deverão efetuar ou não retenção dos novos tributos.

[Baixa de títulos - FIN10060](https://tdn.totvs.com/pages/viewpage.action?pageId=555850211)

FIN10115 - Baixa Escritural de títulos

- Ao realizar a baixa de títulos que contém dados de IBS Mun, IBS UF, CBS, IS e também de PIS, COFINS, CSLL ou IRRF, o programa realizará o cálculo dos impostos e efetuará a baixa por retenção desses valores.

[Exclusão de Baixas - FIN10061](https://tdn.totvs.com/pages/viewpage.action?pageId=327334266)

- Ao realizar a exclusão de baixas que contém dados de IBS Mun, IBS UF, CBS, IS calculados, o programa realizará a exclusão destes valores.

LOG00087 - Manutenção de Parâmetros - **Logix Financeiro/Contas a Receber/Impostos - IBS/CBS/IS**

- Foram criados os seguintes parâmetros:
- Código do portador para geração de retenção de CBS na baixa - 'cod_portador_pgto_cbs'
- Tipo do portador para retenção de CBS na baixa - 'tip_portador_pgto_cbs'
- Forma de Pagamento para Retenção de CBS - 'forma_pgto_ret_cbs'
- Código do portador para geração de retenção de IBS MUN na baixa - 'cod_portador_pgto_ibs_mun'
- Tipo do portador para retenção de IBS MUN na baixa - 'tip_portador_pgto_ibs_mun'
- Forma de Pagamento para Retenção de IBS MUN - 'forma_pgto_ret_ibs_mun'
- Código do portador para geração de retenção de IBS UF na baixa - 'cod_portador_pgto_ibs_uf'
- Tipo do portador para retenção de IBS UF na baixa - 'tip_portador_pgto_ibs_uf'
- Forma de Pagamento para Retenção de IBS UF - 'forma_pgto_ret_ibs_uf'
- Código do portador para geração de retenção de IS na baixa - 'cod_portador_pgto_is'
- Tipo do portador para retenção de IS na baixa - 'tip_portador_pgto_is'
- Forma de Pagamento para Retenção de IS - 'forma_pgto_ret_is'
- Campo ref valor da diferença da retenção CBS/IBS/IS será atribuído - 'campo_difer_calc_trib'
- Código do portador para gerar Nota de Crédito - 'cod_portador_nc'
- Tipo do portador para gerar Nota de Crédito. - 'tip_portador_nc'
- Código de crédito do cliente para criação de Nota de Crédito - 'cod_credito_nc'
- Baixar valor de impostos na baixa parcial de um título? - 'baixar_imposto_na_bxa_parcial'
- Valor permitido como diferença no cálculo dos valores de retenção. - 'difer_permit_calc_ret'

## Pacote 31/08/2026

Automatização de Evento

[Documento de referência OBF26000 - Cockpit Eventos](https://tdn.totvs.com/pages/viewpage.action?pageId=1015546114)

Para que seja possível gerar de **forma automática** os eventos 112110 relativos a "Informação de efetivo pagamento integral para liberar crédito presumido do adquirente", será necessário cadastrar cenários que serão utilizados para a geração dos eventos via programa **OBF26500 - Gerador de eventos** ou através do **JOB0003 - Agendador de tarefas.**

Para realizar o cadastro dos novos cenários, acessar o **OBF26000 - Cockpit Eventos** , opção **"OBF26400 - Configuração de Cenários",** do módulo Fiscal do Logix,

Através do **OBF26400 - Configuração de Cenários** , cadastrar um cenário onde serão definidos os critérios que serão utilizados para realizar os filtros e pesquisas das notas fiscais que serão consideradas para geração dos eventos.

Opção **"OBF26000 - Cockpit Eventos \ Gerador de Eventos":** ao acessar essa opção será aberta a tela OBF26500 para informar os dados da tela para seleção das notas fiscais para incluir os eventos de quitação.

Ao final do processo o programa emite um relatório no formato planilha com as notas fiscais selecionadas para geração do evento.

Opção **"OBF26000 - Cockpit Eventos \ Central de Eventos"** do cockpit: ao acessar essa opção será aberta a tela onde é possível consultar todos os eventos incluídos, com filtros que permitem selecionar os eventos de Quitação e/ou Cancelamento de quitação com informações como: Evento, Status de Envio, Origem, Data de inclusão, Nota Fiscal, Chave da NFe, entre outros.

Além de consultar, existem os botões:

" **Enviar** " - Realiza a geração do XML e envio dos eventos selecionados.

" **Cancelar** " - Gera o evento de cancelamento de envio para os eventos selecionados. O evento de cancelamento será gerado conforme critérios que serão validados antes do processamento efetivo.

Será possível executar o **"OBF26500 - Gerador de Eventos"** através do agendador de tarefas do Logix, cadastrando a rotina no programa JOB0003.

No link [Guia do Usuário: OBF26000 - Cockpit Eventos](https://tdn.totvs.com/pages/viewpage.action?pageId=1015569222) na aba **"Automatização de eventos - JOB0003 - Execução Automática"** são demonstradas as regras para configuração dos parâmetros do JOB0003 para executar o OBF26500 via agendador de tarefas.

Juros e Multas

Para a Geração de Notas Fiscais de Débito no módulo de Vendas, foram realizados ajustes de forma a calcular e registrar automaticamente, no momento da baixa, os valores relacionados ao título baixado. Também alteramos as consultas e cadastros dos tributos por título. Criamos uma consulta para controle de valores pendentes ou já integrados. Nessa mesma tela é possível realizar a geração da Nota Fiscal de Débito no módulo de Vendas.

[Manutenção dos Tributos CBS/IBS/IS - FIN10209](https://tdn.totvs.com/pages/viewpage.action?pageId=1041788645)

Ao realizar a inclusão manual dos impostos previstos e o tipo de documento for Nota de Débito (ND), serão apresentados os valores da multa e juros relacionado à NF no grid da aba "1-Previsão".
Será permitido informar valores para multa e juros somente quando o tipo de documento for Nota de Débito (ND).
Nesta tela, será possível consultar os valores de multa e juros previstos para as NDs geradas automaticamente ou manualmente. Quando essas NDs forem liquidadas no sistema, os valores serão apresentados na aba "2 - Tributo".

[Baixa de títulos - FIN10060](https://tdn.totvs.com/pages/viewpage.action?pageId=555850211)
Baixa Escritural de títulos - FIN10115

Ao realizar a baixa de títulos com o pagamento de juros e multas, para títulos que possuem os novos tributos, o programa irá gravar os valores, realizando o rateio por Nota Fiscal de origem proporcional ao valor da Nota Fiscal, mesmo que não haja retenção dos impostos.
Ao realizar a inclusão de uma ND automática por juros em atraso, o programa irá gravar a previsão de juros para essa ND referente aos valores não recebidos.

[Exclusão de Baixas - FIN10061](https://tdn.totvs.com/pages/viewpage.action?pageId=327334266)

Ao realizar a exclusão de baixas que contenham Notas Fiscais de Débito Eletrônicas (Vendas) relacionadas, o sistema não irá bloquear, ou seja, será permitido realizar o estorno de liquidações de títulos que foram baixados **com multa e juros** , e que geraram nota de débito. Porém, ao identificar essa condição, será apresentada a seguinte mensagem: "Movimento gerou Nota Fiscal de Débito de multa e juros. Providenciar o cancelamento para desfazer os efeitos fiscais da mesma. NFs: ", indicando o número dasNotas Fiscais de Débito Eletrônicas.

Ao realizar a exclusão, esta ficará disponível na consulta **FIN10210 - Controle de Multa e Juros** como um movimento a ser estornado, destacado em vermelho, enquanto a Nota Fiscal de Débito não tiver sido cancelada.

[Geração Automática de Débitos - FIN10034](https://tdn.totvs.com/pages/viewpage.action?pageId=329029919)

Devido à nova demanda com relação à nova legislação, para títulos com os novos tributos, ao realizar a geração automática de débitos, não será possível realizar o controle de suspensão. Será gerada **uma ND para cada título** com pendência de juros.
**Observação** : Quando existir mais de uma Nota Fiscal de origem para a Duplicata com pendência de juros, o valor dos juros e multa será calculado proporcionalmente para cada NF na ND gerada.

FIN10300 – Renegociação de títulos

Não será permitido renegociar títulos com os novos tributos IBS, CBS e IS. Também não será permitido agrupá-los com títulos que não possuam os novos tributos.

[Controle de Multa e Juros e Geração de Nota Fiscal de Débito - FIN10210](https://tdn.totvs.com/pages/viewpage.action?pageId=1114988858)

Criado programa de consulta e geração de Notas Fiscais de Débito, onde a busca poderá ser realizada através dos seguintes filtros:

- Empresa
- Cliente
- Raiz de CNPJ
- Portador
- Emitidos de/até
- Pagos de/até
- Vencimento de/até
- Listar somente pendentes de geração (Selecionar somente multas e juros que não tem NF Débito gerada ainda)
- Listar notas de débito baixadas (Selecionar Notas de Débitos emitidas no Financeiro)
- Listar movimentos estornados (Selecionar baixas que foram excluídas e deverão ter a NF Débito cancelada no módulo de Vendas)

Como resultado serão mostradas as seguintes informações:

Grid principal:Selecionar?, Empresa, Documento, Tipo, Sequência, Cliente, Emissão, Pagamento, Exclusão, Multa, NF Débito, Juros, Nota Fiscal de Débito, CBS, IBS MUN, IBS UF, Situação NF Débito, Estornado (Sim, Não), Erro

- Rodapé - Dados da NF de origem: Empresa (NF), Nota Fiscal, Série, Sub-série, Tipo e Chave de acesso. Cancelamento da Nota Fiscal de Débito: data, hora e usuário de cancelamento.

**Importante** : Ao exibir os estornos, e se em algum deles a Nota Fiscal ainda não tenha sido cancelada, esta linha será exibida em destaque vermelho. Esse destaque alerta que a Nota de Débito correspondente precisa ser cancelada manualmente no VDP0753. Uma vez que a Nota de Débito tenha sido cancelada, o destaque deixa de ser exibido, pois a pendência já foi resolvida. Os valores de CBS, IBS MUN, IBS UF estão relacionados à Nota Fiscal de Débito gerada, então eles só terão valores se a NF tiver sido gerada.

Ao acessar o botão **"Gerar Notas"** o programa irá gerar as Notas Fiscais de Débito no módulo de Vendas, e, após gerá-las, as informações deNota Fiscal de Débito, CBS, IBS MUN, IBS UF, Situação NF Débito serão atualizadas. Caso ocorra algum erro que impeça a geração da Nota Fiscal de Débito, essa informação será apresentada na coluna "Erro". Após o problema ser corrigido, as Notas Fiscais de Débito poderão ser geradas novamente.

## Pacote 21/09/2026

ECONF - Estado de Goiás

O Governo do Estado de Goiás publicou através da instrução normativa nº 1.608/2025-GSE, tornando obrigatória a vinculação entre transações realizadas por meio de pagamento eletrônico à emissão do documento fiscal eletrônico correspondente nas operações sujeitas ao ICMS (NF-e Modelo 55 e NFC-e modelo 65).

**O que é a vinculação dos meios de pagamentos?**

Se o pagamento for realizado após a emissão do documento fiscal, a norma exige que o contribuinte utilize o Evento de Conciliação Financeira – ECONF, conforme estabelecido na Nota Técnica 2024.002.

A legislação exige a **vinculação direta** entre o sistema de pagamento eletrônico e o emissor do documento fiscal (NF-e/NFC-e).

**Solução:**

Esta atualização libera ajustes realizados em funções de busca e validação de informações relacionadas ao evento de Conciliação Financeira ECONF - 110750.

A parametrização desse evento acontece através do Módulo Fiscal, consultar o [Guia do Usuário: OBF26000 - Cockpit Eventos](https://tdn.totvs.com/pages/viewpage.action?pageId=1015569222) que contém as informações necessárias para a configuração dos eventos.

A geração deste evento ocorrerá de maneira manual, através do programa **OBF26300 - Inclusão de eventos** . Onde será gerado um evento para cada baixa relacionada a Nota Fiscal informada.

A consulta e/ou cancelamento de algum desses eventos deverá ser realizada através do programa **OBF26200 - Central de Eventos** .

Ao acessar a lupa, serão apresentados mais detalhes:

Automatização de Eventos

Os títulos renegociados também são considerados na geração automática do evento **112110 - Informação do efetivo pagamento integral para liberar crédito presumido do adquirente** .

Multa e Juros

**Carga de movimentos de Multa e Juros**

O conversor de carga foi criado para que seja possível preparar os títulos emitidos a partir de 01/01/2026, com IBS MUN, IBS UF ou CBS, para a geração de Notas Fiscais de Débito para o Módulo de Vendas, referentes aos valores de multa e juros pagos pelos clientes. Para isso, será necessário processar o conversor **FIN00043 - Atualização de valores de multa e juros - IBS, CBS** , que fica disponível através do programa **FRM0000 - Programas conversores** .

Ao processar, a seguinte tela será apresentada:

A opção **Prévia** gerará uma listagem em Excel para conferência e a opção **Oficial** gerará os registros de Multa e Juros Recebidos que serão apresentados no **FIN10210 - Controle de Multa e Juros** .

Após o processamento:

- Será gerada a previsão de impostos de Multa e Juros para movimentos já existentes na base de dados
- Será gerado o valor de multas e juros relacionados as Notas Fiscais de origem (Consultar os valores gerados na aba "Tributos" do FIN10209), para títulos que foram baixados com valor de juros e multa pagos, onde a duplicata possui os novos impostos. Essas baixas deverão passar a ser apresentadas na tela do FIN10210 para geração de Notas Fiscais de Débito para o módulo de Vendas.
- Também irá gerar a previsão de juros e multas nas NDs (Notas de Débito) geradas a partir de títulos com os novos tributos.
- **Importante** : Antes de processar esse conversor, é necessário que o **VDP10900 - Programa de ajuste de base** também tenha sido processado. Ao acessar a opção "Informar" no FIN00043, será apresentada uma mensagem de aviso orientando "Informamos que antes de processar esse ajuste de base, é importante que o conversor VDP10900 (Atualização do valor CBS/IBS) já tenha sido processado para o mesmo período."

## Pacote 12/10/2026

**FIN10300 - Renegociação de títulos**

Retirada a validação que impedia a renegociação de títulos com os novos tributos IBS, CBS e IS.

**OBF26300 - Inclusão manual de eventos**

**ECONF** : Realizamos uma correção, onde ao incluir um evento do ECONF o programa não trazia parcelas que já tinham um evento de cancelamento do evento. Se o evento de cancelamento estiver autorizado, o programa agora permite incluir um novo evento para a parcela, uma vez que o evento de cancelamento da mesma já foi estornado.
