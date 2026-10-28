# Reforma Tributária Logix — Vendas e Faturamento

Fonte: <https://tdn.totvs.com/pages/releaseview.action?pageId=948652337>

## 1. Visão Geral

A **Reforma Tributária** traz um cenário de mudanças significativas nas regras tributárias brasileiras, exigindo das empresas uma adaptação rápida e precisa para garantir conformidade e eficiência operacional.

2026

## Pacote 02/02

**Funcionalidades Principais:**

- Adequação de campos novos para o pedido - **VDP20000**

Foi alterada a rotina de pedidos ( **VDP20000** ) com os novos campos e validações que foram implementadas inicialmente somente no faturamento manual.

Informações de NFS-e

Foi incluído na aba 8-Adicionais informações da NFS-e os campos :

| Indicador Final | É um campo que indica operação de uso ou consumo pessoal. |
| --- | --- |
| Código Indicador de Operação | Define a natureza e o local de incidência do IBS/CBS, sendo crucial para classificar se o serviço é para uso/consumo pessoal ou não, e deve ser preenchido conforme a Tabela de Indicadores de Operação do Anexo VII da legislação da NFS-e Nacional para garantir a conformidade fiscal e o correto creditamento/débito dos impostos. |
| Tipo operação | Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis: - 1 - Fornecimento com pagamento posterior - 2 - Recebimento do pagamento com fornecimento já realizado - 3 - Fornecimento com pagamento já realizado - 4 - Recebimento do pagamento com fornecimento posterior - 5 - Fornecimento e recebimento do pagamento concomitantes Conforme a Regra de validação da NFS-e: Código do tipo de Operação (tpOper) deve ser informado quando se tratar de uma compra governamental ou um dos serviços da LC 116/2003 listados: 25.05; 15.09; 17.12; 10.05 |

Informações para NF-e:

Foi incluído no grid de itens o campo indicador de doação (SIM/NÃO)

Na Opção 3-Frete ao clicar o botão Inf. Compl. NF-e foi incluído o campo data de previsão de entrega.

O campo pode ser informado de a Modalidade do frete for diferente de 1,4,9.

Na opção 7- Referência foi incluído novo tipo de referência de Pagamento Antecipado.

Foi implementado na consistência de pedidos a validação para verificar se a natureza de operação possuir um dos novos tributos da reforma, é necessário ter os 3 tributos: CBS, IBS_UF e IBS_MUN, tendo os 3 tributos, é necessários que estejam configurados com o mesmo CST e Classificação tributária, caso não estejam irá dar uma mensagem e não permitir continuar a inclusão da solicitação enquanto não seja feito o ajuste da configuração fiscal.

A validação ocorre quando o parametro do LOG00086 - Consistir os tributos no pedido? (consist_trib_pedido) está S e o parametro Data inicial da reforma tributária (data_inicio_ref_trib) está informada e com data inferior a data do pedido.

Exemplos de consistências:

Natureza de operação possui CBS e IBS_UF cadastrados, porém não tem IBS_MUN:

Natureza de operação com os tributos cadastrados, porém com configuração fiscal com Classificação tributária divergente:

Alterado o VDP20029 para enviar os novos campos/tabelas para as tabelas de histórico.

Os Programas VDP0742 e VDP0745 foram alterados para incluir os novos campos da inclusão do pedido(VDP20000) nas tabelas de faturamento para emissão da NFe/NFS-e.

- Tributação regular com redução de aliquota

Incluído novo campo no cadastro de configuração fiscal ( **taxa_reducao_pct_reg)** quando for informado efetuará a redução da alíquota efetiva.

Foi alterado o VDP0696 e VDP10068, incluido o novo adicional "Taxa redução Reg", que deverá ser informado, caso a tributação regular tenha redução de alíquota.

Para que o campo fique disponível é necessário executar a opção 'Atualizar' do VDP10064.

Alterado as funções de calculo dos tributos para considerar a taxa de redução do tributo regular, na consulta da nota poderá ser verificado o % de redução e também a aliquota efetiva do tributo regular, que será gravando quando houver taxa de redução:

OBF40000/VDP9202 - Alterado o envio do xml da NF-e para considerar a alíquota efetiva para o tributo regular:

Até o momento já foram liberados as alterações para atender os seguintes cenários de tributação do IBS/CBS:

| Tributado integralmente | CST 000 |
| --- | --- |
| Tributado com redução de alíquota ( com tributação regular)* | CST 200 |
| Tributado com diferimento parcial ou total | CST 510/515 |
| Tributação imune e não incidência | CST 410 |
| Tributação suspensa (com tributação regular) * | CST 550 |
| Grupo Pagamento Antecipado | |
| Notas com finalidade débito | |
| Tributação crédito presumido | |
| Grupo Transferência de Crédito | CST 800 |
| Eventos (Cadastros e envio do xml) via TSS e TC2 | |
| Estorno de crédito | |
| Ajuste de competência | CST 811 |
| Indicador bem móvel usado | |
| Indicador de doação | |
| NFS-e - Cadastros e Faturamento | |
| NFS-e - Envio do xml modelo Nacional via TSS | |
| NFS-e - Envio do xml no leiaute único TSS | |

*Verificar na tabela cClassTrib para quais deverão ser enviados o grupo de tributação regular

** Avaliar o CST conforme situação

Abaixo a relação de tributações e tipos de notas que ainda **não** foi implementado, será liberado em pacote futuro:

