# Reforma Tributária Logix — Importação

Fonte: <https://tdn.totvs.com/pages/releaseview.action?pageId=1009450061>

## 1. Visão Geral

A **Reforma Tributária** traz um cenário de mudanças significativas nas regras tributárias brasileiras, exigindo das empresas uma adaptação rápida e precisa para garantir conformidade e eficiência operacional.

## Pacote 08/12

**Módulo IMPORTAÇÃO Logix**

- Alterado módulo Importação, para que efetue o cálculo dos tributos CBS, IBS_UF, IBS_MUN, CBS_CR_PRE e IBS_CR_PRE, com base no cadastro definido no

configurador fiscal VDP0696/VDP10068 Entradas (mesmo utilizado nas notas de entradas).

- Ao incluir a nota de importação pelo SUP3760, assumira os valores dos tributos como declarado ao visualizar os novos tributos.

Necessário **rodar conversor de tabela** : imp00056.cnv (caso não tenha sido executado, liberado no pacote 12.1.2507), imp00057.cnv, imp00058.cnv pelo LOG6000 e

**importar XMLs** : imp_proc_item_fisc.xml, despesa_imp.xml, zoom_processo_imp.xml, imp10136.xml e imp10137.xml pelo LOG00074.

- **FIN00000 (Programas Conversores)** **-** Marcar e processar **IMP10001** para que seja marcado automaticamente o indicador dos novos tributos nas despesas de impostos já existentes.

Altera apenas as despesas que incidem no Imposto de Importação.

**Importante:**

Fica a cargo do usuário **revisar IMP0073** após processamento e marcar o indicador nas despesas que deverão ser consideradas no cálculo dos novos tributos.

- **IMP0073 (Despesas de Importação)** - Cadastrar os códigos de despesa para os tributos **CBS, IBS_UF, IBS_MUN**

Revisar demais despesas se deve ser ou não considerada no cálculo dos novos tributos.

**Observação** :

- O IS (Imposto Seletivo) não está sendo tratado, foi apenas incluindo o campo para definir o código da despesa para o Imposto Seletivo.

- Contabilização será tratada futuramente.

- **IMP0008 (Parâmetros Importação)**

Param_processo: Cadastrar Despesas novos tributos.

Param_adiant: **‘Código Comite Gestor’** , informar o código definido para Comitê Gestor no VDP10000/VDP0815 (cadastrar fornecedor) e informar no IMP0008.

Caso não seja informado será considerado código da Receita Federal.

- **IMP0019/IMP0017** (Cálculo e visualização dos Tributos)

Cálculo novos Tributos (CBS, IBS_UF, IBS_MUN, CBS_CR_PRE, IBS_CR_PRE), no módulo importação é gerado via IMP0019/IMP0017 e tem o mesmo conceito do cálculo no Recebimento de materiais.

Deve ser efetuado o cadastro no VDP10068/VDP0696.

- Considerando

**Data de Desembaraço** , se informado, senão considera **data de pagamento impostos:** se data maior que a data inicio reforma tributária (LOG00087 parâmetro data_inicio_ref_trib);

**Município Tributação** informado no IMP0019/IMP0017;

**Grupo de despesa** informado na Ordem de Compra.

Os tributos serão visualizados na opção **Q_Tributos**

**OBSERVAÇÃO: Q_tributos** é fonte METADADOS, caso não tenha acesso a execução pelo IMP0019/IMP0017, deve ser cadastrado programa IMP10136 no MEN0050

