# Reforma Tributária Logix — Entradas

Fonte: <https://tdn.totvs.com/pages/releaseview.action?pageId=948652302>

## 1. Visão Geral

A **Reforma Tributária** traz um cenário de mudanças significativas nas regras tributárias brasileiras, exigindo das empresas uma adaptação rápida e precisa para garantir conformidade e eficiência operacional.

## 2025

### Pacote 30/06

- **Cadastros principais -** Antes da inclusão dos tributos, alguns cadastros são necessários:

- No [SUP34260 - Cadastro da Classificação Tributária](https://tdn.totvs.com/pages/viewpage.action?pageId=923566687) é realizada a inclusão dos códigos e demais campos definidos no [Informe Técnico 2025.002 - v.1.00 - Publicado em 19/05/2025](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ph9Q7hYZ0QU=) . O mesmo pode ser importado conforme arquivo de importação: [cclassif_tributaria.txt](https://tdn.totvs.com/download/attachments/948652302/classif_trib.txt?version=2&modificationDate=1762862075960&api=v2)

- Já o [SUP20214 - Cadastro NBS(Norma Brasileira de Serviço)](https://tdn.totvs.com/pages/viewpage.action?pageId=925363730) é necessário para inclusão pelo SUP3760 de Notas Fiscais de Serviço, onde esse poderá ser informado no campo NCM dos itens. Os códigos podem ser importados pelo arquivo de importação: [nbs.txt](https://tdn.totvs.com/download/attachments/948652302/nbs.txt?version=1&modificationDate=1749064966703&api=v2)

- O cadastro de tributação/CST incluído pelos programas [VDP0440/VDP10061](https://tdn.totvs.com/pages/viewpage.action?pageId=926418235) também precisa existir antes da inclusão dos tributos pelo Configurador de tributos.

- **Fórmulas de entradas no Configurador de Tributos**

- No configurador de tributos VDP0696/VDP10068 é necessário clicar no botão Atualiza CRT, para que o código dos tributos e as fórmulas sejam criados no banco de dados.

- No vdp0692, os campos que vão definir a abrangência do impostos, precisam ser selecionados na aba Trib/benef entrada:

Observação: IBS_UF deverá ter como campos selecionados: Grupo despesa e Estado, entre outros...

IBS_MUN deverá ter como campos selecionados: Grupo despesa e Município entre outros...

- Ainda no vdp0692, os grupos de despesas precisam ser informados na aba Grupo despesa entrada:

- Voltando ao configurador fiscal VDP0696/VDP10068, os tributos precisam ser incluídos, com:

- Origem = Entrada,
- escolhendo a fórmula entre as opções sugeridas no zoom
- qual grupo de despesa que será aplicado e demais chaves se existir
- e informando a alíquota, taxa, incidência, classificação tributária e tributação(CST)

Observação: Caso alguma chave não seja informada, o tributo será criado para todo o grupo daquela chave(exceto exceções).

Tributos liberados nesse pacote:

| | [CBS](https://tdn.totvs.com/pages/viewpage.action?pageId=927561603) | [IBS_UF](https://tdn.totvs.com/pages/viewpage.action?pageId=927561603) | [IBS_MUN](https://tdn.totvs.com/pages/viewpage.action?pageId=927561603) |
| --- | --- | --- | --- |
| [Com redução de alíquota](https://tdn.totvs.com/pages/viewpage.action?pageId=927561603) | x | x | x |
| [C](https://tdn.totvs.com/pages/viewpage.action?pageId=929944870) [om diferimento](https://tdn.totvs.com/pages/viewpage.action?pageId=929944870) | x | x | x |
| [Monofásico(sobre quantidade)](https://tdn.totvs.com/pages/viewpage.action?pageId=929949728) | x | x | x |
| Crédito presumido | | | |
| Tributação Regular | | | |

*Redução de alíquota - conforme benefício, é um percentual(exemplo 30%) de redução na alíquota do imposto;

*Com diferimento - postergação ou adiantamento do impostos, onde é informando um percentual, que pode ser DIFERIMENTO TOTAL = 100% (incidência = 5(diferido)), ou PARCIAL, menor que 100% (incidência =1(tributado));

*Tributação Monofásica - para alguns produtos(exemplo combustível) é antecipada a obrigação do tributo.

- **Sup3760 - Nota de Entrada**

- Na inclusão de uma nota de entrada pelo SUP3760, será incluído o grupo de despesa buscando do cadastro do item(Man10021, aba comercial, campo Serviço do município), e o mesmo pode ser alterado no menu inf_compl_item.

- O valor calculado do tributo será gerado consistência da nota de entrada, considerando o grupo de despesa juntamente com as demais chaves, na busca da configuração fiscal;
- O valor declarado do tributo poderá ser informado manualmente no menu Q-impostos, A-tributos (SUP34120).

Observação:

- para que esse menu A-tributos seja apresentado, o parâmetro data_inicio_ref_trib no log00086, precisa ter uma data menor ou igual a data da emissão da nota de entrada.
- A tela SUP34120 só poderá ser acessada pelo menu A-tributos em 64bits. Em 32bits essa tela precisa ser chamada do menu principal.
- somente os valores declarados podem ser alterados, mas não precisam estar preenchidos.
- se os valores declarados foram informados, estes serão considerados em Obrigação Fiscal e no Contas a Pagar.
- se os valores declarados não forem informados, serão considerados os valores calculados em Obrigação Fiscal e no Contas a Pagar.

- As notas de serviço, consideram como fato gerador, a cidade que foi executado o serviço, então, no menu inf_compl_nf, foi incluído o campo [Cidade Tributação](https://tdn.totvs.com/pages/viewpage.action?pageId=928951776) , que será considerado no cálculo dos tributos;

Ainda no SUP3760, menu Y-tot_nf_calc, foi alterado para mostrar os totais dos tributos:

- **SUP8720 - Nota fiscal de Serviço**

- A consistência da nota de serviço com contrato incluída pelo SUP8720 foi alterada para calcular todos os impostos e tributos que o SUP3760 calcula. Então, conforme grupo de despesa informado/alterado no menu inf_compl_item teremos:
- O valor calculado do tributo que será gerado consistência da nota, considerando o grupo de despesa juntamente com as demais chaves, na busca da configuração fiscal;
- O valor declarado do tributo poderá ser informado manualmente no menu Q-imposto_renda, A-tributos (SUP34120);
- As notas de serviço, consideram como fato gerador, a cidade que foi executado o serviço, então, no menu 7-inf_compl_nf, foi incluído o campo [Cidade Tributação](https://tdn.totvs.com/pages/viewpage.action?pageId=928951776) , que será considerado no cálculo dos tributos;
Observação:

- para que esse menu A-tributos seja apresentado, o parâmetro data_inicio_ref_trib no log00086, precisa ter uma data menor ou igual a data da emissão da nota de entrada.
- A tela SUP34120 só poderá ser acessada pelo menu A-tributos em 64bits. Em 32bits essa tela precisa ser chamada do menu principal.
- somente os valores declarados podem ser alterados, mas não precisam estar preenchidos.
- se os valores declarados foram informados, estes serão considerados em Obrigação Fiscal e no Contas a Pagar.
- se os valores declarados não forem informados, serão considerados os valores calculados em Obrigação Fiscal e no Contas a Pagar.

- **Sup0580 - Nota fiscal de Frete**

- Na inclusão de uma nota de frete pelo SUP0580, será possível incluir manualmente os valores declarados dos tributos, acessando o menu Q-impostos, A-tributos(SUP34217).

(O cálculo dos valores pelo configurador de tributos será liberado em um próximo pacote).

Observação:

- para que esse menu A-tributos seja apresentado, o parâmetro data_inicio_ref_trib no log00086, precisa ter uma data menor ou igual a data da emissão da nota de frete.
- A tela SUP34217 só poderá ser acessada pelo menu A-tributos em 64bits. Em 32bits essa tela precisa ser chamada do menu principal.

- **Devoluções e Transferência entre empresas**

- Para as notas de devolução ou notas de transferência entre empresas, incluídas pelo SUP3760 ou automaticamente pelo módulo de Faturamento, e relacionadas com notas de saída que possuam os tributos CBS, IBS_UF e IBS_MUN. Estes serão carregados automaticamente e proporcionalmente(em caso de devolução parcial) no menu Q-impostos A-Tributos(SUP34120) como os valores calculados.
- Caso na consistência da nota, o cliente deseje recalcular os impostos, os mesmos serão substituídos pelos impostos calculados com base no configurador de tributos.

- **Histórico**

- Os programas de envio de histórico (SUP2510) e recuperação de histórico (SUP1052 e SUP34071) foram alterados para considerar os campos incluídos e as novas tabelas. As alterações foram realizadas no envio/recuperação de histórico, e no envio/recuperação do histórico do histórico.

[Demonstração de como parametrizar em vídeo](https://youtu.be/3NVdCx3sHdA?si=w8L-ZTS3tnmAIWho)

### Pacote 11/08

- **Tributação Regular -** Quando houver tributação diferenciada, deverá ser informada qual seria a tributação regular aplicada.

Conforme configuração fiscal(VDP0696/VDP10068) de entradas:

Ao preencher os campos de Código Classificação Tributária Regular e Tributação Regular,

na consistência da nota de entrada será criado os tributos: CBS e o CBS_REG, que podem ser consultados no SUP3760/SUP8720 - Nota Fiscal, menu Q-impostos, A-tributos(SUP34120):

Observação: Para os tributos: IBS_MUN e IBS_UF, a Tributação Regular tem o mesmo conceito descrito acima.

- **Sup0580 - Conhecimento de Frete e SUP9220 - Frete de Transportador Autônomo**

- Foram alterados para na consistência do frete, incluir o valor calculado conforme o configurador de tributos, podendo ser consultado no SUP34217;

- Foram alterados para na consistência do frete, fazer o rateio dos impostos para as notas de entrada relacionadas,

podendo ser consultado pela tela acima(SUP34217) no botão "Consultar Impostos", ou diretamente no SUP34216.

- **SUP34204 - Monitor de recebimento xml**

- Foi alterado para receber os tributos:

- CBS(com redução, com diferimento e monofásico),
- IBS_UF(com redução, com diferimento e monofásico),
- IBS_MUN(com redução, com diferimento e monofásico)

das NFes(Notas eletrônicas), CTes(Conhecimento de transporte eletrônico) e CTe-os(Conhecimento de transporte eletrônico Outros serviços) conformeNT2025.002 v1.10 e CTe_NT2025.001 v1.05b.

Então, se o xml conter as tags:

Ao importar o mesmo pelo sup34204, a nota será incluída no SUP3760-Nota de entrada ou SUP0580-Conhecimento de Frete,

e os tributos serão incluídos no SUP34120 ou SUP34217, que pode ser acessado pelo menu Q-impostos, A-tributos.

- **Sup0552 - Importação de nota/frete por arquivo texto**

- Foi alterado para receber os tributos:

- CBS(com redução, com diferimento e monofásico),
- IBS_UF(com redução, com diferimento e monofásico),
- IBS_MUN(com redução, com diferimento e monofásico)

que serão incluídos na linha "O" para notas de entrada, conforme exemplo abaixo:

e na linha "P" para os fretes, conforme exemplo abaixo:

E o layout do arquivo xml pode ser acessado:

- [Layout SUP0552.xls](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/23561569368215)

Ao importar o mesmo pelo sup0552, a nota será incluída no SUP3760-Nota de entrada, e os tributos serão incluídos no SUP34120, que pode ser acessado pelo menu Q-impostos, A-tributos.

Já o frete será incluído no sup0580- Fretes, e os tributos serão incluído no SUP34217, que pode ser acessado pelo menu Q-impostos, A-tributos.

- **OBF40000 - Painel da NF-e**

- Foi alterado a geração do xml para notas de devolução ou notas de emissão própria com o tipo "6", para impressão dos grupos dos tributos:

- CBS(com redução, com diferimento, tributação regularizada e monofásico),
- IBS_UF(com redução, com diferimento, tributação regularizada e monofásico),
- IBS_MUN(com redução, com diferimento, tributação regularizada e monofásico)

Para devolução, será impresso também o grupo de Nota referenciada.

- **SUP34032 - Relatório de Movimentação diária de Nota Fiscal e Frete**

- Alterado o relatório para mostrar os tributos CBS, IBS_UF e IBS_MUN:

- **SUP4410/SUP34041 - Rastreabilidade de Notas Fiscais**

- Alterado o relatório para mostrar os tributos CBS, IBS_UF e IBS_MUN quando o campo "Emitir detalhe nota" for selecionado:

### Pacote 22/09

- **Crédito Presumido -** Conforme NT 2025.002 v1.20, para o crédito presumido existe uma tabela específica de códigos ( [cCredPres](https://dfe-portal.svrs.rs.gov.br/DFE/TabelaCreditoPresumido) ), que define os percentuais, vigência, critérios de aplicação e vinculação para esse tributo.

- Foi criado o cadastro **OBF25200** onde pode ser incluído/importado as informações referentes aos códigos de **crédito presumido:**

(deverá ser executado no log6000 o conversor de criação de tabela **OBF00660.cnv** ).

- Foi alterado o configurador fiscal( **vdp0696/vdp10068** ) para buscar os códigos da tabela acima quando os tributos forem: CBS_CR_PRE e IBS_CR_PRE:

- Foi alterado a consistência nos programas **SUP3760-** Entrada de nota fiscal, **SUP8720** **-** Nota fiscal de serviço com contrato, **SUP0580** - Entrada de Fretes e **SUP9220** - Frete de Transportador Autônomo,

para calcular os tributos de CBS_CR_PRE/IBS_CR_PRE quando o grupo de despesa do item/ou respectiva chave informada no configurador.

Os mesmos podem ser consultados no menu Q-impostos, A-tributos de cada tela. (SUP34120- Tributos da nota e SUP34217- Tributos do frete).

- Foi alterado o **OBF40000 - Emissão de nota** , para que os grupos gIBSCredPres e gCBSCredPres sejam gerados corretamente no xml:

- Foi alterado o **SUP34204 - Monitor de Recepção xml** , para importar os xmls referente aos documentos abaixo, com as respectivas informações dos tributos CBS_CR_PRE e IBS_CR_PRE:

- nfe(nota fiscal eletrônica),
- cte(conhecimento de transporte eletrônico),
- cte-os(conhecimento de transporte outros serviços) e
- cte-simplificado

Incluindo a nota no SUP3760 - Entrada de notas ou o frete no SUP0580- Inclusão de Fretes, onde os tributos poderão ser consultados no menu Q-impostos, A-tributos de cada tela. (SUP34120- Tributos da nota e SUP34217- Tributos do frete).

- Foi alterado o **SUP0552** - **Importação de nota e frete via arquivo texto** , para que as linhas referentes aos tributos (linha O - tributos da nota e linha P- tributos do frete), no campo 13, caso os valores sejam:
7-> CBS_CR_PRE

8-> IBS_CR_PRE

Inclua os tributos de Crédito presumido do CBS e Crédito presumido do IBS, ao incluir a nota no SUP3760 - Entrada de notas ou o frete no SUP0580- Inclusão de Fretes.
Sejam Para maiores informações, deverá ser consultado o [arquivo](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/34135122677271) com a definição dos campos de importação.

**Observação: Essa é a primeira liberação referente ao Crédito Presumido.**

**Será realizado uma segunda liberação, prevendo os demais cenários.**

### Pacote 03/11

- **Nota de débito e crédito -** Conforme NT 2025.002 v1.30, poderá ser incluído notas de débito e crédito.

Notas de Débito e Crédito são nomes de instrumentos utilizados mundialmente para documentar situações contábeis onde é necessário corrigir informações comerciais que foram registradas em um documento, que no Brasil é a Nota Fiscal. Esta Nota Técnica cria na NF-e modelo 55 as finalidades de emissões correspondentes.

O sentido das palavras “débito” e “crédito” sempre se referem ao ponto de vista do emissor:
• Uma nota de débito documenta uma situação na qual o emitente registra um aumento no imposto devido (consequentemente, uma redução no imposto devido pelo adquirente, que é o destinatário);
• Uma nota de crédito documenta uma situação na qual o emitente registra uma redução no imposto devido (consequentemente, um aumento no imposto devido pelo adquirente, que é o destinatário);

- Foi alterado o **SUP3760** para inclusão das notas de débito e crédito como NFC(nota fiscal complementar), onde na saída do campo espécie, poderá ser selecionada a classificação:

E o tipo de nota:

Após saída da tela de classificação da Nota Fiscal, será mostrado na tela principal o tipo de nota escolhido:

Conforme as opções apresentadas na NT:

As notas de débito e crédito, com exceção das notas de débito 06-Antecipação de Pagamento e 07- Perda de estoque, possuirão quantidade e valores zerados.

Precisando informar os tributos a que se referente, no menu Q-impostos, A-tributos:

E o relacionamento com a nota de origem, no menu >_nota_origem:

Observação: Para essa alteração foi necessário alterar a tabela "sup_nf_origem", incluindo campo de sequencia da nota de origem(num_seq_origem).

Portanto, é necessário rodar o conversor de tabela sup02131.cnv pelo log6000 e os xmls das tabelas: sup_nf_origem.xml, sup_nf_origem_hist.xml e sup_nf_origem_hist_hist.xml pelo log00074.

**Importante:** Essa alteração impacta nas NFC de valor, onde, se for informado a sequência do AR ao qual a nota de origem se refere,

no fechamento, não será mais rateado todos os itens da NFC para as notas de origem informadas.

Caso seja informado sequencia de AR = 0(zero), o funcionamento será igual ao anterior, rateando os valores.

- Consistência da nota de entrada foi alterada para alertar se não tiver nota de origem relacionada, ou não for informado os tributos declarados.
- Notas de débito e crédito não podem possuir outros tributos como ICMS, IPI, PIS...

- Notas de débito de antecipação de pagamento

Essas notas podem ter quantidade e valor diferente de zero, mas não geram movimentação de estoque.

E não precisam ter o relacionamento da nota de origem no primeiro momento.

- Foi alterado o **OBF40000 - Painel da NF eletrônica,** para geração das notas de emissão própria, somente de crédito. (Notas de débito são emitidas pelo faturamento)

Com geração do grupo DFeReferenciado com a nota de origem:

- Alteramos o **SUP34204- Monitor de recebimento de xml,** para receber NF de débito e respectivas notas de origem informadas no grupo DFeReferenciado,

incluindo na tabela sup_nf_origem que pode ser consultado no SUP3760 - Entrada de Nota Fiscal, menu >_nota_origem.

Observação: Notas de débito de antecipação de pagamento são incluídas no grupo **gPagAntecipado** , previsto em um próximo pacote.

- Foi alterado o **SUP0552 - Importação de notas via arquivo texto** , para receber as NF de débito e respectivas notas de origem

Na linha M(nota) - campo 26 informar a finalidade =6(nota de débito), e no campo 33 o tipo de nota (exemplo: 06, pagamento antecipado) ;

Na linha D(item) - campo 41 - chave da nota de origem, e no campo 44 - a sequencia do item da nota de origem.

- Notas de devolução - Nas devoluções de emissão com nota de emissão própria, a nota de origem poderá ser impressa em um dos grupos abaixo:

- DFeReferenciado - quando existir somente uma nota relacionada
- NFref - quando existir mais de uma nota relacionada.

No SUP3760 - Entrada de Nota fiscal, menu V_nf_vendas, para as notas de emissão própria, relacionadas a somente uma nota, será realizado a pergunta: Deseja imprimir como documento referenciado?,

se sim - imprime no DFeReferenciado,

para os demais casos - imprime no NFref

- Indicador de Bem Móvel Usado

Foi alterado o **SUP3760 - Entrada de Nota Fiscal,** menu info_compl_item, menu 1_prox_tela, incluindo o campo Bem Móvel:

Esse campo só poderá ser assinalado caso o fornecedor seja pessoa física ou MEI(microempreendedor), e será impresso em nota de emissão própria, conforme alteração no **OBF40000 - Painel da NF eletrônica.**

**Observação:**

**1- Essas alterações serão liberadas dia 17/11 para a release 12.1.2511**

**2- Essa alteração impacta no módulo de importação, necessário atualizar IMP0133 na versão 63.**

### Pacote 17/11

- **Classificação fiscal tributária -** Conforme NT 2025.002 v1.30, foram incluídos novos campos e atualizado o arquivo de importação [classif_trib.txt](https://tdn.totvs.com/download/attachments/948652302/classif_trib.txt?version=2&modificationDate=1762862075960&api=v2) com os novos códigos .

Necessário rodar o conversor de tabela: sup02135.cnv pelo log6000 e

xmls: classif_tributaria.xml, sup34260.xml e sup342602.xml pelo log00074.

- **Nota de entrada com antecipações de pagamento**

Foi alterado o **SUP3760** para que na entrada da nota, possa ser relacionado com as antecipações de pagamento(notas fiscais complementares de débito do tipo 6), que foram realizadas antes da entrega do produto:

Podendo ser informado pela chave eletrônica da nota ou pelo número da nota:

Observação: Após inclusão na tela acima, e ao consultar a NFC de antecipação de pagamento(no exemplo acima 1753), no menu >_nota_origem existirá a nota de entrada 1754.

- Foi alterado o **SUP34204- Monitor xml,** para importar o grupo de antecipação de pagamento e incluir no SUP3760 - menu <_antecipação, conforme acima

- Foi alterado o **SUP0552- Importação de arquivo texto,** para importar ao importar as notas, importar também as notas de antecipação de pagamento relacionadas, e incluir no SUP3760 - menu <_antecipação:

Conforme coluna "A" e campo 40, onde deverá ser informado a chave eletrônica da nota fiscal de antecipação.

O arquivo texto poderá ter várias linhas "A", ou seja, várias notas de antecipação de pagamento.

- Foi criado um relatório **SUP34340- Relatório de Pagamento Antecipado,** para acompanhamento das notas e respectivas antecipações, ou das antecipações que não tiveram recebimento:

Necessário rodar o xml sup34340.xml pelo log00074.

- O campo tipo de Nota Fiscal se refere ao filtro dos demais campos. Caso seja informado NF Pagto Antecipado, serão filtradas(data, nota, série....) apenas notas NFC de débito com tipo 6.

Ao desmarcar o campo "Só imprime NF de Pagto Antecipado sem NF entrada?", apresenta as notas de entrada com respectivas notas de antecipação:

- **Redução de Base**

Conforme o CST 222, e classificação tributária 222001, é necessário a redução de base:

Foi alterado o configurador fiscal **vdp0696/vdp10068,** para poder informar a redução de base nas fórmulas de entradas: 701(redução de alíquota) e 702(com diferimento):

Necessário rodar o botão Atualiza CTR para que o campo possa ser mostrado.

- Foi alterado o **SUP3760/SUP8720** - Entrada de notas fiscais, menu Q-impostos, A-tributos para mostrar novos campos:

- Foi alterado o **SUP0580** - Entrada de fretes, menu Q-impostos, A-tributos para mostrar novos campos:

Necessário rodar o conversor de tabela: sup02134.cnv pelo log6000 e

xmls: sup_ar_item_fisc.xml, sup_frete_fisc.xml, sup_frete_item_fisc.xml, sup34120.xml, sup34217.xml e sup34216.xml pelo log00074.

- Foi alterado os programas de envio de histórico( **SUP2510** ) e retorno de histórico( **SUP1052** e **SUP34071** ) para considerar os novos campos nas tabelas de histórico e histórico do histórico.

Necessário rodar o conversor de tabela: sup02134.cnv pelo log6000

- **Eventos**

Conforme NT 2025.002 versão 1.30, foram liberadas as telas do OBF onde será possível cadastrar os eventos do Recebimento, onde o autor é a empresa destinatária:

Necessário cadastrar os eventos acima no **OBF26100- Cadastro de Eventos** com data valida e origem Suprimentos:

Depois, pode ser incluído a nota e seu evento correspondente no **OBF26300- Inclusão de eventos**

Importante: Para a inclusão dos eventos acima, a nota de entrada precisa estar sem erros, ou com os erros assumidos, ser do modelo 55(SUP3760/SUP8720 menu 7_inf_compl_nf)

Precisa possuir chave eletrônica, informada no SUP3760/SUP8720, menu 7_inf_compl_nf, menu nf_eletronica, ou a nota precisa ter sido emitida no OBF40000 - Painel NF-e.

Detalhamento dos eventos:

Evento 112120 - Importação em ALC/ZFM não convertida em isenção

**Função:** Permitir que o adquirente das regiões incentivadas (ALC/ZFM) informe que a tributação na importação não se converteu em isenção de um determinado item por não atender as condições da legislação.

**Validações na nota:** Nota de entrada com fornecedor estrangeiro, ou cfop de importação 7.xxx

**Quantidade:** Nesse evento, pode-se modificar a unidade de medida e a quantidade do item, podendo ser informado na unidade de medida do estoque.

A quantidade/unidade de medida informada será validada conforme fator de conversão do cadastrado SUP7750, e não pode ultrapassar a quantidade da nota de entrada.

Ao salvar o evento, a quantidade informada será convertida/enviado na unidade de medida da nota de entrada e os tributos serão calculados proporcionalmente a quantidade informada.

Evento 211110 - Solicitação de Apropriação de crédito presumido

**Função:** Evento a ser gerado pelo destinatário da NF-e em relação às notas fiscais de aquisição de emissão de terceiros e que lhe gerem o direito à apropriação de crédito presumido.

**Validações na nota:** Nota de entrada com crédito presumido (CBS_CR_PRE e IBS_CR_PRE) no menu Q-impostos, A-tributos.

Evento 211120 - Destinação de item para consumo pessoal

**Função:** Permitir ao adquirente informar quando uma aquisição for destinada para o consumo de pessoa física, hipótese em que não haverá direito à apropriação de crédito.

Evento a ser registrado após a emissão da nota de bens destinados para uso e consumo pessoal(nota de saída).

**Informações:** Nesse evento poderá ser utilizado o zoom na coluna NFE ref. onde deverá ser escolhida a nota de saída de consumo do item.

A nota de saída informada precisa ter o mesmo item, e quantidade informada.

**Quantidade:** Nesse evento, pode-se modificar a unidade de medida e a quantidade do item, podendo ser informado na unidade de medida do estoque.

A quantidade/unidade de medida informada será validada conforme fator de conversão do cadastrado SUP7750, e não pode ultrapassar a quantidade da nota de entrada.

Ao salvar o evento, a quantidade informada será convertida/enviado na unidade de medida da nota de entrada e os tributos serão calculados proporcionalmente a quantidade informada.

Evento 211124 - Perecimento, perda, roubo ou furto durante o transporte contratado pelo adquirente

**Função:** Permitir ao adquirente informar quando uma aquisição for objeto de roubo, perda, furto ou perecimento. O evento está relacionado aos bens que foram objeto de perecimento, perda, roubo ou furto em trânsito, em fornecimentos com frete FOB.

**Validações na nota:** Nota de entrada com frete à pagar.

**Quantidade:** Nesse evento, pode-se modificar a unidade de medida e a quantidade do item, podendo ser informado na unidade de medida do estoque.

A quantidade/unidade de medida informada será validada conforme fator de conversão do cadastrado SUP7750, e não pode ultrapassar a quantidade da nota de entrada.

Ao salvar o evento, a quantidade informada será convertida/enviado na unidade de medida da nota de entrada e os tributos serão calculados proporcionalmente a quantidade informada.

Evento 211140 - Solicitação de Apropriação de Crédito de Combustível

**Função:** Evento a ser gerado pelo adquirente de combustível listado no art. 172 da LC 214/2025 e que pertença à cadeia produtiva desses combustíveis, para solicitar a apropriação de crédito referente à parcela que for consumida em sua atividade comercial.

**Quantidade:** Nesse evento, pode-se modificar a unidade de medida e a quantidade do item, podendo ser informado na unidade de medida do estoque.

A quantidade/unidade de medida informada será validada conforme fator de conversão do cadastrado SUP7750, e não pode ultrapassar a quantidade da nota de entrada.

Ao salvar o evento, a quantidade informada será convertida/enviado na unidade de medida da nota de entrada e os tributos serão calculados proporcionalmente a quantidade informada.

Evento 211150 - Solicitação de Apropriação de Crédito para bens e serviços que dependem de atividade do adquirente

**Função:** Evento a ser gerado pelo adquirente para apropriação de crédito de bens e serviços que dependam da sua atividade

**Observação:** **Impacto no módulo de importação, necessário atualizar IMP0133 na versão 63.**

### Pacote 08/12

- **Devolução e Nota de Retorno**

- Alterado a devolução(NFD ou cfop de devolução) e retorno(NFR) relacionadas as notas de saída anteriores ao parâmetro de Data de Início da Reforma Tributária, para não calcular os tributos conforme configurado

- **PIS/Cofins**

- Alterado a devolução para diminuir da base dos tributos, o PIS/Cofins da nota de saída;
- Alterado a nota de entrada, quando o item não tem crédito de PIS/Cofins(MAN10021-Cadastro de item, aba fiscal), mas a nota possui PIS/Cofins. Para calcular conforme SUP1082- Alíquota de PIS/Cofins por classificação fiscal/item, diminuindo da base dos tributos.

- **Grupos da NT 2025.002 v1.32**

- Grupo **gTransfCred -** Transferência de crédito do associado, inclusive as cooperativas singulares.

Utilizado para Notas de débito com tipo 01=Transferência de créditos para Cooperativas ou tipo 05=Transferência de crédito na sucessão; Ou Nota de crédito com o tipo 05=Transferência de crédito na sucessão;

Foi alterado SUP34204 - Monitor de importação via xml, para importar as informações desse grupo;

Foi alterado OBF40000 - Painel da NF eletrônica, para geração do xml com esse grupo, conforme CST escolhido.

- Grupo **gAjusteCompet** e campo Período de Competência - Ajuste de Competência será preenchido conforme tabela de CST que possui o indicador. Hoje, é referente ao CST 811- Ajustes, que possui as seguintes classificações tributárias:

811001 - Anulação de Crédito por Saídas Imunes/Isentas

811002 - Débitos de notas fiscais não processadas na apuração

811003 - Desenquadramento do Simples Nacional

Foi alterado SUP34204 - Monitor de importação via xml, para importar as informações desse grupo;

Foi alterado SUP3760/SUP8720 - Entrada de notas fiscais, menu Inf_compl_item, 1-prox_tela, para que possa ser informado o campo Período de Competência.

Foi alterado SUP0552 - Importação de nota via arquivo texto para importar o campo Período de Competência. Já os tributos devem ser informados na linha "O" como os demais tributos.

- Grupo **gEstornoCred** e campo Doação - Grupo de Estorno de Crédito será preenchido conforme tabela de CST que possui o indicador. Hoje, é referente ao CST 410 - Imunidade e não incidência, que possui as seguintes classificações tributárias:

410026 - Doação com anulação de crédito

410030 - Estorno de crédito por perecimento, deterioração, roubo, furto ou extravio.

Foi alterado SUP34204 - Monitor de importação via xml, para importar as informações desse grupo;

Foi alterado SUP3760/SUP8720 - Entrada de notas fiscais, menu Inf_compl_item, 1-prox_tela, para que possa ser informado o campo Doação.

Foi alterado SUP0580 - Fretes, menu Info_compl, menu prox_tela_1, para que possa ser informado o campo Doação.

Foi alterado SUP0552 - Importação de nota e fretes via arquivo texto para importar o campo Doação. Já os tributos devem ser informados nas linhas "O"(notas) e "P"(fretes) como os demais tributos.

- Campo Data de Previsão de Entrega - Data de previsão de entrega ou disponibilização do item, que não poderá ultrapassar 3 meses, e poderá ser alterada via evento.

Foi alterado SUP34204 - Monitor de importação via xml, para importar o campo de Data de Previsão de Entrega;

Foi alterado SUP3760/SUP8720 - Entrada de notas fiscais, menu 7-inf_compl_nf, 2-tela_2, para que possa ser informado o campo Data de Previsão de Entrega.

Foi alterado SUP0552 - Importação de nota via arquivo texto para importar o campo Data de Previsão de Entrega.

## 2026

### Pacote 12/01

- **OBF40000 - Emissão da NFe**

- Notas de entrada que não geraram IBS_MUN, e consequentemente, apresentam rejeição. Alterado para inicializar esse tributo com valores zero, quando os mesmos não existirem. Poderá ser executado o programa de acerto para as notas que não possuem o IBS_MUN, pelo FIN0000, opção "suca0004 - Insere IBS_MUN para emissão de nota de devolução";

- **Devolução(NFD ou cfop de devolução)**

- Alterado para considerar notas de cupom fiscal (NFCe modelo 65 importadas pelo Vendas) com o tipo FATNFCE, no relacionamento pelo menu V-nf_vendas;
- Alterado para diminuir o ICMS ST da base de cálculo de CBS e IBS, quando no SUP0650 - Alíquotas ICMS, tela_2, Somar ICMS ST retido no total da Nota? = S .

- **NF de débito e crédito no OBF12000 - Livros Fiscais**

- Após manutenção/modificação das notas de débito/crédito pelo SUP3760 - Entrada de Notas Fiscais, alguns dados permaneciam na base indevidamente, apresentando divergências na emissão do OBF12000- Livro Fiscal. Foi alterado o SUP3760 e criado programa de acerto SUCA2741 para correção dos dados na base.

- **SUP0552 - Importação de NF em arquivo texto**

- Alterado a importação de NF para importar a chave eletrônica da nota de entrada na linha "H" (informações complementares da nota), campo41 (compl_nota2) **;**
- Quando for importação de NFC de débito/crédito, poderá ser informada a nota de origem na linha "D" nos campos:
Numero da nota (posição 48 -grade_1), Série (posição 49 -grade_2), SubSerie (posição 50 - grade_3), Espécie (posição 51 -grade_4).

- **NBS (Norma Brasileira de Serviço)**

- Alterado o SUP3760 - Entrada de Nota Fiscal, SUP8720 - Entrada de Nota Fiscal com contrato de Serviço, para buscar o NBS do cadastro do item Man10021, do novo campo criado no menu Comercial, e conforme documentação disponibilizada pelo Vendas no [Guia de Uso - Reforma Tributária - Vendas#-1099585962](https://tdn.totvs.com/pages/viewpage.action?pageId=948652337#GuiadeUsoReformaTribut%C3%A1riaVendas--1099585962) , do dia 08/12.

- **NFCom (Nota Fiscal de Comunicação)**

- Incluido o campo "Tipo Faturamento NFCom" no SUP3760- Nota Fiscal de Entrada, menu 7-inf_compl_nf, 2-tela_2:

Que será utilizado pelo OBF nos livros fiscais. Caso o campo não seja informado, será considerado o valor 0- Faturamento Normal.

- **PIS/Cofins**

- Conforme pacote anterior, onde foi alterado a nota de entrada para quando o item não tem crédito de PIS/Cofins(MAN10021-Cadastro de item, aba fiscal), mas a nota possui PIS/Cofins. Para calcular conforme SUP1082- Alíquota de PIS/Cofins por classificação fiscal/item, diminuindo da base dos tributos. Nesse pacote, foi alterado para que possa ser consultado o valor calculado para o PIS/Cofins sem crédito, no SUP3760- Entrada de Notas Fiscais, menu Q-impostos, X-pis_cofins_sem_cred

- **Eventos**

Os eventos com autor igual a destinatário, conforme lista abaixo, já podem ser enviados via TC2:

| 211110 - Solicitação de Apropriação de crédito presumido |
| --- |
| 211120 - Destinação de item para consumo pessoal |
| 211124 - Perecimento, perda, roubo ou furto |
| 112120 - Importação em ALC/ZFM não convertida em isenção |
| 211140 - Solicitação de Apropriação de Crédito de Combustível |
| 211150 - Solicitação de Apropriação de Crédito para bens e serviços que dependem de atividade do adquirente |

### Pacote 23/02

- **CNPJ Alfanumérico**

- Foi alterado a validação do CNPJ e a validação da chave eletrônica da nota, para considerar corretamente os caracteres alfanumericos;

- **Integração Trade Easy na inclusão da nota**

- Conforme documentação da Trade Easy em 19/01/2026 - [Pacotes de Atualizações - Comércio Exterior#17](https://tdn.totvs.com/pages/viewpage.action?pageId=526987588#PacotesdeAtualiza%C3%A7%C3%B5esCom%C3%A9rcioExterior-17) , foi liberado pacote que envia para o Logix(via integração EAI) os valores de base, aliquota, valor e classificação tributária dos tributos CBS, IBS_UF e IBS_MUN. No Logix, a integração EAI que gera a nota de entrada, foi alterada para receber esses valores e incluir no SUP3760 - Nota Fiscal de Entrada, menu Q-imposto, A-tributos.

- **Tributação Regular com redução de alíquota**

- Foi alterado o configurador fiscal para que nas fórmulas de entradas, em informações adicionais, possa ser incluída a redução da alíquota da tributação regular. (Necessário processar o botão Atualiza CTR)

Essa redução poderá ser consultada no SUP3760 - Nota Fiscal de Entrada, menu Q-impostos, A-tributos, consultado o tributo CBS_REG ou IBS_UF_REG ou IBS_MUN_REG:

No xml, a alíquota é apresentada com a redução:

Foi alterado o frete incluído pelo SUP0580 - Entrada de Frete, para considerar a redução da tributação regular, podendo ser consultada no menu Q-impostos, A-tributos, informando os tributos CBS_REG ou IBS_UF_REG ou IBS_MUN_REG.

- **Base de CBS/IBS**

- Alterado para descontar pis/cofins da base do CBS/IBS do Frete Venda;
- Empresa de Lucro Presumido, alterado para descontar pis/cofins outros da base CBS/IBS;
- Nota de retorno(NFR), alterado para descontar o ICMS_UF_DEST(Imposto sobre Circulação de Mercadorias e Serviços partilha para Unidade Federativa Destino) da base do CBS/IBS.

- **OBF40000 - Emissão da nota**

- Alterado para tratar o CST 515 - Diferimento com redução de alíquota;

### Pacote 27/04

- **Tributação(declarada/calculada), Classificação Tributária(declarada/calculada) e Incidência(declarada/calculada)**

- Os campos: tributação, classificação tributária e incidência, das telas:

- SUP34120- Tributos das notas;
- SUP34217- Tributos do frete;
- SUP34216- Rateio dos Fretes

estavam sendo carregados conforme as informações do configurador de tributos(vdp0696/vdp10068), modificando as informações importadas pelo:

- SUP34204 - Monitor xml;
- SUP0552 - Importação por arquivo texto;
- Na devolução, as informações carregadas automaticamente da nota de saída ;
- Na transferência entre empresa, as informações carregadas automaticamente da nota de origem.

Para manter a rastreabilidade dos dados importados, criamos 3 novos campos nas tabelas de tributos(sup_ar_item_fisc, frete_sup_fisc e sup_frete_item_fisc): tributacao_calc, cod_classif_trib_calc e incidencia_calc, que serão carregados com as informações do configurador. Portanto, será necessário atualizar:

- As tabelas pelo log6000, rodando os conversores: sup02143.cnv, sup02144.cnv
- Os xmls pelo log00074: sup_ar_item_fisc.xml, h_sup_ar_item_fisc.xml, hh_sup_ar_item_fisc.xml, frete_sup_fisc.xml, h_frete_sup_fisc.xml, hh_frete_sup_fisc.xml, sup_frete_item_fisc.xml, h_sup_frete_item_fisc.xml, hh_sup_frete_item_fisc.xml, sup34120.xml, sup34216.xml e sup34217.xml.

- Observação:

- Para o correto funcionamento do sistema, após a alteração das tabelas, deverá ser executado o FIN00000, programas SUP35004 e SUP35005, para que os campos novos recebam os valores dos campos antigos, ou seja, tributacao_calc vai receber o valor do campo tributacao.
- Para empresas que utilizam o módulo de Importação, existiu a mesma alteração acima(favor consultar a documentação de importação: [Guia de Uso - Reforma Tributária - Importação](https://tdn.totvs.com/pages/viewpage.action?pageId=1009450061) ).

- **Ajuste SINIEF 49/25 e SINIEF 8/26,** que são referentes a algumas situações de notas de saída, que foram detalhadas abaixo:

- Quando for necessário a redução de valores ou quantidades, e não for possível realizar o cancelamento da Nota Fiscal eletrônica (NF-e de saída), então:

- o remetente da NF-e de saída original deve emitir **NF-e de entrada de crédito** (finNFe= 5) com tipo da nota de crédito(tpNFCredito) **“04=Redução de valores ou quantidades”** ;

- Quando existir retorno por recusa total na entrega, ou por não localização do destinatário, então:

- o remetente da NF-e de saída original deve emitir **NF-e de entrada de crédito** (finNFe= 5) para anulação total da operação de saída original com tipo da nota de crédito(tpNFCredito) **“03=Retorno por Recusa na Entrega ou Por Não Localização do Destinatário na Tentativa de Entrega”;**

- Quando existir o retorno por recusa parcial na entrega, então:

- o remetente da NF-e de saída original deve emitir **NF-e de entrada de crédito** (finNFe= 5) com tipo da nota de crédito(tpNFCredito) **“06=Retorno por Recusa Parcial na Entrega”.**

Portanto, para que essas notas possam "movimentar estoque", relacionar com "notas fiscais de faturamento" da empresa e "gerar notas de crédito", alteramos o SUP3760 - Inclusão da nota de entrada,

para que ao incluir uma NFC, com a classificação 5-Nota de crédito e tipo de nota: 3(Retorno por recusa), 4(Redução de valores ou qtde) ou 6(Retorno por recusa parcial)

será apresentado a mensagem: "Esse tipo de NF movimenta estoque, será considerada como NFD(devolução)"

Alterado a espécie de NFC para NFD, mas mantendo sua finalidade e tipo, conforme a descrição no cabeçalho da nota

- Para o tipo **“03=Retorno por Recusa na Entrega ou Por Não Localização do Destinatário na Tentativa de Entrega”,** os itens serão carregados automaticamente;
- Somente para essas notas de crédito, o relacionamento com a nota de faturamento origem deverá ser realizado pelo menu **V-nf_Vendas** , como já é feito para notas de devolução.
- A movimentação de estoque, caso seja necessária, irá utilizar as operações de estoque de devolução parametrizadas no **SUP7160 - Parâmetros para devolução de cliente** ;

- Para o tipo **“04=Redução de valores ou quantidades”,** foi criado um novo parâmetro, gerando operações de ajuste de valor(quando quantidade for zero). Quando a quantidade for maior que zero, irá utilizar as mesmas operações de estoque da devolução;

- A operação de estoque também pode ser informada diretamente no SUP3760, no campo Oper, quando a empresa utilizar o parâmetro do SUP1180- Padrões para Recebimento/Compras, no campo "Informa Oper.Estoq. no Recebimento" = S(sim);

- O OBF40000 foi alterado para gerar corretamente o xml conforme os tipos citados:

- Gerando os textos fixos na natureza de operação(natOp):

- Tipo 04 - texto = “Redução de valores ou quantidades"
- Tipo 03 - texto = “Retorno por Recusa ou não localização”
- Tipo 06 - texto = “Retorno por Recusa Parcial na Entrega”

- Para notas tipo **“04=Redução de valores ou quantidades”,** é necessário informar o motivo da redução de valores/quantidade para que seja apresentado na tag "infAdFisco". Para isso, precisa informar no SUP3760 - Entrada de Nota Fiscal, menu 9_compl_nfe, menu k_info_fisco.

- Observação:

- As notas do tipo **“06=Retorno por Recusa Parcial na Entrega”** ainda não estão sendo aprovadas pela Sefaz.

### Pacote 18/05

- **NF de Serviço**

- Devido aos vários tipos de Notas fiscais de serviço, e para conseguir diferenciá-los,

alteramos o SUP3760 - Entrada de Nota Fiscal, onde na inclusão da nota de entrada do tipo "NFS", poderá ser selecionado:

1- Nota fiscal de Serviço - notas fora do padrão nacional;

2- NFS-e Nacional - nota fiscal de serviço com xml no padrão nacional;

3- NFS-e Simplificada - nota fiscal de serviço simplificada;

4- NFS-e Via - nota fiscal de serviço de exploração de vias (pedágio);

5- NFS-e Locação - nota fiscal de serviço de locação de imóveis;

6- Outros, podendo ser:

- NFCom(nota fiscal eletrônica de serviço de comunicação),
- NFAg-e (Nota fiscal de água e serviço de saneamento)
- entre outros,

onde, possui um modelo de nota que os diferencia.

Essas notas precisam ser somente de serviço, caso tenham ICMS, precisarão ser lançadas como NF ou NFF.

Após inclusão da nota, essa informação poderá ser consultada no SUP3760 - Entrada de notas fiscais, menu 7_inf_compl_nf, menu nf_servico, campo Tipo da Nota:

Observação: Deverá ser rodado o programa fin00000, selecionando o programa = 'suca0005', onde irá substituir o campo antigo "nfsenac" - que identificava a nota de serviço nacional, pelo campo novo "tipo_nfs" - que identifica os vários tipos de nota de serviço, para que seja possível visualizar corretamente as notas anteriores.

- Também foi alterado no SUP3760 - Nota fiscal de entrada, menu 7_inf_compl_nf, menu nf_eletronica, os motivos de substituição da chave eletrônica de origem, que variam conforme cada tipo de NF.

Para isso, foi criado a tabela sup_par_nf_eletr e deverá ser rodado pelo log6000 o conversor de tabela: sup02148.cnv. Pelo log00074 o xml de tabela: sup_par_nf_eletr.xml

Também é necessário rodar o programa fin00000, selecionando o programa = 'suca0006', que atualizará os motivos de substituição na nova tabela.

- **NFS-e Via - Exploração de serviço de vias (pedágio)**

- Na inclusão desse tipo de nota pelo SUP3760 - Nota fiscal de entrada, alguns campos são fixos. O campo abaixo será preenchido automaticamente:

- Indicador de Operação = 80101 - Serviço de exploração de via

- Já o grupo de despesa utilizado para o item dessa nota, deverá estar no configurador de tributos(vdp0696/vdp10068) com os seguintes dados:

- CST = 000 - Tributação Integral
- Classificação tributária = 000002 - Exploração de Via

- No cadastro do item(MAN10021 - aba comercial), ou no item da nota no SUP3760, deverá ser utilizado o código NBS = 106042100

- Na consistência da nota de entrada, será validado se a chave eletrônica foi informada, caso não tenha sido, será apresentado consistência, grave ou não, conforme parametrização(log00086 - parametro = consiste_chave_acesso_nf_entr). Essa consistência também é feita para as notas NFS-e nacional e NFS-e simplificada.

- **SUP0552 - Importação de nota/frete via arquivo texto**

- Para fretes de compra(tipo CON) e fretes de venda (tipo COV), foi alterado o nome da linha onde os tributos são informados, passando da linha "P" para a linha "B". Isso foi necessário devido a conflitos com a modificação de fretes.
- Foi alterado para que seja possível importar a chave eletrônica e protocolo do frete e da nota.

- **SUP34340 - Relatório de Pagamento Antecipado**

- Foi incluído o filtro por data de entrada da nota. Deverá ser atualizado pelo log00074 o xml: sup34340.xml.

### Pacote 08/06

- **IS (Imposto Seletivo)**

"Conforme [Lei Complementar 214, Art. 409](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm) . Fica instituído o Imposto Seletivo, de que trata o [inciso VIII do art. 153 da Constituição Federal](https://www.planalto.gov.br/ccivil_03/Constituicao/Constituicao.htm#art153-8) , incidente sobre a produção, extração, comercialização ou importação de bens e serviços prejudiciais à saúde ou ao meio ambiente. Consideram-se prejudiciais à saúde ou ao meio ambiente os bens classificados nos códigos da NCM/SH e o carvão mineral, e os serviços listados no [Anexo XVII](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm#anexo17) , referentes a:

I - veículos;

II - embarcações e aeronaves;

III - produtos fumígenos;

IV - bebidas alcoólicas;

V - bebidas açucaradas;

VI - bens minerais;

VII - concursos de prognósticos efantasysport **.**

Os bens a que se referem os incisos III e IV do § 1º estão sujeitos ao Imposto Seletivo quando acondicionados em embalagem primária, assim entendida aquela em contato direto com o produto e destinada ao consumidor final. **O Imposto Seletivo incidirá uma única vez** sobre o bem ou serviço, sendo **vedado** qualquer tipo de **aproveitamento de crédito do imposto** com operações anteriores ou **geração de créditos** para operações posteriores."

Para que seja possível incluir o Imposto Seletivo no Recebimento Logix, foram realizadas as seguintes alterações:

- **Configurador de Tributos (vdp0696/vdp10068):**

- Foram incluídas 3 fórmulas:

- 701 - Base multiplicada pela alíquota;
- 702 - Quantidade multiplicada pela alíquota específica por unidade de medida apropriada;
- 703 - Junção das 2 fórmulas acima, (Base multiplicado pela alíquota) + (Quantidade multiplicada pela alíquota específica por unidade de medida apropriada).

- Para atualização das fórmulas, é necessário rodar o menu "Atualiza Controle de Acesso"
- Depois deverá ser incluido o tributo IS, com origem E(Entrada) e filtros escolhidos;

Observação: Na NT_2025.002_v1.40 cita uma nova tabela de classificação tributária para o IS. No entanto, essa tabela ainda não foi disponibilizada pelo governo.

Para inclusão do IS e respectivas fórmulas, estamos utilizando a classificação tributária do cbs/ibs.

- **Inclusão da Nota de Entrada pelo SUP3760:**

- Foi alterado a consistência da nota de entrada, para que busque o tributo "IS" do configurador, e também inclua esse tributo na base de cálculo do CBS/IBS;
- Alteramos o SUP34120(Tributos do Item da Nota Fiscal) incluindo a coluna "Compl", onde para o tributo "IS"(imposto seletivo), ao clicar na linha, será apresentando uma tela auxiliar, podendo ser:

- informado o declarado
- visualizado o calculado

com os campos: percentual de alíquota específica, quantidade e unidade de medida.

1- Para essa alteração foi necessário a criação de novos campos(alíquota específica, quantidade e unidade de medida) nas tabelas que armazenam os tributos: sup_ar_item_fisc e tabelas de histórico;

Sendo Necessário rodar o conversor de tabela pelo log6000: sup02147.cnv

E os xmls pelo log00074: sup34120.xml, sup341201.xml, sup_ar_item_fisc.xml, h_sup_ar_item_fisc.xml e hh_sup_ar_item_fisc.xml

2- Foram alterados os programas de envio e retorno de histórico(SUP2510, SUP1052 e SUP34071) , para trabalharem com os novos campos;

- **OBF40000 - Emissão da nota eletrônica**

- Alterado programa para que seja emitido xml com o grupo de "IS" - Imposto Seletivo, conforme exemplo em xml abaixo:

- **SUP34204 - Importação de nota via xml**

- Alterado a importação das notas de entrada, para buscar os valores do 'IS' - Imposto Seletivo no xml, e incluir como valores declarados na nota de entrada.

- **SUP0552 - Importação de nota via arquivo texto**

- Alterado o programa para importar o tributo 'IS' - Imposto Seletivo na coluna "O", e seus novos campos: percentual de alíquota específica, quantidade e unidade de medida.

- **Relatórios -** alterado para mostrar a coluna de valores do "IS" - Imposto Seletivo

- SUP34032 - Notas Fiscais e Fretes
- SUP34041- Recebimento de Materiais - Rastreabilidade
- SUP4410 - Recebimento de Materiais - Rastreabilidade

- **Ajustes da NT 1.40**

- Para notas de devolução, ao relacionar com a nota de saída, alterado para não perguntar "Deseja imprimir como documento referenciado?", pois deverá sempre imprimir na tag DFeReferenciado:

- **Fretes**

- Criado botão, no SUP34216, para exclusão dos rateios de um frete de uma única vez,

Sendo Necessário rodar os xmls pelo log00074: sup34216.xml e sup34217.xml

### Pacote 20/07

- **Compras Governamentais**

"Conforme [Lei Complementar 214, Art. 473](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm) . O produto da arrecadação do IBS e da CBS sobre as aquisições de bens e serviços pela adminiatração pública direta, por autarquias e por fundações públicas será integralmente destinado ao ente federativo contratante, mediante redução a zero das alíquotas do IBS e da CBS devidos aos demais entes federativos e equivalente elevação da alíquota do tributo devido ao ente contratante".

Para que seja possível calcular o "Compras Governamentais" no Recebimento Logix, foram realizadas as seguintes alterações:

- **No SUP3760 - Entrada de Notas Fiscais:**

- Foi incluído no menu 7_inf_compl_nf o menu que abrirá a tela abaixo:

Onde poderá ser incluído as informações:

- Entidade Pública que está fazendo a compra;
- Redução da alíquota do tributo;
- Operação que está sendo realizada;
- Chave de acesso da operação realizada anteriormente.

Conforme as opções do xml:

Observação:

Se o tipo de operação for:

- 2- Recebimento de pagamento com fornecimento já realizado;
- 3- Fornecimento com pagamento já realizado;

Deverá ser informado a chave eletrônica da nota anterior. Essa nota anterior, precisa ter um dos tipos de operação abaixo:

- 1- Fornecimento com pagamento posterior;
- 4- Recebimento do pagamento com fornecimento posterior.

- **Consistência da Nota de Entrada pelo SUP3760/SUP8720:**

- Foi alterado a consistência da nota de entrada, para enviar as informações do "Ente Governamental" e o "percentual de redução de alíquota" para o configurador de tributos,

onde o mesmo irá calcular e retornar os tributos, conforme as regras da NT2025.002 v1.50:

- De 2027 até 2032:

- CBS será calculado com a alíquota informada no configurador de tributos;
- Se Ente Governamental = 1(União) - Valor somado de todos os tributos no CBS, portanto, IBS_UF = 0(zero) e IBS_MUN = 0(zero);
- Se Ente Governamental = 2(Estadual) ou 3(DF) - Valor somado no IBS_UF, portanto, IBS_MUN= 0(zero);
- Se Ente Governamental = 4(Municipal) - Valor somado no IBS_MUN, portanto, IBS_UF = 0(zero);

- De 2033 ou superior:

- Se Ente Governamental = 1(União) - Valor somado de todos os tributos no CBS, portanto, IBS_UF = 0(zero) e IBS_MUN = 0(zero);
- Se Ente Governamental = 2(Estadual) ou 3(DF) - Valor somado no IBS_UF, portanto, CBS = 0(zero) e IBS_MUN= 0(zero);
- Se Ente Governamental = 4(Municipal) - Valor somado no IBS_MUN, portanto, CBS = 0(zero) e IBS_UF = 0(zero);

Os tributos com final GOV: CBS_GOV, IBS_UF_GOV e IBS_MUN_GOV, serão o calculo sem a soma acima. Por exemplo, se o Ente Governamental = 2(Estado), o IBS_UF = R$5,00 e o IBS_MUN = 0,

já o IBS_UF_GOV = R$2,50 e o IBS_MUN_GOV = R$2,50. Esses tributos calculados, podem ser consultados no SUP3760 - Entrada de Nota Fiscal, menu Q-impostos, A-tributos.

- **OBF40000 - Emissão da nota eletrônica**

- Alterado programa para que seja emitido xml com os grupos referentes ao "Compra Governamental", conforme exemplo em xml abaixo:

Campos da Nota:

Campos do Item:

- **SUP34204 - Importação de nota via xml**

- Alterado a importação das notas de entrada, para buscar os valores referentes aos grupos do "Compras Governamental" no xml, e incluir nas Informações Complementares da Nota e como valores declarados na nota de entrada.

- **SUP0552 - Importação de nota via arquivo texto**

- Alterado o programa para importar as informações do "Compras Governamental",

- na coluna "M" - as informações referentes a nota;
- na coluna "H" - as informações referentes a chave eletrônica de origem;
- na coluna "O" - as informações referentes as tributos (CBS, IBS_UF, IBS_MUN, CBS_GOV, IBS_UF_GOV e IBS_MUN_GOV).

- **Relatórios -** alterado para mostrar a coluna de valores do "Compras Governamental"

- SUP34032 - Notas Fiscais e Fretes
- SUP34041 - Recebimento de Materiais - Rastreabilidade
- SUP4410 - Recebimento de Materiais - Rastreabilidade

- **NF Gás - modelo 76**

- Alterado no SUP3760 - Nota Fiscal de Entrada, menu 7_inf_compl_nf, menu nf_eletronica, para poder informar a "Finalidade" e o "Motivo de Substituição" corretos para esse tipo de nota.
- Na consistência, caso esteja parametrizado para obrigar a chave eletrônica, apresentará erro na nota.

Necessário rodar o suca0006 dentro do programa FIN00000.

- **NFS - Nota Fiscal de Serviço**

- Alterado o SUP8720- Nota Fiscal de Serviço por Contrato, para que possa ser informado o "Tipo" da NFS:

- **NFSe Locação - Nota Fiscal de Serviço de Locação(Bens móveis e imóveis) e Obras**

- No SUP3760- Nota Fiscal de Entrada, menu inf_compl_item, foi criado o menu "2-Loc/Obras", que irá abrir o programa SUP34740, onde para cada item de "SERVIÇO" da nota, poderá ser informado até 99 bens móveis/imóveis ou obras.

- No grid dessa tela, para cada Bem móvel/imóvel ou obra, poderá ser informado as deduções.
- Esse valor somado, será diminuido da base do CBS,IBS_UF e IBS_MUN. Necessário rodar o "Atualiza CTR" no VDP0696/VDP10068 - Configurador de tributos.
- A descrição do tipo de dedução só poderá ser informada quando o Tipo = 99 Outros.

Para essa alteração é necessário rodar os conversores de tabela pelo log6000: sup02153.cnv, sup02154.cnv e sup2157.cnv

E xmls de tela e tabela pelo log00074: aviso_rec_obra_loca.xml, h_aviso_rec_obra_loca.xml, hh_aviso_rec_obra_loca.xml, aviso_rec_deducao.xml, h_aviso_rec_deducao.xml, hh_aviso_rec_deducao.xml, sup34740.xml

- **Histórico**

- Os programas de envio de histórico (SUP2510) e recuperação de histórico (SUP1052 e SUP34071) foram alterados para considerar as novas tabelas. As alterações foram realizadas no envio/recuperação de histórico, e no envio/recuperação do histórico do histórico.

- **Ajuste SINIEF 49/25 e SINIEF 20/26,** referentes a **NF-e de entrada de crédito** (finNFe= 5) com os tipos (3, 4 e 6):

- **Identificação Automática de Devolução:** Ao informar uma Nota Fiscal Complementar (NFC) com classificação de "Nota de Crédito" e tipos específicos de retorno ou redução (3, 4 e 6), o sistema alerta o usuário e altera automaticamente a espécie para Nota Fiscal de Devolução (NFD).
- **Tipo 03-Retorno por Recusa na Entrega ou Por Não Localização do Destinatário na Tentativa de Entrega:** Para esses casos de recusa total o sistema agora carrega automaticamente todos os itens e dados da nota de saída de origem, eliminando mensagens intermediárias e reduzindo o tempo de digitação.
- **Tipo 04-Redução de Valores e Quantidades:** Para essas notas de crédito, diferentemente dos retornos por recusa (Tipos 3 e 6), os itens da nota de saída de origem não são carregados automaticamente e a mensagem de alerta de devolução não é exibida. Isso ocorre para dar flexibilidade ao usuário, que deve preencher os itens manualmente, informando apenas as reduções específicas de valor ou quantidade desejadas.
- **Tipo 06-Retorno por Recusa Parcial na Entrega:** Nesses tipo de retorno por recusa parcial o usuário pode optar por carregar os dados da nota de saída original, facilitando o preenchimento dos itens que estão sendo devolvidos
- **Consistência de Dados:** O sistema impede alterações manuais inconsistentes em notas que já possuem relacionamento com documentos de saída, garantindo que a classificação e o tipo de nota de crédito permaneçam íntegros durante todo o processo de recebimento

Alterado para não gerar consistência para os impostos (ICMS, IPI, PIS/COFINS...) e gerar o xml corretamente no OBF40000 - Emissão de nota fiscal eletrônica.

### Pacote 10/08

- **Classificação Tributária**

- Alterado o SUP34260 - Cadastro da Classificação Tributária para incluir os novos campos
- E arquivo de importação [cclassif_tributaria.txt](https://tdn.totvs.com/download/attachments/948652302/cClassTrib%202026-08-10.txt?version=1&modificationDate=1786046897300&api=v2) com os novos códigos.

conforme IT 2025.002 versão 1.60 de 23/06/2026.

Para essa alteração é necessário processar o conversor de alteração de tabela no log6000: sup02160.cnv

E xml pelo log00074: classif_tributaria.xml e sup34260.xml

- **Consistência da Nota**

- Para Notas de Devolução que possuem PIS/Cofins, estava apresentando diferença do valor Declarado x Calculado na base dos tributos CBS,IBS_UF, IBS_MUN e IS. Foi alterado para considerar o PIS/Cofins primeiro da nota de saída, e posteriormente da nota de devolução;
- Foi alterado para não exigir os tributos CBS,IBS_UF, IBS_MUN e IS quando a éspecie do documento não for fiscal: "DOC" e "REC";
- Alterado para calcular os tributos para as notas NFR, sem relacionamento com notas de saída;

**Evento 211110 - Solicitação de Apropriação de crédito presumido**

- Alterado para envio no layout da NT 2025.002 na versão 1.40.

### Pacote 31/08

- **Descontar o ISS não retido(a recolher) da base do CBS/IBS/IS**

- Esse ISS é informado no SUP3760- Nota fiscal de entrada, SUP8720 - Nota fiscal com contrato ou SUP0580 - Nota fiscal de Frete, ao selecionar o campo "IR/INSS/ISS?" = Sim;

Informando o campo "Ret ISS" = Sim, e o valor no campo "Valor ISS".

- **Descontar o ISS retido anteriormente, da base do CBS/IBS/IS**

- O ISS retido anteriormente ou com ISSQN - não sujeito a retenção, também precisa ser descontado da base do CBS/IBS/IS nas notas fiscais de serviço, ou notas de débito e crédito.

Para isso, alteramos o configurador de tributos, para que seja possível incluir a fórmula de cálculo para o ISS_REC de Entrada:

Com as fórmulas:

- 701 - ISS a recolher, por alíquota, com base utilizando o **valor bruto** , sendo possível informar a redução da base;
- 702 - ISS a recolher, por alíquota, com base utilizando o **valor líquido** , sendo possível informar a redução da base;

Para atualização das fórmulas, é necessário rodar o menu "Atualiza Controle de Acesso" no configurador de tributos (vdp0696/vdp10068)

Depois deverá ser incluido o tributo ISS_REC, com origem E(Entrada) e filtros escolhidos;

não pode ser informado os valores declarados.

O valor calculado para o ISS_REC será diminuído da base do CBS, IBS_UF, IBS_MUN, IS, CBS_CR_PRE(crédito presumido) e IBS_CR_PRE(crédito presumido).

E pode ser consultado na tela de tributos:

Esse tributo apenas pode ser consultado, não podem ser informados os valores declarados.

Alterado também o SUP0580 - Inclusão de Conhecimento de Fretes, para calcular o ISS_REC e mostrar na tela de tributos SUP34217;

Para essa alteração, é necessário rodar o XML de tela pelo log00074: sup34120.xml

**Zona de Livre Comércio - grupo gALCZFMCBS**

- Conforme a NT 2025.002 na versão 1.40, se uma empresa (Pessoa Jurídica) estabelecida na ZFM ou na ALC vender um produto nacional ou prestar um serviço físico para alguém que também está localizado dentro dessa mesma área (seja empresa ou pessoa física), a alíquota da CBS fica reduzida a zero.

Em resumo: É o benefício das chamadas "operações internas". Se o vendedor é de Manaus e vende para um morador ou loja de Manaus, ele não paga a CBS sobre essa venda. Se ele vender para São Paulo, essa regra já não se aplica. Para emitir as informações sobre esse benefício, devem ser emitidas no grupo **gALCZFMCBS** . Nesse grupo, será demonstrado o "Tipo de aplicação de alíquota zero para a CBS" e o "número do Processo na Suframa para o item comercializado".

Para essa alteração, foi incluído no configurador de tributos, nas informações adicionais, o campo Tipo Aliq ALCZFM:

e a tributação precisa ter 100% de redução de alíquota:

- Quando o campo "Tipo Aliq ALCZFM" estiver preenchido,
- o fornecedor possuir Suframa no VDP10000 - Cadastro de fornecedores, aba cliente,
- e o item possuir número do processo Suframa no MAN10021 - Cadastro do item, aba comercial,

na consistência da nota de entrada pelo SUP3760/SUP8720, irá gerar o CBS com as informações no botão de Compl:

Também será gerado o CBS_REG, como demonstrativo da alíquota normal, sem a redução aplicada:

Também foram realizadas alterações nos programas:

- OBF40000 - Foi alterado para a emissão das notas com o **grupo gALCZFMCBS;**
- SUP34204 - Foi alterado para a importação dos xmls com o **grupo gALCZFMCBS;**
- Programas de envio/retorno de histórico (sup2510, sup1052, sup34071)

Foi necessário modificar as tabelas: sup_ar_item_fisc, h_sup_ar_item_fisc e hh_sup_ar_item_fisc.

Devendo ser rodado o conversor de alteração de tabela pelo log6000: sup02158.cnv, sup02162.cnv e sup02163.cnv

E rodar o xml de tela pelo log00074: sup341202.xml, sup_ar_item_fisc.xml, h_sup_ar_item_fisc.xml, hh_sup_ar_item_fisc.xml, frete_sup_fisc.xml, h_frete_sup_fisc.xml, hh_frete_sup_fisc.xml, sup_frete_item_fisc.xml, h_sup_frete_item_fisc.xml, hh_sup_frete_item_fisc.xml

- **NF-e ABI (Alienação de Bens Imóveis)**

- A NF-e ABI é o novo documento fiscal eletrônico nacional destinado a documentar operações de alienação de bens imóveis, atendendo à Lei Complementar 214/2025. Emitida e armazenada exclusivamente em formato digital, possui validade jurídica garantida pela assinatura digital do emitente e pela Autorização de Uso concedida pelo Ambiente Nacional.
- Foi alterado para poder incluir no SUP3760 - Entrada de Nota Fiscal e SUP8720 - Nota fiscal de serviço com contrato, a Nota de Alienação de Bens Imóveis, modelo 77.

- No menu 7_info_compl_nf, menu nf_eletrÔnica, foi alterado para poder informar as finalidades corretas. Sendo que, a finalidade de substituição permite informar a chave eletrônica de substituição;
- Alterada a consistência da nota, para caso seja o modelo 77 e a chave eletrônica não for informada, apresentar consistência.

- **NFM x NFP**

- Alterada a consistência da nota para que as NFP(notas fiscais de recebimento parcial) não gerem os tributos.

### Pacote 21/09

- **Contabilização**

- As contas contábeis para os tributos: CBS, IBS_UF, IBS_MUN, IS, etc..., podem ser informadas no configurador de tributos (vdp0696/VDP10068), na opção Adicionais ou diretamente nas telas de tributos:

- da nota(SUP34120) - acessado pelo SUP3760/SUP8720 - Nota fiscal de Entrada, menu Q-impostos, menu A-tributos;
- do frete(SUP34217) - acessado pelo SUP0580 - Nota fiscal de frete, menu Q-impostos, menu A-tributos.

- Para o CBS, IBS_UF e IBS_MUN, a contabilização poderá ser realizada de 2 formas:

- Caso seja informado **apenas** a conta **contábil de débito** :

- O crédito do tributo será juntamente com o valor do item e tributos, na conta contábil do Fornecedor;
- E o débito à apropriar será na conta informada nas telas de tributos (SUP34120/SUP34217);

- Caso seja informado as contas contábeis de **débito e crédito** :

- O crédito será na conta contábil transitória do tributo informada nas telas (SUP34120/SUP34217);
- E o débito à recuperar será na conta informada nas telas de tributos (SUP34120/SUP34217);

- Para o IS(imposto seletivo), a contabilização poderá ser realizada de 2 formas:

- Caso seja informado **apenas** a conta **contábil de crébito** :

- O crédito será na conta contábil transitória do tributo, informada nas telas de tributos (SUP34120/SUP34217);
- E o débito será juntamente com o valor do item, na conta contábil do item;
- A conta contábil do fornecedor será creditada com o valor do item e dos tributos, sem o valor do IS;

- Caso seja informado as contas contábeis de **débito e crédito** :

- O crédito será na conta contábil transitória do tributo, informada nas telas de tributos (SUP34120/SUP34217);
- O débito do tributo será na conta contábil de custos e despesas, informada nas telas (SUP34120/SUP34217);
- A conta contábil do fornecedor será creditada com o valor do item, dos tributos e do valor do IS;
- A conta contábil do item será debitada com o valor do item e o valor do IS;

Observação: Caso não seja informada nenhuma conta contábil, não será contabilizado os tributos.

- Para devoluções de fornecedores - a contabilização inverte as contas contabeis informadas na nota fiscal de origem;
- Para devoluções de clientes ou Notas de crédito de Recusa(onde a empresa é a responsável pela Venda)- a contabilização utiliza as contas contábeis do faturamento, e inverte;
- Para transferência entre unidades - a contabilização utiliza as contas contábeis do faturamento caso existam, ou conforme as contas na tela de tributos (SUP34120);
- Frete Compra e Frete Venda - serão contabilizados conforme as contas na tela de tributos (SUP34217).

### Pacote 12/10

**Zona de Livre Comércio para o FRETE - grupo gALCZFMCBS**

- Conforme alterações liberadas no pacote da RT do dia 31/08/2026:

- o configurador de tributos (vdp0696/vdp10068) precisa estar configurado com o campo "Tipo Alíq ALCZFM", e a tributação precisa ter 100% de redução de alíquota;

- e o fornecedor possuir Suframa no VDP10000 - Cadastro de fornecedores, aba cliente

na consistência do frete pelo SUP0580, irá gerar o CBS com as informações no botão de Compl:

Também será gerado o CBS_REG, como demonstrativo da alíquota normal, sem a redução aplicada.

Caso o "Tipo Aliq ALCZFM" for 2- Operação industrial com processo aprovado na Suframa. Deverá ser informado o número do Processo Suframa na linha dos valores Declarados.

Foi necessário modificar as tabelas: frete_sup_fisc, h_frete_sup_fisc e hh_frete_sup_fisc, sup_frete_item_fisc, h_sup_frete_item_fisc e hh_sup_frete_item_fisc;

Devendo ser rodado o conversor de alteração de tabela pelo log6000: sup02164.cnv;

E rodar o xml de tela pelo log00074: sup34216.xml, sup342162.xml, sup34217.xml, sup342171.xml, frete_sup_fisc.xml, h_frete_sup_fisc.xml, hh_frete_sup_fisc.xml, sup_frete_item_fisc.xml, h_sup_frete_item_fisc.xml, hh_sup_frete_item_fisc.xml;

### Pacote 26/10

**Tabela de Classificação Tributária - Referente ao IT 2025.002.v.1.70**

- Conforme alterações do informe técnico de 01/10/2026, foi alterado a tabela(classif_tributaria), programa(SUP34260) e arquivo de importação da Classificação Tributária.

Incluindo os campos de indicador de doação e Receita Bruta do Simples Nacional, e novos códigos de classificação que podem ser importados conforme arquivo de importação: [cclassif_tributaria.txt](https://tdn.totvs.com/download/attachments/948652302/cclassif_trib.txt?version=1&modificationDate=1792506973103&api=v2)

Foi necessário modificar a tabela classif_tributaria;

Devendo ser rodado o conversor de alteração de tabela pelo log6000: sup02166.cnv;

E rodar o xml de tela pelo log00074: sup34260.xml.

**Tributação Monofásica**

A tributação monofásica é um regime em que o recolhimento de um tributo é concentrado no início da cadeia produtiva, geralmente no fabricante ou importador. Nas etapas seguintes de revenda (distribuidores e varejistas), as alíquotas dessas contribuições são reduzidas a zero, evitando a bitributação.

Conforme a NT 2025.002.v1.50 foi alterado o layout do xml, separando os grupos entre **Ad Rem** e **Ad Valorem** .

- Ad Rem - A alíquota ad rem é um modelo de cobrança onde o imposto incide sobre uma **quantidade, peso ou volume específico** do produto (valor fixo por litro ou quilo);
Ad Valorem - Significa que o imposto é calculado aplicando-se uma **alíquota percentual** diretamente sobre o **valor da operação.**

- Dentro dos grupos Ad Rem e Ad Valorem, existem os subgrupos conforme a classificação tributária:

- gMonoPadrao - Monofásico Padrão;
- gMonoReten - Monofásico Sujeito à Retenção;
- gMonoRet - Monofásico Retido Anteriormente;
- gpBioDiferenca - mistura de EAC com gasolina A em percentual inferior ou superior ao obrigatório.

- Para adequação do sistema, foram criadas as seguintes fórmulas no configurador:

- Ad Valorem

- gMonoPadrao - Utilizar as fórmulas 701 do CBS,IBS_UF e IBS_MUN;
- gMonoReten - Deverá ser cadastrado os tributos "CBS_MONO_RET" e "IBS_MONO_RET", utilizando a fórmula 703, informando o campo "Tipo de Retenção" = S, sujeito à retenção;
- gMonoRet - Deverá ser cadastrado os tributos "CBS_MONO_RET" e "IBS_MONO_RET", utilizando a fórmula 703, informando o campo "Tipo de Retenção" = R, retido anteriormente;
- gpBioDiferenca- Deverá ser cadastrado os tributos "CBS_MONO_RET" e "IBS_MONO_RET", utilizando a fórmula 704.

- Ad Rem

- gMonoPadrao - Utilizar as fórmulas 703 do CBS,IBS_UF e IBS_MUN;
- gMonoReten - Deverá ser cadastrado os tributos "CBS_MONO_RET" e "IBS_MONO_RET", utilizando a fórmula 701, informando o campo "Tipo de Retenção" = S, sujeito à retenção;
- gMonoRet - Deverá ser cadastrado os tributos "CBS_MONO_RET" e "IBS_MONO_RET", utilizando a fórmula 701, informando o campo "Tipo de Retenção" = R, retido anteriormente;
- gpBioDiferenca- Deverá ser cadastrado os tributos "CBS_MONO_RET" e "IBS_MONO_RET", utilizando a fórmula 702.

Para utilizar as fórmulas, é necessário rodar o "Atualiza CTR" no vdp0696/vdp10068.

Para o gMonoReten, gMonoRet e gpBioDiferenca, também é necessário o cadastros da tributação monofásica no vdp10303:

- Também foram alterados os programas abaixo:

- SUP34120 - Tela de tributos da nota

- Para apresentação dos novos tributos
- Na coluna "Compl", mostrar as informações complementares da "gpBioDiferenca":

- OBF40000 - Emissão da nota fiscal eletrônica, para emitir o novo layout do xml com as informações da tributação monofásica;

- SUP0552 - Importação de arquivo texto, para importar a tributação monofásica, na linha "O", conforme os demais tributos da reforma.
- SUP34204 - Importação de arquivo xml, para importar a tributação monofásica;
- SUP4410/SUP34041 e SUP34032 - relatórios de informações das notas de entrada, incluindo em tela a opção "Monofásico", onde no relatório serão impressos as informações sobre essa tributação;

Foi necessário modificar as tabelas: sup_ar_item_fisc, h_sup_ar_item_fisc e hh_sup_ar_item_fisc;

Devendo ser rodado o conversor de alteração de tabela pelo log6000: sup02165.cnv;

E rodar o xml de tela pelo log00074: sup34120.xml, sup341203.xml, sup34032.xml, sup34041.xml, sup_ar_item_fisc.xml, h_sup_ar_item_fisc.xml e hh_sup_ar_item_fisc.xml

'"