| Tributação monofásica - [https://tdn.totvs.com/x/64kVPQ](https://tdn.totvs.com/x/64kVPQ) |
| --- |
| Grupo de Compra governamental |
| Grupo de Informações da devolução de tributos |
| DANFE (com os novos tributos) |

## Pacote 23/02

**Funcionalidades Principais:**

- Inclusão do Código NBS no pedido - **VDP20000**

Foi alterada a rotina de pedidos ( **VDP20000** ) para a inclusão do campo Código NBS.

Foi incluído nos Dados Adicionais do Item :

- Incluído no **VDP40005** o campo Código NBS na consulta do item.

- Alterado os programas **VDP40003** e **VDP20029** para enviar o campo cod_nbs para histórico.

- Alterado programa de faturamento **VDP0745** para gravar na tabela fat_nf_item o cod_nbs.

- Alterado o programa **VDP0746** para incluir o campo de Código NBS na tela de digitação dos Itens.

- Alterado o **OBF50000** para na geração da NFS-e ler o novo campo cod_nbs da tabela fat_nf_item e se estiver preenchido utilizar, senão buscar do cadastro do item.

- Adequação dos programas para CNPJ Alphanumérico :

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

Foram alterados os programas para aceitar a numeração alphanumérica :

VDP10000 :

VDP20000

Até o momento já foram liberados as alterações para atender os seguintes cenários de tributação do IBS/CBS:

| Tributado integralmente | CST 000 |
| --- | --- |
| Tributado com redução de alíquota ( com tributação regular)* | CST 200 |
| Tributado com diferimento parcial ou total | CST 510/515 |
| Tributação imune e não incidência | CST 410 |
| Tributação suspensa (com tributação regular) * | CST 550 |
| Grupo Pagamento Antecipado | |
| Notas com finalidade débito | |
| Tributação crédito presumido | |
| Grupo Transferência de Crédito | CST 800 |
| Eventos (Cadastros e envio do xml) via TSS e TC2 | |
| Estorno de crédito | |
| Ajuste de competência | CST 811 |
| Indicador bem móvel usado | |
| Indicador de doação | |
| NFS-e - Cadastros e Faturamento | |
| NFS-e - Envio do xml modelo Nacional via TSS | |
| NFS-e - Envio do xml no leiaute único TSS | |

*Verificar na tabela cClassTrib para quais deverão ser enviados o grupo de tributação regular

** Avaliar o CST conforme situação

Abaixo a relação de tributações e tipos de notas que ainda **não** foi implementado, será liberado em pacote futuro:

| Tributação monofásica - [https://tdn.totvs.com/x/64kVPQ](https://tdn.totvs.com/x/64kVPQ) |
| --- |
| Grupo de Compra governamental |
| Grupo de Informações da devolução de tributos |
| DANFE (com os novos tributos) |

## Pacote 06/04

**Funcionalidades Principais:**

- **Ajuste SINIEF nº 49/2025 - Parte 1**

Para atender o Ajuste SINIEF nº 49/2025, que regulamenta a emissão de Notas Fiscais de Débito (Finalidade 6) para operações de faturamento antecipado e regularização de estoque, criando CFOPs específicos para estas operações foram alterados os programas:

**VDP0696/VDP10068** - Alterada configuração fiscal dos tributos para incluir o adicional do CFOP para os novos tributos da Reforma Tributária: CBS, IBS_MUN e IBS_UF. É necessário processar o Atualizar do VDP10064 para que o adicional fique disponível para os tributos.

**VDP0746** - Alterado faturamento para gravar o respectivo CFOP na fat_nf_item_fisc para cada tributo, conforme o parametrizado na configuração fiscal.

**OBF40000/VDP9202** - Alterado para gravar na tag <CFOP> o respectivo CFOP conforme parametrizado na configuração fiscal.

OBS: A seleção do CFOP selecionará o MAX(cod_fiscal) encontrado, pois a tag <CFOP> é única por item/sequencia.

**Anteriormente, quando a nota não tinha ICMS destacado e não encontrava dados do código fiscal para os novos tributos, o sistema alimentava a tag <CFOP> com dados fixos, para evitar erro no XML. Sendo os valores utilizados anteriormente como 5949 (dentro do estado), 6949 (fora do estado) e 7949 (exportação), a partir dessa atualização é necessário informar o CFOP para os tributos para que não ocorra falha de schema.**

- **NFS-e (Modelo Nacional): NT 007 - Ajustes referente os valores de PIS e COFINS**

Foi publicada a NT 007 da NFS-e para o modelo nacional esclarecendo informações sobre como devem ser gerados os valores de PIS e COFINS de apuração própria e retidos, onde os valores do PIS/COFINS de apuração própria devem ser gerados nas tags vPis e vCofins, e se houver retenção deve ser somados ao CSLL e gerado na tag vRetCSLL. Também foram implementadas novas opções para a tag tpRetPisCofins

Até o momento já foram liberados as alterações para atender os seguintes cenários de tributação do IBS/CBS:

Foram alteradas as funções de envio da NFS-e, para buscar os valores de PIS/COFINS conforme alterações da NT.

**Para envio do XML com as alterações da NT007 da NFS-e é necessário a atualização dos schemas do TSS.**

- **Demais ajustes e manutenções:**

**NF-e / Devoluções:**

Ao gerar uma Nota Fiscal de Saída do tipoDevolução a Fornecer, o sistema estava retornando a **Rejeição 321 – “NF-e de devolução de mercadoria não possui documento fiscal referenciado”** , devido à ausência do vínculo com a nota fiscal de entrada correspondente.

DT - [26145720 DMANFATMANUT-14002 DT - Rejeição de NF de Devolução ao fornecedor.](https://tdn.totvs.com/pages/viewpage.action?pageId=1036763628)

Verificação dos novos tributos na nota de entrada

DT - [26718588 DMANFATMANUT-15194 DT NF emitida não está gerando cClassTrib](https://tdn.totvs.com/pages/viewpage.action?pageId=1054121338)

ICMS Desonerado não está abatendo o valor total do item

DT - [26035489 DMANFATMANUT-14511 DT OBF40000- ICMS Desonerado não está abatendo o valor total do item](https://tdn.totvs.com/pages/viewpage.action?pageId=1041761493)

**NFS-e, correção para as rejeições:**

Rejeição: E0712:Para ME-EPP somente um dos 3 poderá ser informado: grupo vTotTrib ou pTotTrib ou pTotTribSN

DT - [25364865 DMANFATMANUT-13947 DT Rejeição no OBF50000 - E0712:Para ME-EPP somente um dos 3 poderá ser informado: grupo vTotTrib ou pTotTrib ou pTotTribSN](https://tdn.totvs.com/pages/viewpage.action?pageId=1034805964)

Rejeição: E0713 - Para Não Optante o indicador de informação de valor total de tributos e o valor percentual aproximado do total dos tributos da alíquota do Simples Nacional (%) não podem ser informados.

DT - [DMANFATMANUT-14747 DT OBF50000 - DT Rejeição E0713 - NT007 NFS-e](https://tdn.totvs.com/pages/viewpage.action?pageId=1043702717)

Rejeição E0120 - IM do prestador não deve ser informado

DT - [DMANFATMANUT-14062 Rejeição E0120 - ajustes para correção](https://tdn.totvs.com/pages/viewpage.action?pageId=1039013014)

Remoção do zero à esquerda na tag **cTribNac** e erro de schema na tag **CNPJ** e **CEP** , devido à montagem incorreta do endereço de entrega quando o município era diferente.

DT - [26223802 DMANFATMANUT-14053 DT OBF50000 - Erros de schema na emissão da NFS-e Nacional na geração das tags cTribNac e CNPJ.](https://tdn.totvs.com/pages/viewpage.action?pageId=1037985674)

**Pedidos:**

Durante o faturamento, estão ocorrendo inconsistências em pedidos inseridos via API REST e via VDP20000 antes da geração da tabelaped_info_nfs_e, devido à ausência de tratamento adequado de valores nulos.

DT - [26402836 DMANFATMANUT-14518 DT VDP0742 Erro no faturamento em pedidos sem registro na tabela ped_info_nf_e](https://tdn.totvs.com/display/LLOG/26402836+DMANFATMANUT-14518+DT+VDP0742+Erro+no+faturamento+em+pedidos+sem+registro+na+tabela+ped_info_nf_e)

VDP20000 - Erro VDP90235_ARMAZENA_DADOS function waiting 6 parameters however was passed 5

DT - [26950309 DMANFATMANUT-15229 DT VDP20000 - VDP90235_ARMAZENA_DADOS function waiting 6 parameters however was passed 5](https://tdn.totvs.com/display/LLOG/26950309+DMANFATMANUT-15229+DT+VDP20000+-+VDP90235_ARMAZENA_DADOS+function+waiting+6+parameters+however+was+passed+5)

**Faturamento:**

No VDP0742, ao incluir uma solicitação de faturamento informando uma OM, ocorre o erro: "Invalid number of returning values on VDP0742_CARREGA_TEMP_TRANSP"

DT - [26394552 DMANFATMANUT-14510 DT VDP0742 problema na inclusao da solicitacao](https://tdn.totvs.com/display/LLOG/26394552+DMANFATMANUT-14510+DT+VDP0742+problema+na+inclusao+da+solicitacao)

Até o momento já foram liberados as alterações para atender os seguintes cenários de tributação do IBS/CBS:

| Tributado integralmente | CST 000 |
| --- | --- |
| Tributado com redução de alíquota ( com tributação regular)* | CST 200 |
| Tributado com diferimento parcial ou total | CST 510/515 |
| Tributação imune e não incidência | CST 410 |
| Tributação suspensa (com tributação regular) * | CST 550 |
| Grupo Pagamento Antecipado | |
| Notas com finalidade débito | |
| Tributação crédito presumido | |
| Grupo Transferência de Crédito | CST 800 |
| Eventos (Cadastros e envio do xml) via TSS e TC2 | |
| Estorno de crédito | |
| Ajuste de competência | CST 811 |
| Indicador bem móvel usado | |
| Indicador de doação | |
| NFS-e - Cadastros e Faturamento | |
| NFS-e - Envio do xml modelo Nacional via TSS | |
| NFS-e - Envio do xml no leiaute único TSS | |

*Verificar na tabela cClassTrib para quais deverão ser enviados o grupo de tributação regular

** Avaliar o CST conforme situação

Abaixo a relação de tributações e tipos de notas que ainda **não** foi implementado, será liberado em pacote futuro:

| Tributação monofásica - [https://tdn.totvs.com/x/64kVPQ](https://tdn.totvs.com/x/64kVPQ) |
| --- |
| Grupo de Compra governamental |
| Grupo de Informações da devolução de tributos |
| DANFE (com os novos tributos) |

## Pacote 18/05

**Funcionalidades Principais:**

- **Integração com o financeiro.**

Alterada a integração do faturamento com o Contas a Receber para enviar os novos impostos quando for acrescido o valor na duplicata, ou seja, quando na configuração fiscal os tributos possuem a aplicação A - Acrescimo N - Nota e Duplicata ou D-Duplicata.

As informações serão gravadas na tabela **cre_previsao_ibs_cbs** e podem ser consultadas no programa **FIN10209** . - [Guia de Uso - Reforma Tributária - Financeiro#-1592630058](https://tdn.totvs.com/pages/viewpage.action?pageId=1009450308#GuiadeUsoReformaTribut%C3%A1riaFinanceiro--1592630058)

Lembrando que em 2026 a Sefaz ainda não está autorizando as notas com os tributos somando no total da nota, para testes pode ser utilizado a aplicação Acréscimo na Duplicata apenas.

## Pacote 08/06

**Funcionalidades Principais:**

- **Imposto Seletivo**

Foram liberadas as alterações para atender o imposto seletivo - IS, conforme especificações da Nota técnica 2025.002.

O novo tributo pode ser consultado no VDP10064 e as novas fórmulas estão no VDP10065, para isso é necessário processar a opção 'Atualizar' do VDP10064

Foram disponibilizadas 3 fórmulas padrões e futuramente conforme necessário serão criadas novas fórmulas, também é possível criar fórmulas especificas caso desejar fazer algum teste.

## Pacote 29/06

**Funcionalidades Principais:**

- **NT008 - NFS-e.**

No pacote de 29/06 não houve liberação de fontes do VDP, porém informamos que foi liberado pelo TSS as alterações para atender a NT 008 da NFS-e, para impressão do DANFSe, quando utilizado o modelo Nacional.

A impressão permanece no OBF50000 utilizando as mesmas funções e métodos, a alteração foi apenas interna para deixar de utilizar a api do portal da NFSe e gerar conforme o leiaute sugerido pela NT0008.

Orientamos a atualização do TSS conforme os links abaixo:

[26145979 DSERTSS1-37622 DT Protheus FISA022 - NFSE Nacional - PDFs DANFSE x Cons. Nacional NT 008 - uso método CONSCHVNFSE001](https://tdn.totvs.com/pages/viewpage.action?pageId=1075942485)

Pacotes:

- TSS 12.1.2310: [https://r.totvs.io/p/1255668](https://r.totvs.io/p/1255668)
- TSS 12.1.2410: [https://r.totvs.io/p/1255669](https://r.totvs.io/p/1255669)
- TSS 12.1.2510: [https://r.totvs.io/p/1255667](https://r.totvs.io/p/1255667)

**Importante** : é preciso fazer o procedimento descrito nesse documento técnico: [https://tdn.totvs.com/x/eEFKQ](https://tdn.totvs.com/x/eEFKQ)

Orientamos que os dados do DANFSe sejam confrontados com a nota fiscal do sistema para garantir consistência e evitar gerar notas com parametrizações diferentes do Sistema Nacional.

## Pacote 20/07

**IMPORTANTE:**
O pacote de 20/07 traz as implementações conforme a NT 2025.002 v1.40. A **atualização é recomendad** a para quem quer estar com o ambiente preparado antes do corte de produção (03/08/2026).

**Importante** : clientes que não se enquadram nos cenários abaixo podem atualizar **apenas o schema** com risco reduzido de rejeição, já que os campos são condicionais e só entram em validação se o cenário de negócio existir:

- **Compra Governamental:** só se vende para ente público, consórcio ou Comitê Gestor do IBS
- **cIndOp (B25d):** só em leilão judicial, licitação pública ou irregularidade documental
- **Imposto Seletivo (adRemIS):** só para produtos sujeitos ao IS
- **DFe Referenciado (item):** obrigatório para devolução a partir de 01/09/2026

**Observação:** o redutor de alíquota de Compra Governamental (art. 472, LC 214/2025) só entra em vigência em 2027. O Imposto Seletivo também só passa a vigorar em 2027, e a tabela de produtos/alíquotas ainda não foi publicada. Por isso, esses dois cenários específicos ainda não se aplicam na prática para nenhum cliente neste momento.

**Atenção** : independente do cenário, os tributos novos (IBS/CBS) precisam ser enviados. Isso não é condicional, é obrigatório para todos os emitentes CRT=3 a partir de 03/08/2026.

De qualquer forma, cabe a cada cliente homologar e validar seus próprios cenários de negócio antes do corte de produção (03/08/2026), através de testes que podem ser realizados no ambiente de homologação disponibilizado pela Sefaz.

**Funcionalidades Principais:**

- **Compra Governamental - NF-e e NFCom**

Alterações necessárias para gerar os grupos gCompraGov e gTribCompraGov referente Compras Governamentais conforme a NT 2025.002 v 1.40 da NF-e e NT 2025.001 da NFCom v1.14a

**VDP10064 - Cadastro de Tributos** :

Criados novos tributos CBS_GOV, IBS_UF_GOV, IBS_MUN_GOV, para que fiquem disponíveis é necessário processar a opção atualizar no VDP10064.

Esses tributos serão gerados automaticamente no faturamento, não sendo necessário cadastrar uma configuração fiscal.

**VDP0746 - Faturamento Manual** :

Incluído no VDP0746 na tela NF Referência a nova opção 'Compra governamental' com o tipo G, para que possa ser referenciado uma nota fiscal de saída nos casos onde é necessário gerar a tag refDFeAnt - Chave de acesso do documento fiscal anterior.

Essa opção deverá ser utilizada no caso de emissão de nota como o Tipo de Operação Governamental(tpOperGov) 2=Recebimento do pagamento com fornecimento já realizado ou 3=Fornecimento com pagamento já realizado;

No caso do tpOperGov = 2 deverá referenciar apenas uma nota fiscal com compra governamental emitida anteriormente com o tpOperGov = 1. Nessa nota pode ter apenas os novos tributos da reforma CBS, IBS_UF e IBS_MUN. E na configuração precisa ser informado o CFOP para pelo menos um dos tributos.

No caso do tpOperGov = 3 deverá referenciar uma ou mais notas fiscais com compra governamental emitida anteriormente com o tpOperGov = 4

Criado os novos campos de compra Governamental, na tela Informações complementares da NF-e:

Opções do zoom do campo **Tipo Ente Governamental** : 1-União, 2-Estado, 3-Distrito Federal, 4-Município, 5-Consórcio Publico, 6-Comitê Gestor do IBS

**VDP20000 - Pedidos** :

Incluído no VDP20000 os novos campos de compra Governamental, nas Informações complementares da NFe

Opções do campo **Tipo Ente Governamental** : 1-União, 2-Estado, 3-Distrito Federal, 4-Município, 5-Consórcio Publico, 6-Comitê Gestor do IBS

Inclusão do novo Tipo de referência "Compra Governamental", para esses casos deve ser informado uma nota fiscal de saída.

**VDP0745 - Faturamento automatico**

Alterado VDP0745 para gravar os novos campos tipo_ente_gov, pct_red_gov e tipo_oper_gov da tabela **PED_INFO_NF_E** na tabela **FAT_INFO_NF_E.**

**Calculo dos tributos:**

Alterada a função de calculo dos tributos (vdpr57) considerando as validações da NT e Conforme Art. 473, § 1o e seus Incisos I, II, III e IV e Art. 372 da LC 214/2025.

Portanto em 2026 serão calculados os tributos CBS, IBS_UF e IBS_MUN com seus respectivos valores, e a partir de 2027 serão gerados a soma dos tributos conforme o Tipo do ente governamental.

**VDP40005 - Consulta da nota fiscal:**

Incluído no VDP40005 os novos campos de compra Governamental, nas Informações complementares da NFe

Os campos referente a Compra governamental não podem ser alterados pois afetam o calculo dos tributos.

**VDP40003/VDP20029 - Envio para histórico:**

Alterado os programas de envio para histórico para prever os novos campos relacionados a compra governamental.

**OBF40000/VDP9202 - Painel da NF-e**

Alterado OBF40000/VDP9246 para gerar os novos grupos de compra governamental: gCompraGov e gTribCompraGov conforme layouts NT 2025.002 v 1.40 na NF-e

**VDP60000 - Painel da NFCom**

Alterado VDP60000 para gerar os novos grupos de compra governamental: gCompraGov e gTribCompraGov conforme layouts NT 2025.001 v 1.14a na NFCom

- **Nota 2025.002 - RTC - versão 1.40**

**Grupo DFeReferenciado.**

Devido as alterações na regra de validação VC02-14, passa a ser proibido o referenciamento da Nota na tag “refNFe” na devolução, devendo referenciar no grupo “DFeReferenciado”.

Foi alterado as funções de envio do xml da NF-e, para que verifique se possui a referencia a nível de item, mesmo para notas de origem "WMS", e caso o item tem mais de uma nota referenciada a NF-e ficará com status 9 no OBF40000 - Painel da NF-e, ficando a mensagem de erro:

**"Nota fiscal de devolução ou débito, não permitido referenciar mais de uma nota por item, conforme Nota Técnica 2025.002 versão 1.40"**

Sendo necessário ajustar os dados na origem da nota, seja no faturamento ou outro módulo.

Para notas de devolução incluídas pelo VDP0746 é preciso informar a sequencia do item da nota de entrada, para isso pode ser utilizado um dos parâmetros abaixo para que a tela onde será informada a sequencia do item será aberta após informar os dados do item:

**LOG00086** em **PROCESSO** **SAIDAS** > **FATURAMENTO** > **SOLICITAÇÃO** **FATURAMENTO** > **Grupo fiscal de naturezas que utilizam IPI da nota fiscal de entrada** - **grp_fisc_ipi_entrada_dev_forne**

**LOG00086 em PROCESSO SAIDAS> FATURAMENTO> DEVOLUÇÃO A FORNECEDOR> Consistir saldo da nota fiscal de entrada na devolução a fornecedor - consis_saldo_nf_entrada_devol**

Para notas de débito tipo 03 - Débitos de notas fiscais não processadas na apuração, foi ajustado a tela para informar a nota referenciada, onde não é obrigatório informar a sequencia do item da NF referenciada e caso seja informada, ficará gravado no faturamento, porém no xml não será enviado.

Para notas de débito tipo 04 - Multas e juros é obrigatório informar a sequencia do item da nota fiscal referenciada.

**Campo cIndOp - Código Indicador do local da operação de fornecimento:**

**VDP10106** - Cadastrar o Código Indicador de operação que é gravado na tabela vdp_codigo_ind_operacao. [Cadastro Código Indicador da Operação - VDP10106](https://tdn.totvs.com/pages/viewpage.action?pageId=983809653)

**VDP0746** - Alterado para informar o Código de Indicador de operação na tela de Informações Complementares da NF-e, gravando os dados na tabelafat_info_nf_e.

**VDP20000 -** Alterado para informar o Código de Indicador de operação na tela de Informações Complementares da NF-e, gravando os dados na tabela ped_info_nf_e:

**VDP0745** - Alterado para efetivar o novo campo cod_ind_oper da ped_info_nf_e na fat_info_nf_e ao faturar o pedido.

**VDP40005** - Alterado para mostrar o novo campo Código de Indicador de operação na tela de Informações da NF-e ao consultar os dados da nota/NFe

**VDP20029 -** O programa foi alterado para enviar o campo novo para histórico.

**VDP40003 -** O programa foi alterado para enviar o campo novo para histórico.

**OBF40000/VDP9202 -** O programa foi alterado para gerar a Tag cIndOp.

Quando informado os códigos 010104 ou 010105, o **"Local da Retirada"** deve ser gravado no faturamento.

Para gerar o grupo **"Local da Retirada"** na NF-e, configure o parâmetro **LOG00086 Processos Saídas - Faturamento - Faturamento- “Processo onde serão cadastradas informações do local de retirada da NF”** . Após a configuração, os dados poderão ser informados no **VDP20000 (Pedido de Venda)** , **VDP0746 (Solicitação de Faturamento)** ou na **Ordem de Montagem** , conforme o processo definido. Essas informações serão utilizadas na geração do grupo **"Local da Retirada"** da nota fiscal.

**Campo adRemIS - Aliquota especifica por unidade de medida:**

Alterado **OBF40000/VDP9202** para fazer os ajustes necessários alterando a tag pISEspec para adRemIs.

## Pacote 10/08

**Funcionalidades Principais:**

- **Evento 211110: Solicitação de Apropriação de crédito pres** **umido pelo Emitente**

Foram liberadas as alterações para atender prever a geração do **Evento 211110: Solicitação de Apropriação de crédito pres** **umido pelo Emitente** conforme NT - 2025.002 - V1.40

**OBF26300 - Inclusão de Eventos**

Alterado para permitir a inclusão do evento 211110 pelo emitente/faturamento.

**OBF26200 - Central de Eventos**

Alterado para fazer o envio do evento 211110 pelo emitente (FAT) conforme o mesmo layout do evento 211110 de entradas (SUP).

**Esta alteração deve ser baixada em conjunto com as alterações de Obrigações Fiscais sobre o mesmo assunto:**

**DBACKRTLGX-5391 DT OBF26000 - Cockpit Eventos - Adequações NT 2025.002 v1.40/v1.50**

- **Demais ajustes e manutenções:**

**NFS-e:**

Necessidade de atender as atualizações do **TSS (TOTVS Sped Service)** referentes à emissão de **NFS-e no padrão nacional** , no contexto da **Reforma Tributária** .

A atualização contempla a alteração da versão do layout da Nota Fiscal de Serviço Eletrônica, que passa a utilizar o sufixo_RT— por exemplo:2.00_RT.

DT - [DMANFATMANUT-16197 DT Aumento da versão da NFS-e devido a NFS-e nacional](https://tdn.totvs.com/x/fDQbQ)

## Pacote 31/08

Alterados os programas abaixo para atender as Notas Técnicas **NT2025.002 versão 1.40** , para gerar o novo grupo de incentivo da Zona Franca/Área de Livre Comércio, e **NT2026.002** , ajustes na NFCOM e também a **automatização da nota de débito de multas e juros** .

**Funcionalidades Principais**

Nota Técnica 2025.002 - Versão 1.40 - Grupo gALCZFMCBS

Alterado processos para permitir a geração do novo grupo **gALCZFMCBS** :

**VDP0696/VDP10068 - Configuração fiscal**

Inclusão do campo **Tipo Alíquota ALCZFM** para indicar o tipo da alíquota do incentivo, conforme descrito pela NT.

O campo foi criado como um adicional do tributo CBS ao qual se refere o incentivo.Para que o mesmo fique disponível é necessário utilizar a opção 'Atualizar Fiscal'do **VDP0692/VDP10064.**

**MAN10021 - Cadastro de itens - Comercial**

Inclusão do campo **Numero Processo Suframa**

**VDP0746 - Faturamento manual**

Inclusão dos campos "Tipo ALCZFM" e "Processo SUFRAMA" na Aba Tributos/Benefícios, permitindo informar o campo quando for Manual.

No faturamento automático vai carregar os dados da configuração fiscal (Tipo ALCZFM) e do item automaticamente (Processo SUFRAMA).

**VDP40005 - Consulta da Nota Fiscal**

Inclusão dos campos "Tipo alíquota ALCZFM" e "Número processo Suframa" na opção Itens / Fiscal.

**VDP40003 - Envio de Notas Fiscais para Histórico**

Programa foi alterado para enviar os novos campos para histórico.

**OBF40000 - Painel NF-e**

Alterado envio da Nf-e para prever o novo grupo **gALCZFMCBS** e a tag **<ISUFEmit>** (suframa do emitente) atrelada ao grupo.

Para que seja gerado o novo grupo e a nova tag a configuração fiscal deve ter o novo adicional do CBS informado (Tipo Alíquota ALCZFM), as informações do Suframa para o emitente e o cliente, e o número do processo do Suframa cadastrado para os itens que tenham processo no Suframa (man10021).

Desta forma, ao faturar será gerado o tributo CBS_REG com a tributação que seria devida caso não houvesse o incentivo, gerando assim os dados do novo grupo:

Nota Técnica 2026.002 - NFCOM

Alterados processos para atender os itens abaixo da **NT 2026.002** da **NFCOM** :

- Novo motivo de substituição:6 - Regime especial
- CNPJ Cobrança Terceiro

**VDP0746 - Faturamento manual**

O programa foi alterado para prever um novo motivo de substituição:6 - Regime especial.

O programa foi alterado, na tela de itens **VDP0782** , para inclusão do campo **"CNPJ Cobr Terceiros"**

**VDP40005 - Consulta de Nota Fiscal**

O programa foi alterado para mostrar na tela de Itens o campo novo "CNPJ Cobrança Terc NFCOM":

**VDP40003 - Envio de nota fiscal para histórico**

O programa de histórico foi ajustado para contemplar o campo **cnpj_cobr_terc** , realizando a transferência dos dados da tabela **fat_nf_item** para a tabela **fat_nf_item_hist** .

**VDP60000 - Painel NFCOM**

O programa foi alterado para gerar a tag **CNPJCobrTerc** quando houver conteúdo informado.

Automatização - Nota de débito - Multas e Juros

Foi implementado a opção de geração de nota fiscal de débito de multas e juros a partir de um título, no **FIN10210** poderá ser consultados os títulos que possuem multas e juros e também os novos tributos da reforma tributária, e selecionar o registro que deseja gerar a nota fiscal de débito.

Foi disponibilizada uma nova tela **VDP10302** para cadastro de parâmetros de notas de débito, permitindo a definição e o gerenciamento das regras que orientam a emissão automatizada de encargos por atraso (multas e juros). O sistema passou a contar com validações automáticas durante a parametrização, garantindo a consistência das informações antes da persistência dos dados:

**Natureza de Operação:** Permite a busca facilitada e permite a inclusão apenas de naturezas que não gerem duplicata fiscal/financeira.

**Série e Subsérie:** Restringe a seleção exclusivamente para documentos habilitados para faturamento de produto/serviço (tipo SOLPRSV).

**Condição de Pagamento:** Valida e aceita apenas condições de pagamento configuradas para não gerar duplicatas.

**VDP10302 - Parâmetros nota de débito**

No programa **FIN10210** quando acionado a opção 'Gerar Notas ', será chamada uma função do vendas que irá fazer os seguintes passos:

- Ler os dados da nota fiscal de origem.
- Ler os dados do cadastro de parâmetros no programa **VDP10302** .
- A natureza de operação informada no **VDP10302** deverá ter os tributos da reforma (CBS, IBS_MUN, IBS_UF) vinculados no VDP10059. E não é necessário ter uma configuração fiscal, o cálculo dos tributos será com base nos dados da nota de origem.
- Com base na nota fiscal de origem, irá verificar o valor total dos itens e valor total de juros e multas do titulo que foi selecionado, irá calcular o valor do item proporcional e será feito o rateio do valor juros e multas para cada item.
- Será calculado o valor dos tributos utilizando a configuração fiscal de cada item/tributo da nota fiscal de origem.
- Irá gerar uma nova nota fiscal com a finalidade da NF-e = 6 (Nota de débito) e tipo de débito = 4 (Multas e Juros).
- A nota fiscal ficará com status F - Faturado no **FIN10210** , e a mesma deverá ser enviada para a Sefaz através do **OBF40000** .
- Após a nota ser autorizada na Sefaz, o status será alterado para A- Autorizado
- Em caso de cancelamento de nota, será atualizado o status para C- Cancelado.
- Caso seja utilizado uma empresa controladora do CRE (parametro empresa_ctrl_cre no LOG00086), o envio para a Sefaz e cancelamento da NF-e devem ser feitos na empresa origem da nota fiscal.

Abaixo um exemplo de uma nota fiscal e o rateio calculado pelo sistema:

**.card { width: 80%; margin-left: 30px; box-shadow: 0px 0px 14px #CCC; padding: 15px 30px; } .card h1 { font-weight: bold; border-bottom: 1px solid rgb(255,153,0); color: black; margin-bottom: 25px; } .card p { color: gray; }**

**IMPORTANTE! A atualização automática do status da nota de debito para Autorizado do programa FIN10210 será feita apenas no painel da NF-e - OBF40000, caso ainda utilize o VDP9202, orientamos a migração para o Painel da NF-e para usufruir das funcionalidades e melhorias liberadas para a NF-e.**

**VDP10900 - Programa de ajuste de base**

Foi criada uma opção para realizara integração de notas retroativas (com IBS/CBS) para o financeiro, será considerado as notas fiscais que possuem valores para os tributos CBS, IBS_MUN e IBS_UF, independente se soma ou não no total da nota.

Esta opção vai criar a tabela CRE_PREVISAO_IBS_CBS e vai solicitar um período em tela.

Para mais detalhes verificar também o **Guia de Uso do Financeiro** :

[Guia de Uso - Reforma Tributária - Financeiro#-2132490262](https://tdn.totvs.com/pages/viewpage.action?pageId=1009450308#GuiadeUsoReformaTribut%C3%A1riaFinanceiro--2132490262)

Demais ajustes e manutenções

**VDP0746** - Ajustes no cálculo do **valor do diferimento** e da gravação dos dados da **fat_info_nf_e** .

**OBF40000** - Ajustes grupo de **estorno de crédito.**

## Pacote 21/09

Alterados os programas abaixo para atender às adequações da **Reforma Tributária** .

**Funcionalidades Principais**

Nota Técnica 005 versão 1.1 - NFS-E Grupo compra governamental

Alterado os processos abaixo para permitir a geração do grupo de Compra Governamental para a emissão da NFS-e conforme a NT 005 versão 1.1:

Os novos tributos CBS_GOV, IBS_UF_GOV, IBS_MUN_GOV, já foram disponibilizados no pacote de 20/07, nas alterações da NFe referente a Compra Governamental.

Esses tributos serão gerados automaticamente no faturamento, não sendo necessário cadastrar uma configuração fiscal.

Caso ainda não tenha utilizado, para que os novos tributos fiquem disponíveis é necessário processar a opção atualizar no VDP10064.

Incluído no VDP0746 na tela NF Referência a nova opção 'Compra governamental' com o tipo G, para que possa ser referenciado uma nota fiscal de saída nos casos onde é necessário gerar a tag refDFeAnt - Chave de acesso do documento fiscal anterior.

Essa opção deverá ser utilizada no caso de emissão de nota como o Tipo de Operação Governamental(tpOperGov) 2=Recebimento do pagamento com fornecimento já realizado ou 3=Fornecimento com pagamento já realizado;

No caso do tpOperGov = 2 deverá referenciar apenas uma nota fiscal com compra governamental emitida anteriormente com o tpOperGov = 1. Nessa nota pode ter apenas os novos tributos da reforma CBS, IBS_UF e IBS_MUN. E na configuração precisa ser informado o CFOP para pelo menos um dos tributos.

No caso do tpOperGov = 3 deverá referenciar uma ou mais notas fiscais com compra governamental emitida anteriormente com o tpOperGov = 4

Criado os novos campos de compra Governamental, na tela Informações complementares da NFS-e:

Opções do zoom do campo **Tipo Ente Governamental** : 1-União, 2-Estado, 3-Distrito Federal, 4-Município, 5-Consórcio Publico, 6-Comitê Gestor do IBS

Incluído no VDP20000 os novos campos de compra Governamental, **Tipo Ente Governamental** e **Percentual Redução** , nas Informações NFSe no folder **Adicionais**

Opções do campo **Tipo Ente Governamental** : 1-União, 2-Estado, 3-Distrito Federal, 4-Município, 5-Consórcio Publico, 6-Comitê Gestor do IBS

Alterado VDP0745 para gravar os novos campos tipo_ente_gov, pct_red_gov da tabela **PED_INFO_NFS_E** na tabela **FAT_INFO_NFS_E.**

Alterada a função de calculo dos tributos (vdpr57) para ler as informações da compra governamental da **fat_info_nfs_e,** quando houver dados. Os cálculos foram considerados da mesma forma que faz para a NFe, conforme dados da NT.

Incluído no VDP40005 os novos campos de compra Governamental, nas Informações complementares da NFSe

Os campos referente a Compra governamental não podem ser alterados pois afetam o calculo dos tributos.

Alterado os programas de envio para histórico para prever os novos campos relacionados a compra governamental.

Alterado OBF50000 para gerar a tag de Tipo de Entidade Compra Governamental dentro do grupo IBSCBS.

No layout único é gerada a TAG **tpentegov.**

No layout nacional é gerado o grupo **gRefNFSe/refNFSe** e a TAG **tpEnteGov** .

NT 2026.002 - NFCOM - Grupo gALCZFMCBS

Necessidade de atender os itens abaixo da NT 2026.002 da NFCOM:

- Novo campo Inscrição Suframa do Emitente
- Novo grupo gALCZFMCBS

Inclusão do campo Tipo Alíquota ALCZFM para indicar o tipo da alíquota do incentivo.

O campo foi criado como um adicional do tributo CBS ao qual se refere o incentivo.Para que o mesmo fique disponível é necessário utilizar a opção 'Atualizar Fiscal'do **VDP0692/VDP10064.**

**VDP0696**

**VDP10068**

Inclusão dos campos "Tipo alíquota ALC/ZFM" na opção Itens / Fiscal.

Programa foi alterado para enviar os novos campos para histórico.

Alterado para prever o novo grupo **gALCZFMCBS** e a tag **<ISUFEmit>** (suframa do emitente) atrelada ao grupo.

Para que seja gerado o novo grupo e a nova tag a configuração fiscal deve ter o novo adicional do CBS informado (Tipo Alíquota ALCZFM), as informações do Suframa para o emitente e o cliente.

Desta forma, ao faturar será gerado o tributo CBS_REG com a tributação que seria devida caso não houvesse o incentivo, gerando assim os dados do novo grupo:

Contabilização - CBS/IBS

Alterados processos para atender a contabilização para os novos tributos da reforma tributária.

**IMPORTANTE:**
Ao baixar este pacote/issue deverá ser executado o vdp5970 com a Opção 7 (vdp_cctbl_hist) para que sejam atualizados os controles de acesso, mesmo que não sejam alterados os cadastros das contas contábeis.

Os programas foram alterados para contemplar os campos **CLASSIFICAÇÃO TRIBUTÁRIA** e **NBS** .

A classificação tributária estará habilitada somente para os tributos da reforma tributária(CBS, IBS_UF, IBS_MUN e IS).

O NBS estará habilitado somente para os tributos ISS_REC, ISS_RET e ISS_RET_DUPL.

Estes novos campos serão considerados na tabela CTR_ACESSO.

Foi criada uma nova finalidade chamada " **MERCADORIA_LIQUIDA** ". Esta finalidade poderá ser marcada como "principal" e terá o mesmo tratamento da finalidade "MERCADORIA".

**IMPORTANTE:**
No ano de 2026 como não haverá recolhimento efetivo dos novos tributos da RT, as contas de débito e crédito devem ser as mesmas, ou deverá haver lançamento manual na contabilidade para zerar os saldos das contas. No ano de 2027, com o devido recolhimento, seja pelo próprio fornecedor ou pelo adquirente, os lançamentos de contrapartida serão feitos pelos demais processos (Contas a receber/Contas a pagar).

Alterada a contabilização para considerar os novos campos, **CLASSIFICAÇÃO TRIBUTÁRIA** e **NBS,** no controle de acesso ao buscar as contas contábeis.

O programa também foi alterado para gerar lançamentos pelo **valor líquido** na nova finalidade " **MERCADORIA_LIQUIDA** ", permitindo que seja contabilizado o valor líquido da mercadoria, independentemente do parâmetro utilizado no lançamento da conta de MERCADORIA ( **valor_lancto_ctb_merc_serv** ).

Além disso, o programa foi alterado paraverificar se foi executada a atualização do controle de acesso, considerando os novos campos da tabela, antes do início da contabilização.

Alterada a integração com o Contas a Receber para ler corretamente as contas considerando os novos campos de **CLASSIFICAÇÃO TRIBUTÁRIA** e **NBS** , quando houver.

Alterado programa de ajuste de cálculo de retenção no CRE para ler corretamente as contas considerando os novos campos de **CLASSIFICAÇÃO TRIBUTÁRIA** e **NBS** , quando houver.

DFeReferenciado para notas fiscais de retorno embalagem/vasilhame

Ajustado o Faturamento para gerar o grupo **DFeReferenciado** nas NF-e de retorno de embalagem/vasilhame, emitidas com a finalidade **4 – Devolução** , passando a referenciar, a nível de item, a **nota fiscal de entrada** correspondente.

O Faturamento passa a gravar as informações de referência na tabela **fat_nf_refer_item** , com base nos dados da tabela **fat_retn_item_nf** . Dessa forma, no envio da NF-e à Sefaz, será gerado o grupo **DFeReferenciado** para os respectivos itens.

Para evitar a **Rejeição 1010** , o relacionamento com a **nota fiscal de venda** não será mais gerado na tag **NFref** , no nível do cabeçalho da NF-e, pois não é permitido informar documento fiscal referenciado simultaneamente no **cabeçalho** e nos **itens** da NF-e.

DT: [VDP0742/VDP0746 -DFeReferenciado para notas fiscais de retorno embalagem/vasilhame](https://tdn.totvs.com/x/n6LDQg)

Demais ajustes e manutenções

- **DBACKRTLGX-6837:** Atualização da descrição doVDP10900referente à integração com o financeiro para contemplar os valores de **CBS/IBS** .
- **DT DMANFATMANUT-17862:** Correção da determinação e gravação da finalidade **4 — Devolução** da NF-e em operações de retorno de beneficiamento, industrialização e embalagem.
- **DT DMANFATMANUT-18296:** Tratamento de valores nulos de juros e multa no cálculo do preço unitário dos itens da nota fiscal de débito.

## Pacote 12/10

Alterados os programas abaixo para atender às adequações da **Reforma Tributária** .

**Funcionalidades Principais**

Ajustes e manutenções

- **DBACKFATLGX-192 -** Ajuste do indicador de conta principal para a correta contabilização do PIS e COFINS a recolher

- DT [30529921 DBACKFATLGX-192 DT - VDP0768/VDP40030 PIS e COFINS não lançados na contabilização, identificação da conta principal](https://tdn.totvs.com/pages/viewpage.action?pageId=1131838386)

- **DBACKFATLGX-222 -** Ajuste em relação a integração com EAI no envio/retorno da nota para a SEFAZ

- DT [30434467 - DMANFATMANUT-18389 DT OBF40000 - Não está fazendo integração EAI](https://tdn.totvs.com/pages/viewpage.action?pageId=1131812134)

## Pacote 26/10

Alterados os programas abaixo para atender às adequações da **Reforma Tributária** .

**Funcionalidades Principais**

Nota Técnica 2025.002 - Monofásico

Foram realizados ajustes nos programas de cadastro e manutenção do Produto ANP para atender à Reforma Tributária, contemplando o grupo de tributação monofásica do IBS e da CBS para produtos regulados pela ANP.

Foram criados os tributos IBS_MONO_RET e CBS_MONO_RET, criados adicionais para estes tributos e as fórmulas 1, 2, 3 e 4 para ambos os tributos.

Para que estas informações estejam disponíveis no sistema, é necessário processar o " **Atualiza_fiscal** " do VDP0692/VDP10064.

É necessário verificar em qual cenário os itens se enquadram e configurar os tributos e fórmulas, abaixo pode ser verificado quais fórmulas utilizar para cada grupo correspondente no xml da NF-e

- **VDP0696 - Configuração fiscal**

Alterado para permitir os novos tributos, seus respectivos adicionais e fórmulas.

- **VDP10068 - Configuração fiscal**

Alterado para permitir os novos tributos, seus respectivos adicionais e fórmulas.

Foi criado o programa **VDP10303** para realizar o cadastro do Produto ANP, contemplando os novos campos relacionados à **Reforma Tributária** e replicando as regras já existentes no programa **OBF1205** , na opção **Cadastro Produto** .

O programa **VDP10303** deverá ser incluído no **Menu** , permitindo sua execução de forma independente ou por meio do programa **OBF1205** , na opção **Cadastro Produto** .

- **VDP10303 - Cadastro Produto ANP**

Adicionado a tela para Cadastro da Origem do Combustível

Adicionado a opção para chamar a tela **SUP34218 - Cadastro de Alíquota de ICMS**

- **VDP0746 - Faturamento:**

Alterado para calcular os tributos CBS_MONO_RET e IBS_MONO_RET conforme as fórmulas e conforme os campos novos na OBF_PRODUTO_ANP.

Exemplo simbólico utilizando a fórmula 3:

- **VDP40005 - Consulta da nota fiscal**

Alterado para mostrar os campos novos na tela de informações fiscais

- **VDP40003 - Envio das notas fiscais para histórico**

Alterado para enviar os campos novos para histórico.

Alterado para gerar as tags do grupo gIBSCBSMono quando houver conteúdo informado.

DFeReferenciado para notas fiscais de retorno embalagem/vasilhame

Realizamos ajustes e manutenções nos programas envolvidos na geração do DFeReferenciado para notas fiscais de retorno de embalagem/vasilhame, visando garantir a geração correta das referências fiscais e evitar rejeições no envio dos documentos à SEFAZ.

- **DBACKRTLGX-7381:** VDP0742– Ajuste para gerar uma sequência de item para cada nota fiscal de origem no retorno automático de embalagem/vasilhame pelo Controle de Terceiros.

- DT [DBACKRTLGX-7381 DT - VDP0742– Gerar uma sequência de item para cada nota fiscal de origem no retorno automático de embalagem/vasilhame pelo Controle de Terceiros](https://tdn.totvs.com/x/QAENR)

- **DBACKFATLGX-186 -** Ajuste para validar corretamente o saldo da nota origem informada na referência de devolução do item.

- DT [30526510 DBACKFATLGX-186 DT - VDP0746 - Nota de retorno de embalagem - Quantidade do item maior que quantidade de saldo rejeitado na inspeção.](https://tdn.totvs.com/x/E_zAQw)

- **DBACKFATLGX-200 -** Ajuste no VDP0746 para gerar a referência de devolução do item no retorno de terceiros.

- DT [30494393 DBACKFATLGX-200 DT - VDP0746 - Rejeição 321 - Não está gerando o DFEreferenciado para notas de retorno de terceiros](https://tdn.totvs.com/x/-vjAQw)

2025

## Pacote 30/06

- **Funcionalidades Principais**

**Cadastro de CST para os novos tributos:**

Os programas VDP0440/VDP10061 foram alterados para inclusão dos novos tributos, para atender a Reforma Tributária: Imposto sobre Bens e Serviços (IBS) Municipal e Estadual, a Contribuição sobre Bens e Serviços (CBS) e o Imposto Seletivo (IS).

A tabela dos novos CST's está disponível no portal da NF-e: [https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=dAgqLmXh/eA=](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=dAgqLmXh/eA=)

No VDP10900 foi disponibilizada uma opção para fazer uma carga inicial dos CSTs com base na tabela disponibilizada no Portal da NF-e.

**Configuração dos novos tributos**

O VDP0692/VDP10064 foi alterado para atender as seguintes necessidades:

Foram criados os tributos:

IS - Imposto Seletivo

CBS - Contribuição sobre bens e serviços

IBS_UF - Imposto sobre Bens e Serviços Estadual

IBS_MUN - Imposto sobre Bens e Serviços Municipal

CBS_CR_PRE - CBS crédito presumido

IBS_CR_PRE - IBS crédito presumido.

Para que os mesmos fiquem disponíveis é necessário utilizar a opção 'Atualizar Fiscal' do **VDP0692/VDP10064** .

Todos os tributos são criados com as chaves de configuração desmarcadas, é necessário marcar e configurar conforme necessidade através do **VDP0692/VDP10064** .

Para verificar a ordem de busca da configuração fiscal consulte o artigo [Cross Segmentos - Linha Logix - FAT - Ordem de busca da configuração fiscal no momento do faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047605573-Cross-Segmentos-Linha-Logix-FAT-Ordem-de-busca-da-configura%C3%A7%C3%A3o-fiscal-no-momento-do-faturamento)

Na aba Operação fiscal saída podem ser informadas as naturezas de operação que serão utilizadas no faturamento para cálculo dos novos tributos.

Serão criadas 3 fórmulas padrões para os tributos **CBS, IBS_UF e IBS_MUN** no **VDP0693/VDP10065** , e futuramente conforme necessário serão criadas novas fórmulas, também é possível criar fórmulas especificas caso desejar fazer algum teste.

Para o **IS** , não foram criadas fórmulas nesse momento, será previsto em release futura considerando que a cobrança deste tributo será apenas em 2027.

É necessário vincular os novos tributos na natureza de operação que será utilizado na emissão das notas - **VDP0050/VDP10059** **.** Caso já não tenha sido feito através do **VDP0692/VDP10064.** .

Após vincular o tributo à natureza de operação, deverá ser cadastrado uma configuração fiscal no VDP0696/VDP10068:

- O adicional 'Cod class trib' dos tributos **CBS, IBS_UF e IBS_MUN** deverá ser previamente cadastrado noSUP34260 - Cadastro de Classificação tributária.
- Os campos Cod Class trib e Tributação precisam ser informados para os 3 novos tributos **CBS, IBS_UF e IBS_MUN** com a mesma informação, pois no xml da NF-e é gerado apenas uma vez a tag, ao gerar o xml é considerado o Cod Class trib e Tributação do tributo IBS_UF.
Os tributos 'CBS_CR_PRE' e 'IBS_CR_PRE' tem o adicional 'Class Trib Presum', que é a classificação tributária para o crédito presumido. O campo é não obrigatório e aceita qualquer valor pois a tabela ainda não foi definida pela legislação. Assim que for definido, passará a consistir com o novo cadastro ou com o cadastro geral de classificação tributária, se for o caso.

- As alíquotas utilizadas na configuração devem ser de acordo com a legislação vigente e o cenário da empresa, orientamos que seja verificado junto a área fiscal da empresa.

Foi criado o parâmetro no LOG00086: Processo Saídas > Faturamento > Nota fiscal eletrônica: "Data de início para cálculo dos tributos da reforma tributária" ( **data_inicio_ref_trib)** que deverá ser informado para indicar a partir de que data será calculado os novos tributos na nota fiscal e também a partir dessa data será gerado as novas tags no xml da NF-e.

**Tributação Regular**

Para atender a criação do novo grupo de tributação regular na NF-e,

foram criados os tributos CBS_REG, IBS_MUN_REG e IBS_UF_REG, que são tributos automáticos calculados pelo sistema.

Além disso, foram criados os novos campos adicionais "TRIBUTACAO_REG" e "COD_CLASSIF_TRIB_REG" para os tributos CBS, IBS_MUN e IBS_UF.

Esses novos campos aparecem da tela de informações adicionais dos tributos, no VDP0696/vdp10068 - configuração fiscal, para serem inclusos quando houver tributação diferenciada, onde deverá ser informada qual seria a tributação regular aplicada.

Verificar na tabela cClassTrib para quais situações ser enviados o grupo de tributação regular, indicador 'ind_gTribRegular a tabela está disponível no portal da NF-e: [https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ix44jDLyQog=](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ix44jDLyQog=)

Exemplo de configuração fiscal:

Consulta da nota fiscal com registros de tributação regular:

**Consulta da nota fiscal**

Foram alterados os programas de consulta da nota fiscal para mostrar os novos campos referente aos tributos da reforma tributária.

VDP40005 - Consulta da nota, opção Itens - Fiscal VDP90207- Incluso novo campo Código da classificação tributária.

VDP0752 - Opções Itens - Aba Tributos/benefícios Incluso novo campo Código da classificação tributária.

**Relatórios**

O Relatório de Resumo de faturamento por representante e cliente **VDP5243** , foi alterado para passar a demonstrar os tributos IBS_UF e IBS_MUN calculados na nota fiscal.

## Pacote 11/08

**Funcionalidades Principais**

- **Notas Finalidade crédito e débito**

Alterações no faturamento para atender as notas com finalidade crédito, débito e novo grupo para referenciar notas.

Foram criados dois novos parâmetros no LOG00086 - Processos Saídas - Faturamento - Nota fiscal Eletrônica: "Grupo fiscal para notas de débito" e "Grupo fiscal para notas de crédito", onde deverão ser informado um código de grupo fiscal e depois no VDP10005 cadastrar as naturezas de operação que serão utilizadas para cada tipo de nota no respectivo grupo.

Alterado programa de faturamento manual VDP0746 para permitir informar a sequencia do item da nota referenciada.

Se o tipo da nota de referência for igual a **A - Manual - Nf Entrada** e a natureza de operação estiver nos grupos fiscais de débito ou credito ( **grupo_fiscal_nota_debito** ou no **grupo_fiscal_nota_credito) o** u o tipo de referência for igual a **D -Devolução** , abrirá a tela de referência por item para informar os dados da nota de entrada/AR.

Se o tipo de nota de referência for igual a **M - Manual - NF Saída** e a natureza de operação estiver nos grupos fiscais de débito ou credito ( **grupo_fiscal_nota_debito** ou **grupo_fiscal_nota_credito** no log0087), abrirá a tela de referência por item para informar os dados da nota de saída relacionada.

Na tela de Informações complementares da NF-e foram incluídos dois campos novos Tipo de Crédito e Tipo de Débito valor deve ser informado para geração do campo no XML conforme Nota técnica.

Essas alterações foram feitas para atender os tipos de notas com finalidade Débito ou Crédito conforme a NT 2025.002

Tela de referência por item da nota fiscal - informar item da nota de entrada/AR.

Tela de referência por item da nota fiscal - informar item da nota de saída.

Tela de Informações Complementares NFE.

O envio da NF-e com finalidade debito e crédito ainda não estão com as validações ativas na Sefaz, neste caso podem ser feito testes apenas na rotina de faturamento.

- **Envio de NF-e(xml)**

No **OBF40000/VDP9202** foram realizadas alterações nas funções que geram o xml para gerar as notas tags conforme layout da Nota Técnica 2025.002.

As novas tags serão geradas somente quando o parâmetro doLOG00086:Data de início para cálculo dos tributos da reforma tributária ( **data_inicio_ref_trib)** estiver informado data inferior a data corrente.

Neste pacote foram liberadas as alterações para atender os seguintes cenários de tributação do IBS/CBS:

| Tributado integralmente | CST 000 |
| --- | --- |
| Tributado com redução de alíquota ( com tributação regular)* | CST 200 |
| Tributado com diferimento parcial ou total | CST 510 |
| Tributação imune e não incidência | CST 410 |
| Tributação suspensa (com tributação regular) * | CST 550 |

*Verificar na tabela cClassTrib para quais deverão ser enviados o grupo de tributação regular

Abaixo a relação de tributações e tipos de notas que ainda **não** foi implementado, será liberado em pacote futuro:

| Tributação monofásica |
| --- |
| Tributação crédito presumido |
| Notas com finalidade débito e crédito |
| Grupo de Compra governamental |
| Grupo Pagamento Antecipado |
| Grupo Transferência de Crédito |
| Grupo Fornecimento para Zona Franca de Manaus |
| Eventos |
| DANFE (com os novos tributos) |

- **Importação de notas via arquivo texto - VDP0002**

Foi adequado o leiaute de importação notas via do arquivo texto, foi incluído os novos tributos CBS, IBS_MUN e IBS_UF. E também alterado o tamanho do campo referente ao protocolo de autorização e cancelamento da NF-e de 15 para 17.

**Alertamos que a alteração do campo protocolo impactou na posição dos campos posteriores, como data de recebimento do protocolo, forma de emissao, protocolo de cancelamento, série, tipo do documento, importante revisar os arquivos que serão importados.**

O leiaute atualizado está disponível no link: [Importação Notas Fiscais - VDP0002](https://tdn.totvs.com/pages/viewpage.action?pageId=284464244)

**IMPORTANTE!**

É preciso estar com o TSS atualizado no último pacote liberado, assim como os schemas para realizar os testes. Verifique no link as atualizações liberadas pelo TSS: [Cross Segmentos - Linha Logix - NFE - Atualização do TOTVS Service SOA para a correta utilização do OBF40000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025034751-Cross-Segmentos-Linha-Logix-NFE-Atualiza%C3%A7%C3%A3o-do-TOTVS-Service-SOA-para-a-correta-utiliza%C3%A7%C3%A3o-do-OBF40000)

Fiquem atentos as datas de Implementação em base de testes e produção conforme divulgado na Nota técnica 2025.002 v1.20

Acesse aqui a Nota Técnica completa: [Portal da nota fiscal eletrônica](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY=)

## Pacote 22/09

**Funcionalidades Principais:**

- Prever a nova tag vIBS, conforme NT 2025.002 v 1.20

Alterado a geração do xml para gerar a tag vIBS a nível de item.

- Sequência do item da nota no XML

Passou a ser gravado a sequência do item no XML, para ser utilizado no DFe Referenciado e demais obrigações fiscais e/ou outros módulos quando necessário.

A necessidade decorre do fato de existir o parâmetroOrdem de impressão dos itens da Danfe( **ordem_impr_item_danfe)** no LOG00087, que permite imprimir os itens no DANFE/XML de formas diferentes, alterando a sequência do item no XML em relação a sequência do item na nota (fat_nf_item). Assim, ao precisar referenciar a sequência do item no XML, a mesma pode divergir da sequência do item na nota, se o cliente utilizar o referido parâmetro diferente de 1 (sequência do item na nota fiscal).

Alteradas as tabelasfat_info_nf_e e fat_info_nf_eletr_historico criando nova coluna nitem_xml, conversor vdp02818.cnv. O novo campo gravará a informação da sequência do item da nota no XML.

No OBF40000, ao enviar a NF-e, passa a gravar a sequência do item no XML, e ao gerar a tag do DfeReferenciado, passa a utilizar o nitem_xml, se houver dados na tabela.

Para as notas em que não for encontrado o nitem_xml, será utilizada a sequência do item na nota fiscal.

Para notas que possuem notas de entrada como referência, será verificado se possui cadastro no SUP34221.

VDP40005, tela de informações da NF-e por item, alterado para visualizar a informação da sequência do item no XML.

VDP40003 - alterado envio os dados para histórico, para prever o novo campo.

- Ajustes na geração dos grupos de NfRef ou DfeReferenciado, relativas as alterações daNT 2025.002v1.20.

Alterações no VDP0746:

Ao informar nota de referência do tipo D - Devolução, e a natureza de operação constar no grupo fiscal de notas fiscais de devolução que utilizam valores da nota de entrada ( **grp_fisc_ipi_entrada_dev_forne** no LOG00087), abriráa tela de referência por item para informar asequência do item da nota de entrada/AR referenciado, sendo obrigatório que seja informada uma sequência e item válidos. Caso a natureza de operação não esteja no grupo citado, não abrirá a tela para informar a referência por item.

Ao informar nota de referênciado tipo M - Manual - NF Saída, e a natureza de operação constar no grupo fiscal notas de débito ( **grupo_fiscal_nota_debito** no LOG00087), abrirá a tela de referência por item para informar a sequência do item da nota de saída relacionada, não sendo obrigatório informar por item. Se informar, deverá ser uma sequência e item válidos.

Para as notas fiscais de finalidade **crédito** , deverá ser informada a referência na tela de nota de referência e não mais abrirá a tela para informar a referência por item.

Alterações no OBF40000:

Na geração do XML da NFe as notas de devolução passam a gerar a tag <Nfref> caso tenha informado a nota de referência e não tenha sido informado a referência por item ou <DfeReferenciado> caso tenha sido informada a referência por item.

As notas de crédito passam a gerar a tag <Nfref> se for informada a nota de referência. No caso de nota de crédito do tipo = 2 (Apropriação crédito presumido IBS sobre saldo devedor ZFM), não deve ser informada referência, para que não seja gerada a informação no XML.

As notas de débito, passam a gerar a tag <Nfref> caso tenha informado a nota de referência e não tenha sido informado a referência por item ou <DfeReferenciado> caso tenha sido informada a referência por item. Lembrando que para as notas de débito do tipo ”04-Multa e Juros” consistirá se o usuário informou corretamente a referência por item.

No caso das notas de débito do tipo ”03-Débitos de notas fiscais não processadas na apuração”, gerará sempre a tag <DfeReferenciado> com o nitem nulo, no primeiro item da nota. Hoje permite apenas uma nota de referência.

OBS: As notas de crédito e debito ainda estão em desenvolvimento, já foi implementado a geração das novas tags, porém ainda não conseguimos homologar todos os tipos de notas de crédito e débito.

- Código cCredPres - Classificação tributária Presumido no VDP10068/VDP0696

Implementada modificação nos programas **VDP0696** e **VDP10068** , direcionando o campo **Class Trib** **Presum** para buscar o **zoom/validação** na tabela obf_cad_cred_presumido, cadastro dessa tabela deverá ser feito através do programa OBF25200.

- Manutenções do pacote 11/08

Foram identificados algumas situações que foram liberadas no pacote de 11/08 e a correção está sendo disponibilizada neste pacote:

No OBF40000, ao fazer um envio da nota fiscal, ocorre erro no UPDATE de uma tabela temporária. Este erro ocorre somente para clientes que possuem EPL nessa rotina.

- VDP0745 - Não está descontando o item de retorno do valor da duplicata
- No VDP10900 ao executar a opção de criação do CST da Reforma Tributária fica sempre pendente.
- VDP50000 - Erro na passagem de parâmetro no cálculo de duplicatas.
Ao faturar uma solicitação, através do VDP0742, o valor do frete ( tipo 4,5 e 6)não está somando no total da nota.

- VDP10068 - Ao incluir ou pesquisar a configuração fiscal do tributo ICMS_ST, o programa apresentava erro e abortava a execução.

**Para envio do XML com as alterações da NT2025.002 v1.20 é necessário a atualização dos schemas do TSS.**

Até o momento já foram liberados as alterações para atender os seguintes cenários de tributação do IBS/CBS:

| Tributado integralmente | CST 000 |
| --- | --- |
| Tributado com redução de alíquota ( com tributação regular)* | CST 200 |
| Tributado com diferimento parcial ou total | CST 510 |
| Tributação imune e não incidência | CST 410 |
| Tributação suspensa (com tributação regular) * | CST 550 |

*Verificar na tabela cClassTrib para quais deverão ser enviados o grupo de tributação regular

Abaixo a relação de tributações e tipos de notas que ainda **não** foi implementado, será liberado em pacote futuro:

| Tributação monofásica |
| --- |
| Tributação crédito presumido |
| Notas com finalidade débito e crédito |
| Grupo de Compra governamental |
| Grupo Transferência de Crédito |
| Grupo Pagamento Antecipado |
| Grupo Fornecimento para Zona Franca de Manaus |
| Eventos |
| DANFE (com os novos tributos) |

## Pacote 03/11

**Funcionalidades Principais:**

- Emissão de notas de débito

As orientações abaixo podem sofrer alterações caso tenha novas publicações pela Sefaz ou alterações em legislação:

Para gerar uma nota de débito, é necessário seguir o procedimento:

- Utilizar uma natureza com controle N-Normal e sem operação de estoque;
- A natureza de operação deverá estar cadastrada dentro de um grupo fiscal no VDP10005 e este grupo informado no parametro grupo_fiscal_nota_debito no LOG00086.
- Parametrizar o CBS/IBS_MUN/IBS_UF no VDP10068 - Configuração Fiscal com o CST e Classificação tributária correspondente e ter relacionado na aba Tributos no VDP10059 - Natureza de Operação.
- Deve-se processar a nota pelo VDP0746 de forma manual quando for preciso informar somente valores dos tributos.
- Quando houver necessidade de referenciar uma nota fiscal, informar na tela de NF de referência, informando o tipo Manual Saída ou Manual Entrada.
- No caso da NF de débito tipo 03 -Débitos de notas fiscais não processadas na apuração, a referência deverá ser informada na tela após informar os dados do item.
- Na tela de itens informar o item com a quantidade igual a 1, ou zero e valor do item zero, ou dependendo do tipo de débito informar os valores normalmente.
- Na tela dos tributos, selecionar o tributo CBS/IBS_MUN/IBS/UF, e informar os campos Base calc, Base calc total, Valor calc e Valor total, verificar alíquota, CST e Classificação tributária dos tributos.

Abaixo o exemplo de uma solicitação de faturamento para uma nota de debito tipo 03:

Selecionar opção Manual:

Informar o tipo de débito:

Zerar os valores do item:

Importante: para o tipos de débito 06 e 07 os valores do item precisam ser informados

No caso do tipo 03, a tela de referencia será aberta após informar os dados dos itens, para outros tipo de débito a referência pode ser informada na tela NF referência:

Informar os valores dos tributos:

Observação: os valores acima são apenas exemplos, deve ser avaliado cada nota e cada situação.

Foi implementado na consulta da nota, VDP40005 opção Nota fiscal eletrônica - Informações NF-e, o campo tipo Débito.

No envio para a Sefaz, a nota referenciada será gerada no grupo <DFeReferenciado> caso a nota tenha alguma referencia informada.

Para os tipos de débito 01 e 05, é necessário enviar o grupo gTransCred, onde já foi desenvolvido porém nos testes de envio para a Sefaz não possível obter autorização, ocorre a rejeição 1132: Grupo de transferência de crédito não informado, mesmo com as tags sendo geradas corretamente no xml.

- Grupo de notas de Antecipação de Crédito, conforme Nota Técnica 2025.002:

Para as operações com pagamento antecipado, deverá ser emitida primeiro a nota fiscal finalidade de débito com o tipo de débito = 6 - Pagamento antecipado;

No VDP0746, incluir a solicitação informando o tipo débito =6 na tela Info. Notas de débito:

Informar os demais valores do item e faturar a nota.

Posteriormente quando a mercadoria for enviada e for emitida a nota fiscal de venda, na solicitação de faturamento deverá ser referenciada a nota fiscal de débito emitida anteriormente, na tela NF Referência deverá ser informado o tipo P - Antecipação de pagamento, pode ser informado uma ou mais notas.

No envio para a Sefaz, será gerado o grupo <gPagAntecipado> com a chave de acesso da nota fiscal referenciada.

- Ajustes para atender a redução de alíquota com diferimento

Foi implementado na tabela de CSTs e Classificação tributária, o CST 515 - Diferimento com redução de alíquota, para isso foi atualizado a fórmula 2 dos tributos CBS, IBS_UF e IBS_MUN, para que seja possível informar o % de redução de alíquota na configuração fiscal:

Observação: os percentuais devem ser informados conforme legislação vigente, os valores mostrados são apenas um exemplo.

Alterado também o envio da NF-e, para prever os grupos de Diferimento ( **gDi** f) e de redução de alíquota ( **gRed** ), no caso do **CST (515).**

- Crédito presumido e alterações da NT 2025.002 v1.30

Para emissão de notas com crédito presumido, deverá ser vinculado a natureza de operação os tributos 'CBS_CR_PRE' e 'IBS_CRE_PRE', parametrizar no VDP10068 - Configuração fiscal os dados para calcular o tributo:

O Class Trib Presum deverá estar previamente cadastrado no **OBF25200**

Na consulta da nota mostrará os valores correspondentes:

No xml da NF-e será gerado o grupo gCredPresOper

**Para envio do XML com as alterações da NT2025.002 v1.30 é necessário a atualização dos schemas do TSS.**

Até o momento já foram liberados as alterações para atender os seguintes cenários de tributação do IBS/CBS:

| Tributado integralmente | CST 000 |
| --- | --- |
| Tributado com redução de alíquota ( com tributação regular)* | CST 200 |
| Tributado com diferimento parcial ou total | CST 510/515 |
| Tributação imune e não incidência | CST 410 |
| Tributação suspensa (com tributação regular) * | CST 550 |
| Grupo Pagamento Antecipado | |
| Notas com finalidade débito** | |
| Tributação crédito presumido | |

*Verificar na tabela cClassTrib para quais deverão ser enviados o grupo de tributação regular

** Tipo debito 01 e 05 ainda não está sendo autorizado na Sefaz

Abaixo a relação de tributações e tipos de notas que ainda **não** foi implementado, será liberado em pacote futuro:

| Tributação monofásica |
| --- |
| Grupo de Compra governamental |
| Grupo Transferência de Crédito |
| Eventos |
| Estorno de crédito |
| Ajuste de competência |
| DANFE (com os novos tributos) |

## Pacote 17/11

**Funcionalidades Principais:**

- **Adequação da NFCom para os novos tributos da Reforma tributária.**

No **VDP60000** foram realizadas alterações nas funções que geram o xml para gerar as novas tags referente aos novos tributos da Reforma Tributária (CBS, IBS_UF e IBS_MUN)

As novas tags serão geradas somente quando o parâmetro doLOG00086:Data de início para cálculo dos tributos da reforma tributária ( **data_inicio_ref_trib)** estiver informado data inferior a data corrente.

Para cálculo dos tributos no faturamento da nota deverá ser feita a mesma parametrização que consta na aba 30/06 deste documento.

- **Cadastro de eventos.**

Foi liberado o cadastro centralizados dos eventos pela equipe de Obrigações Fiscal: [Guia de Uso - Reforma Tributária - Eventos](https://tdn.totvs.com/pages/viewpage.action?pageId=1009450038)

Para os eventos 112130 e 112140 foram liberadas funções de regra de negócio para validar a inclusão dos eventos conforme abaixo

112130 - Perecimento, perda, roubo ou furto durante o transporte contratado pelo fornecedor

Permite a inclusão de eventos para NF-e autorizada, onde o tipo de frete é CIF por conta do remetente, caso a nota possua tipo de frete = 3 FOB ou CIF pelo destinatário, não irá permitir a inclusão.

112140 - Fornecimento não realizado com pagamento antecipado

Permite a inclusão de eventos para NF-e autorizada, precisa ser uma Nota de débito, com o tipo de débito = 6.

- **Ajustes referente a Exceção das rejeições 1037, 1036 e 1026**

A exceção das rejeições 1026 e 1036 já constavam na NT2025.002 e a 1037 foi implementada na versão 1.31:

Foi ajustado o calculo do tributo CBS/IBS_UF/IBS_MUN, para que seja zerado a alíquota no faturamento, caso tenha o tributo regular configurado.

Abaixo um exemplo deste caso, lembrando que é necessário informar a alíquota na configuração fiscal para que seja possível calcular o tributo regular.

- **Grupo de transferência de crédito**

Para a emissão das notas de débito tipo 01 - Transferência de créditos para Cooperativas; e 05=Transferência de crédito na sucessão, é necessário a utilização do CST 800 e também e gerar no xml o Grupo de Transferência de Crédito.

Na inclusão da solicitação pelo VDP0746, utilizar a opção Manual, informar natureza de operação deverá estar cadastrada dentro de um grupo fiscal no VDP10005 e este grupo informado no parametro grupo_fiscal_nota_debito no LOG00086, na tela de Info Notas Débito informar o tipo correspondente (01 ou 05), na tela de itens, deixar os valores zerados, e na tela de tributos, informar apenas os valores dos tributos CBS/IBS_UF/IBS_MUN, nos campos Valor calc e Valor total, a base de calculo ficará zerada.

No envio para a Sefaz o xml será gerado com o Grupo de Transferência de Crédito:

**Para envio do XML com as alterações da NT2025.002 v1.31 e para envio da NFCom é necessário a atualização dos schemas do TSS.**

Até o momento já foram liberados as alterações para atender os seguintes cenários de tributação do IBS/CBS:

| Tributado integralmente | CST 000 |
| --- | --- |
| Tributado com redução de alíquota ( com tributação regular)* | CST 200 |
| Tributado com diferimento parcial ou total | CST 510/515 |
| Tributação imune e não incidência | CST 410 |
| Tributação suspensa (com tributação regular) * | CST 550 |
| Grupo Pagamento Antecipado | |
| Notas com finalidade débito | |
| Tributação crédito presumido | |
| Grupo Transferência de Crédito | CST 800 |
| Eventos (Cadastros) | |

*Verificar na tabela cClassTrib para quais deverão ser enviados o grupo de tributação regular

** Avaliar o CST conforme situação

Abaixo a relação de tributações e tipos de notas que ainda **não** foi implementado, será liberado em pacote futuro:

| Tributação monofásica |
| --- |
| Grupo de Compra governamental |
| Eventos (Envio do xml) |
| Estorno de crédito |
| Ajuste de competência |
| Grupo de Informações da devolução de tributos |
| Indicador bem móvel usado |
| DANFE (com os novos tributos) |

## Pacote 08/12

**Funcionalidades Principais:**

- **NFS-e**

Neste pacote foram liberados alguns cadastros e alterações no faturamento para atender a NFS-e, o envio do xml ainda está em desenvolvimento pois o ambiente do governo ainda não foi liberado para testes.

**VDP10106 - Cadastro código Indicador de operação.**

Cadastro da tabela de códigos disponível no portal da NFS-e: **https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/anexovii-indop_ibscbs_v1-00-00.xlsx/view**

Esse cadastro será utilizado no faturamento de notas de serviço e depois enviado no xml na tag cIndOP.

Na opção Importar, é possível importar um arquivo csv ou txt com os dados da tabela, pode ser utilizado o arquivo: [cod_ind_op.txt](https://tdn.totvs.com/download/attachments/948652337/cod_ind_op.txt?version=1&modificationDate=1764960271523&api=v2)

**VDP0746 - Faturamento Manual**

Ao incluir uma solicitação de faturamento de serviço, se a data da reforma tributária estiver informada e o modelo da NFSe for modelo nacional, abrirá nova tela, após a tela de transportadora, para informar os campos relativos a NFS-e:

Ind Final: Indica operação de uso ou consumo pessoal.

Cod Ind. Operação: Código indicador de operação

Tipo de operação: Conforme a Regra de validação da NFS-e: Código do tipo de Operação (tpOper) deve ser informado quando se tratar de uma compra governamental ou um dos serviços da LC 116/2003 listados: 25.05; 15.09; 17.12; 10.05.

Para cálculo dos tributos no faturamento da nota de serviço deverá ser feita a mesma parametrização que consta na aba 30/06 deste documento.

Na consulta da nota VDP40005, foi criado uma nova opção Informações NFS-e para consulta dos dados informados na nota fiscal.

**MAN100021** - Ajuste no campo para informação do **NBS**

Para a NFS-e Nacional, a informação do NBS estava sendo buscado do campo Serviço do Municipio, porém foi identificado a necessidade de um campo próprio para o NBS, foi criado o campo Código NBS, na opção Comercial do MAN10021, este campo possui o zoom do cadastro de NBS: SUP20214.

NO **VDP10900 - Atualização da base de dados** foi criado uma opçao para migrar os dados do campo Serviço município para o campo Código NBS, quando o mesmo estiver cadastrado no sup20214 - Nomenclatura Brasileira de Serviços - NBS.

- **NF-e e NFCom**

Implementado a tratativa dos grupos gEstornoCred, gAjusteCompet e a tag indDoação.

No **vdp0746** foi incluso o campo " **Doação?"** na tela de itens, para identificar um item de doação.

Quando esse campo é marcado, no envio do xml será gerado a tag indDoacao = 1, abaixo um exemplo de xml, o CST e cClassTrib também são apenas exemplos, deve ser gerado conforme a operação da empresa.

Para atender o grupo Ajuste de competência (gAjusteComp), deverá ser gerado uma nota fiscal de débito pelo VDP0746, opção Manual **, com tributação/CST = 811 (Ajustes)** , ao informar o valor do tributo (CBS, IBS_UF ou IBS_MUN) abrirá nova tela para informar o Mês/ano competência da apuração.

Para atender o grupo Estorno de crédito (gEstornoCred), deverá ser gerado uma nota fiscal pelo VDP0746, opção Manual **,** com tributação/CST correspondente e informar o valor do tributos (CBS, IBS_UF ou IBS_MUN).

No envio do xml é verificado se o cClassTrib utilizado possui o indicador ind_gEstornoCred =1 para gerar o grupo gEstornoCred, por exemplo:

**SUP34260 -** Cadastro da classificação tributária:

**Importante** :

Foi implementado no VDP0746 uma validação para verificar se a natureza de operação possuir um dos novos tributos da reforma, é necessário ter os 3 tributos: CBS, IBS_UF e IBS_MUN, tendo os 3 tributos, é necessários que estejam configurados com o mesmo CST e Classificação tributária, caso não estejam irá dar uma mensagem e não permitir continuar a inclusão da solicitação enquanto não seja feito o ajuste da configuração fiscal.

Exemplo 1: Natureza possui CBS mas não possui IBS_UF: Exemplo 2: Possui configuração fiscal com Classtrib diferente para um dos tributos.

- **Data de previsão de entrega**

Conforme NT 2025.002, foi disponibilizado o campo Data de previsão de entrega:

Foram alterados os programas **VDP0746** e **VDP0742** para permitir informar a data de previsão de entrega na inclusão da solicitação, na tela Informações complementares da NFe:

**OBF40000** - Foi alterado as funções de envio do xml para ler a informação do faturamento e gravar a nova tag dPrevEntrega.

- **Eventos**

Alterado **OBF26300** para fazer as adequações na função responsável pela validação dos dados da nota fiscal x evento. **Novo evento: 112150- Atualização da Data de Previsão de Entrega.**

**Evento 112150 -** Permite o ajuste da data de previsão de entrega para qualquer nota válida. Se houver data digitada na nota, trará a data preexistente, caso contrário, permitirá a digitação da data de previsão de entrega.

Também foi liberado neste pacote a transmissão dos eventos via TSS, na central de eventos OBF26000 é possível enviar e retornar o xml dos eventos. Mais informações no guia de uso de Eventos: [Guia de Uso - Reforma Tributária - Eventos](https://tdn.totvs.com/pages/viewpage.action?pageId=1009450038)

- **Crédito presumido - Indicador Bem Móvel Usado**

No **VDP10068/VDP0696,** foi incluída fórmula 2 para os tributos CBS_PRE_CRE e IBS_PRE_CRE para atender esse cenário. Necessário executar o atualiza fiscal no VDP0692/VDP10064 para que as fórmulas fiquem disponíveis.

Alterado cálculo dos tributos da Reforma Tributária no faturamento, para **buscar os valores na nota de entrada** do **CBS, IBS_UF e IBS_MUN,** se informado uma nota fiscal de entrada como referência no VDP0746, será considerado os valores desta nota, caso não tenha sido informado a nota de aquisição será considerado a ultima compra do item.

Alterado faturamento, **VDP0746** , para prever na tela de referências da nota fiscal novo **tipo 'U' (Bem móvel usado)** e o novo campo ' **Bem móvel usado?** ' na tela dos itens da nota fiscal .

A referência não é obrigatória, porém quando informado irá buscar os valores da nota fiscal de entrada informada na referência, caso não for informado irá considerar os valores da ultima compra do item.

Na tela NF referência pode ser informada a NF de aquisição do item, ou então na tela de itens, quando marcar o campo Bem móvel usado, irá aparecer a pergunta: "Deseja informar a nota fiscal de aquisição?"

- Se responder que sim, ao final da inclusão de cada item da nota fiscal, abrirá a tela de referência por item para que seja informada a nota de entrada/AR e sequencia do AR.
- Se responder não, seguirá com a inclusão na nota normalmente, não exigindo a nota de referência (aquisição).

Alterado também **OBF40000** para gerar a tag <indBemMovelUsado> igual a "1" no xml da nota, quando o campo 'Bem móvel usado' estiver marcado.

Mais informações sobre esse processo, consulte o parecer da consultoria tributária item 3.2: [Orientações Consultoria de Segmentos - PSCONSEG-18580 - Reforma Tributária - Eventos de Apropriação do Crédito Presumido](https://tdn.totvs.com/pages/viewpage.action?pageId=984974365)

Até o momento já foram liberados as alterações para atender os seguintes cenários de tributação do IBS/CBS:

| Tributado integralmente | CST 000 |
| --- | --- |
| Tributado com redução de alíquota ( com tributação regular)* | CST 200 |
| Tributado com diferimento parcial ou total | CST 510/515 |
| Tributação imune e não incidência | CST 410 |
| Tributação suspensa (com tributação regular) * | CST 550 |
| Grupo Pagamento Antecipado | |
| Notas com finalidade débito | |
| Tributação crédito presumido | |
| Grupo Transferência de Crédito | CST 800 |
| Eventos (Cadastros e envio do xml) | |
| Estorno de crédito | |
| Ajuste de competência | CST 811 |
| Indicador bem móvel usado | |
| Indicador de doação | |
| NFS-e - Cadastros e Faturamento | |

*Verificar na tabela cClassTrib para quais deverão ser enviados o grupo de tributação regular

** Avaliar o CST conforme situação

Abaixo a relação de tributações e tipos de notas que ainda **não** foi implementado, será liberado em pacote futuro:

| Tributação monofásica |
| --- |
| Grupo de Compra governamental |
| Grupo de Informações da devolução de tributos |
| DANFE (com os novos tributos) |
| NFS-e - Envio do xml |

## Pacote 22/12

**Funcionalidades Principais:**

- **NFS-e modelo Nacional**

Foram realizadas alterações nas funções do OBF50000 para gerar as notas tags conforme NT 004, disponível no portal da NFSe:

[https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc)

Importante: o parametro do LOG00086 - Permite enviar mais de um item na NFS-e? (permite_itens_nfse) precisa estar como **N** , pois o modelo nacional não permite mais de um item no xml, caso a nota fiscal tenha mais de item, com as mesmas características(cnae, código item lista serviço, tributação no município, nbs), será feito o agrupamento no envio da NFS-e

Para calculo dos tributos no faturamento, deve seguir as orientações do Guia de uso, ver aba 'Pacote 30/06': [Guia de Uso - Reforma Tributária - Vendas#-1097053754](https://tdn.totvs.com/pages/viewpage.action?pageId=948652337#GuiadeUsoReformaTribut%C3%A1riaVendas--1097053754)

Também foram realizados ajustes no cancelamento da NFSe, a solicitação deverá ser feita pelo VDP0753, e o parametro do LOG00086 - Possui cancelamento de NFS-e para o municipio do emitente? (utiliza_cancelamento_nfse) = 'S'

Mais detalhes consulte o DT: [DBACKRTLGX-3585 - RT - Envio de NFS-e modelo Nacional com os novos tributos CBS/IBS_UF e IBS_MUN](https://tdn.totvs.com/pages/viewpage.action?pageId=1024346165)

- **Notas de débito para cliente interestadual**

Foi realizado ajustes para prever a emissão de notas de débito para clientes interestadual e exterior, será gerado o CFOP conforme abaixo:

5.949 - Clientes dentro do estado

6.949 - Clientes interestaduais

7.949 - Clientes exterior

- **Devolução a forncedores**

Necessidade de verificar no documento de origem(nota de entrada) se tem os novos tributos da reforma tributária (IBS/CBS) e gerar na nota de saída - devolução a fornecedor somente se tiver na entrada.

Foi alterado o calculo da nota fiscal, quando se trata de uma devolução a fornecedor e foi informado a referencia da nota no VDP0746, para verificar se a NF de entrada possui os novos tributos da reforma tributária (CBS, IBS_MUN, IBS_UF, CBS_CR_PRE e IBS_CR_PRE), se encontrados na nota de entrada, irá calcular normalmente na nota fiscal de devolução(saída) conforme parametrização da configuração fiscal, mas caso não tenha os novos tributos na nota de entrada não irá calcular na nota de devolução(saída).

- **Validação de CSTs diferentes entre IBS_UF e IBS_MUN**

O sistema foi ajustado para realizar a validação dos **CSTs** dos tributos **IBS_MUN** e **IBS_UF** , evitando a ocorrência de erro em tela durante o processamento da nota fiscal.

Quando for identificada **divergência de CST** entre os tributos **IBS_MUN** e **IBS_UF** , a nota fiscal será gerada com **status 9** no programa **OBF40000.** Adicionalmente, no programa **VDP9202** será apresentada uma mensagem informativa ao usuário.

“Tributação/CST diferente entre os tributos IBS_MUN e IBS_UF para o item X.”

- **Emissão de notas de devolução com origem no módulo WMS**

Foram realizado ajustes para verificar se a nota fiscal de devolução tem origem no módulo de WMS, caso positivo será gerado apenas as tags de referencia no grupo NFref, isso ocorre devido a múltiplas notas referenciadas para o mesmo item, conforme a NT2025.002, para um mesmo item só é possível referenciar uma nota fiscal no grupo DFeReferenciado.

- **Ajustes na tela de referência por item e de itens VDP0746**

Alterado o vdp0746/vdp0782(tela de itens) para os ajustes necessários:

- Passa a consistir novos tributos apenas se a data de início da reforma for menor ou igual a data do faturamento.

- Correção no problema em informar o código do item e não permitir dar continuidade na inclusão dos dados.

- Na tela de referência por item, ao informar o AR/nota e carregar os dados da nota de entrada, já vai passar para o campo de sequência do AR.

- **Eventos via TC2**

Liberado as alterações para permitir o envio do xml dos eventos via Totvs Colaboração 2.0

Até o momento já foram liberados as alterações para atender os seguintes cenários de tributação do IBS/CBS:

| Tributado integralmente | CST 000 |
| --- | --- |
| Tributado com redução de alíquota ( com tributação regular)* | CST 200 |
| Tributado com diferimento parcial ou total | CST 510/515 |
| Tributação imune e não incidência | CST 410 |
| Tributação suspensa (com tributação regular) * | CST 550 |
| Grupo Pagamento Antecipado | |
| Notas com finalidade débito | |
| Tributação crédito presumido | |
| Grupo Transferência de Crédito | CST 800 |
| Eventos (Cadastros e envio do xml) via TSS e TC2 | |
| Estorno de crédito | |
| Ajuste de competência | CST 811 |
| Indicador bem móvel usado | |
| Indicador de doação | |
| NFS-e - Cadastros e Faturamento | |
| NFS-e - Envio do xml modelo Nacional via TSS | |

*Verificar na tabela cClassTrib para quais deverão ser enviados o grupo de tributação regular

** Avaliar o CST conforme situação

Abaixo a relação de tributações e tipos de notas que ainda **não** foi implementado, será liberado em pacote futuro:

| Tributação monofásica - [https://tdn.totvs.com/x/64kVPQ](https://tdn.totvs.com/x/64kVPQ) |
| --- |
| Grupo de Compra governamental |
| Grupo de Informações da devolução de tributos |
| DANFE (com os novos tributos) |
| NFS-e - Envio do xml no leiaute único TSS |

## Pacote 29/12

**Funcionalidades Principais:**

- **NFS-e modelo único TSS**

Foram realizadas alterações nas funções do OBF50000 para gerar as tags referente aos novos tributos CBS, IBS_UF e IBS_MUN conforme o modelo único do TSS: [Modelo único de envio de NFS-e (Modelo Obsoleto)](https://tdn.totvs.com/pages/viewpage.action?pageId=679180430)

É necessário estar com o TSS atualizado no ultimo pacote e schemas liberados e verificar se o município já possui a implementação da Reforma tributária dentro do leiaute único do TSS: [Prefeituras atendidas pelo TSS para Transmissão de NFSe](https://tdn.totvs.com/pages/viewpage.action?pageId=4814340)

**Importante** : o parametro do LOG00086 - Permite enviar mais de um item na NFS-e? (permite_itens_nfse) precisa estar como **N** , pois o modelo único com as informações da reforma tributária não permite mais de um item no xml, caso a nota fiscal tenha mais de item, com as mesmas características(cnae, código item lista serviço, tributação no município, nbs), será feito o agrupamento no envio da NFS-e

Para envio no modelo único é preciso informar o parametro Utilizar layout único do TSS para transmissão de NFS-e? (utiliza_layout_unico_tss) = **S** do LOG00086 e no VDP10076 - opção NFSe no campo Modelo NFSe, informar **NFSe Prefeitura**

Para calculo dos tributos no faturamento, deve seguir as orientações do Guia de uso, ver aba 'Pacote 30/06': [Guia de Uso - Reforma Tributária - Vendas#-1097053754](https://tdn.totvs.com/pages/viewpage.action?pageId=948652337#GuiadeUsoReformaTribut%C3%A1riaVendas--1097053754)

Caso a prefeitura exige a informação do código NBS, deverá ser informado no cadastro do item - MAN10021 - Comercial

- **VDP40005**

Para atender a emissão das nota fiscais de serviço eletrônico, é necessário informar alguns dados complementares da NFSe, para isso foi implementado inicialmente somente no VDP0746, para notas de serviço faturadas a partir de um pedido, poderá ser informado os dados na consulta da nota antes do envio para a prefeitura.

Realizado alteração na opção Nota fiscal eletrônica - Informações da NFSe para permitir a modificação/inclusão dos dados da NFSe:

Consulte a nota na tela principal e altere os dados na opção Informações da NFSe

Será permitido a alteração para notas que ainda não foram enviadas para prefeitura ou que estão com status de Rejeitada(R) , Falha de schema(8) ou Erro no Logix (9) no OBF50000.

Até o momento já foram liberados as alterações para atender os seguintes cenários de tributação do IBS/CBS:

| Tributado integralmente | CST 000 |
| --- | --- |
| Tributado com redução de alíquota ( com tributação regular)* | CST 200 |
| Tributado com diferimento parcial ou total | CST 510/515 |
| Tributação imune e não incidência | CST 410 |
| Tributação suspensa (com tributação regular) * | CST 550 |
| Grupo Pagamento Antecipado | |
| Notas com finalidade débito | |
| Tributação crédito presumido | |
| Grupo Transferência de Crédito | CST 800 |
| Eventos (Cadastros e envio do xml) via TSS e TC2 | |
| Estorno de crédito | |
| Ajuste de competência | CST 811 |
| Indicador bem móvel usado | |
| Indicador de doação | |
| NFS-e - Cadastros e Faturamento | |
| NFS-e - Envio do xml modelo Nacional via TSS | |
| NFS-e - Envio do xml no leiaute único TSS | |

*Verificar na tabela cClassTrib para quais deverão ser enviados o grupo de tributação regular

** Avaliar o CST conforme situação

Abaixo a relação de tributações e tipos de notas que ainda **não** foi implementado, será liberado em pacote futuro:

| Tributação monofásica - [https://tdn.totvs.com/x/64kVPQ](https://tdn.totvs.com/x/64kVPQ) |
| --- |
| Grupo de Compra governamental |
| Grupo de Informações da devolução de tributos |
| DANFE (com os novos tributos) |