**Para mais informações ACESSAR Documento Técnico:** [DBACKRTLGX-512 DT Módulo Importação (Parte 2)](https://tdn.totvs.com/pages/viewpage.action?pageId=1018587882)

## Pacote 12/01

- Alterado o cálculo da base do CBS/IBS para considerar a taxa Siscomex e demais impostos, taxas, contribuições ou direitos incidentes sobre os bens importados até a sua liberação, inclusive aqueles expressamente previstos no PLP 68/2024;

Xml de alteração de tela que precisam ser executados pelo log00074: imp10136.xml e imp10137.xml.

## Pacote 23/02

- CNPJ alfanumérico e ajustes no cálculo dos tributos;

- **Tributação Regular com redução de alíquota**

- Foi alterado o configurador fiscal para que nas fórmulas de entradas, em informações adicionais, possa ser incluída a redução da alíquota da tributação regular. (Necessário processar o botão Atualiza CTR)

Essa redução poderá ser consultada noIMP10136, para os tributo CBS_REG ou IBS_UF_REG ou IBS_MUN_REG.

## Pacote 27/04

- **Tributação(declarada/calculada), Classificação Tributária(declarada/calculada) e Incidência(declarada/calculada)**

- Os campos: tributação, classificação tributária e incidência, da tela IMP10136, estava sendo carregado conforme as informações do configurador de tributos(vdp0696/vdp10068), modificando as informações incluidas manualmente.

Para manter a rastreabilidade dos dados importados, criamos 3 novos campos na tabela de tributos(imp_proc_item_fisc):tributacao_calc, cod_classif_trib_calc e incidencia_calc, que serão carregados com as informações do configurador.

Portanto, será necessário atualizar:

- A tabela pelo log6000, rodando o conversor: imp00059.cnv;
- Os xmls pelo log00074: imp_proc_item_fisc.xml e imp10136.xml;

- Observação: Para o correto funcionamento do sistema, após a alteração das tabelas, deverá ser executado o FIN00000, programa SUP35006, para que os campos novos recebam os valores dos campos antigos, ou seja, tributacao_calc vai receber o valor do campo tributacao.

## Pacote 08/06

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

- **Inclusão do Processo de Importação pelo IMP0019:**

- Foi alterado a consistência do processo de importação, para que busque o tributo "IS" do configurador, e também inclua esse tributo na base de cálculo do CBS/IBS;
- Alteramos o IMP10136(Tributos do Processo de Importação) incluindo a coluna "Compl", onde para o tributo "IS"(imposto seletivo), ao clicar na linha, será apresentando uma tela auxiliar, podendo ser:

- informado o declarado
- visualizado o calculado

com os campos: percentual de alíquota específica, quantidade e unidade de medida.

1- Para essa alteraçãofoi necessário a criação de novos campos(alíquota específica, quantidade e unidade de medida) na tabela que armazena os tributos: imp_proc_item_fisc;

Sendo Necessário rodar o conversor de tabela pelo log6000: imp00060.cnv

E os xmls pelo log00074: imp10136.xml, imp101361.xml, imp_proc_item_fisc.xml

## Pacote 31/08

- **Descontar o ISS não retido(à recolher) da base do CBS/IBS/IS**

- O ISS não retido é calculado pelo módulo do Financeiro, no entanto, o mesmo precisa ser descontado da base do CBS/IBS/IS nas notas fiscais de serviço, ou notas de débito e crédito.

Para isso, alteramos o configurador de tributos, para que seja possível incluir a fórmula de cálculo para o ISS_REC:

Com as fórmulas:

- 701 - ISS à recolher, por alíquota, com base utilizando o **valor bruto** , sendo possível informar a redução da base;
- 702 - ISS à recolher, por alíquota, com base utilizando o **valor líquido** , sendo possível informar a redução da base;

Para atualização das fórmulas, é necessário rodar o menu "Atualiza Controle de Acesso" no configurador de tributos (vdp0696/vdp10068)

Depois deverá ser incluido o tributo ISS_REC, com origem E(Entrada) e filtros escolhidos;

O valor calculado para o ISS_REC, será diminuido da base do CBS, IBS_UF, IBS_MUN, IS, CBS_CR_PRE(crédito presumido) e IBS_CR_PRE(crédito presumido).

E pode ser consultado na tela de tributos:

Esse tributo apenas pode ser consultado, não pode ser informado os valores declarados.

Para essa alteração é necessário rodar o conversor de tabela pelo log6000: imp00062.cnv

E o xml de alteração de tela pelo log00074: imp10136.xml

## Pacote 12/10

- **Diminuir os Tributos nas Despesas de Importação**

- Foram criadas 2 formas de diminuir os tributos das Despesas de Importação:

- Informando um "Grupo de Despesa" no IMP0073 - Despesas de Importação,

que esteja cadastrado no Configurador de Tributos:

Ao incluir a Despesa de Importação no IMP0029, com ano maior ou igual a 2027 e moeda Real e salvar, irá apresentar a mensagem:

Ao responder SIM, irá calcular os tributos, conforme configurador fiscal (vdp0696/vdp10068), mostrando no campo "Tributos RT" e diminuindo do "Valor da Despesa":

Os tributos calculados, podem ser consultados no menu "Q-Tributos NF"

- Ou Informando um AR, pré-cadastrado no SUP3760 - Entrada de Nota Fiscal, com informações no menu Q-impostos, A-Tributos:

Exemplo :

Parametrizar no IMP0073 - Despesas de Importação, com o campo "Entrada via NF?" marcado:

Ao incluir no IMP0029- Despesas de Importação, informando o AR/seq, com ano maior ou igual a 2027 e moeda Real e salvar, irá apresentar a mensagem:

Ao responder SIM, irá buscar os tributos da AR, mostrando no campo "Tributos RT" e diminuindo do "Valor da Despesa":

Os tributos calculados, podem ser consultados no menu "Q-Tributos NF"

Para essa alteração é necessário rodar o conversor de tabela pelo log6000: imp00061.cnv e imp00066.cnv

E os xmls pelo log00074: zoom_despesa_imp.xml, despesa_processo.xml, despesa_processo_trib.xml, imp101461.xml, imp10146.xml

## Pacote 26/10

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

- Também foi alterado o programa IMP10136 - Tela de tributos do processo de importação:

- Para apresentação dos novos tributos
- Na coluna "Compl", mostrar as informações complementares da "gpBioDiferenca":

Foi necessário modificar a tabela imp_proc_item_fisc;

Devendo ser rodado o conversor de alteração de tabela pelo log6000: imp00067.cnv;

E rodar o xml de tela pelo log00074: imp10136.xml, imp101361.xml, imp101362.xml e imp_proc_item_fisc.xml.
