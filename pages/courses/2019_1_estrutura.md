title: Estrutura e Concepção de Circuitos Integrados (CMOS)
menu: courses
date: 2018.2

## Ano 2019
## Período 1

---
O Calendario letivo para esse semestre ([calendario UFPB](http://www.prg.ufpb.br/prg/codesc/documentos/calendario-academico/academico-campi-i-e-iv-2018-2.pdf/view)) tem início dia 22 de novembro de 2018 e término dia 10 de maio de 2019. Um recesso deverá acontecer durante os meses de dezembro e janeiro, como mostrado no calendário.

---
### *Plano da disciplina:*
A disciplina de Dispositivos Eletrônicos é composta de três unidades:

* Unidade 01: Elementos de Projeto em Microeletrônica CMOS
* Unidade 02: Fisica dos dispositivos MOS e amplificadores de um estágio e amplificadores diferenciais.
* Unidade 03: Resposta em frequência de amplificadores e espelho de corrente

Você vai encontrar o link pra o plano completo da disciplina [aqui](link para o plano da disciplina).

---
### *Contato*
Os horários para consulta fora do horário de aula são:

* Segunda-feira - 14h-16h
* Quinta-feira - 14h-16h

Por e-mail não esqueça de seguir a expressão '[Estrutura] - &#60;título&#62;' no título do e-mail. Caso contrário meu cliente de e-mail filtrará diretamente para a pasta de *spam*.

O e-mail é <a href="mailto:rsmarinho@cear.ufpb.br">rsmarinho@cear.ufpb.br</a>.

---

### *Provas e trabalhos:*

Você pode encontrar os roteiros com os todos os trabalhos da disciplina [aqui](https://github.com/rsmarinho/ecci_labs). Ou se preferir olhar de um por um olhe abaixo:

* [lab01](https://github.com/rsmarinho/ecci_labs/blob/master/lab01.pdf)
* [lab02](https://github.com/rsmarinho/ecci_labs/blob/master/lab02.pdf)
<!-- * [lab03](https://github.com/rsmarinho/ecci_labs/blob/master/lab03.pdf) -->
<!-- * [lab04](https://github.com/rsmarinho/ecci_labs/blob/master/lab04.pdf) -->
<!-- * [lab05](https://github.com/rsmarinho/ecci_labs/blob/master/lab05.pdf) -->
<!-- * [lab06](https://github.com/rsmarinho/ecci_labs/blob/master/lab06.pdf) -->
<!-- * [lab07](https://github.com/rsmarinho/ecci_labs/blob/master/lab07.pdf) -->
<!-- * [lab08](https://github.com/rsmarinho/ecci_labs/blob/master/lab08.pdf) -->
<!-- * [lab09](https://github.com/rsmarinho/ecci_labs/blob/master/lab09.pdf) -->
<!-- * [lab10](https://github.com/rsmarinho/ecci_labs/blob/master/lab10.pdf) -->

---

### *Livro texto:*
O principal livro utilizado nessa disciplina é o [Design of Analog CMOS Integrated Circuits](https://www.amazon.com/Design-Analog-CMOS-Integrated-Circuits/dp/0072380322), outros livros são considerados como material de apoio. Por exemplo:

* [CMOS: Circuit Design, Layout, and Simulation](https://www.amazon.com/CMOS-Circuit-Simulation-Microelectronic-Systems-ebook/dp/B004J4VVM4/ref=sr_1_1?crid=25T8MLN1T921B&keywords=cmos+circuit+design%2C+layout%2C+and+simulation&qid=1559242607&s=books&sprefix=cmos+circuit%2Cstripbooks-intl-ship%2C235&sr=1-1)
* [CMOS Analog Circuit Design](https://www.amazon.com/Circuit-Design-Phillip-Douglas-Holberg/dp/0199937427/ref=sr_1_fkmr0_1?keywords=philip+allen+cmos&qid=1559242633&s=books&sr=1-1-fkmr0)

Também é recomendado que o aluno tenha algum conhecimento do simulador de circuitos SPICE (ou algum outro simulador de circuitos). Isso é importante porque faremos muito uso de simulações durante as aulas.

Abaixo eu listo algum material que pode servir de guia para seus estudos. Não faça desse material sua única fonte de estudo para disciplina. Estas são notas de aula que ainda estão sendo desenvolvidas e que portanto podem não acompanhar a sequência das aulas.

---

### *Material de apoio:*

Você encontrará mais material de apoio [aqui](https://drive.google.com/drive/folders/1r0Qymi3utqgJtTObksUJIuvzFO-i3BoH?usp=sharing)

## Unidade 00

* Aula 01
[[Nota de aula](/estrutura/aula_01)]
  1. Contextualização da disciplina

## Unidade 01
  <!-- [[Quiz](/dispositivos/quiz)] -->
  <!-- [[Exercicios](/dispositivos/exercicios)] -->

* Aula 01 - MOSFETs: princípio de funcionamento
  Revisão sobre o BJT
  1. Introdução aos transistores a efeito de campo
  2. MOSFETS
    * Estrutura física
    * Relação tensão-corrente
    * Regiões de funcionamento
    * Efeitos de segunda ordem

* Aula 02 - MOSFETs: Modelo equivalente para pequenos sinais e polarização
  1. Modelo equivalente para análise de pequenos Sinais (baixa-frequência)
    * Transcondutância
    * Resistência de saída
  2. Circuitos de polarização
    * Tensão \(V_{GS}\) fixa
    * Resistor de degeneração de Fonte
    * Espelho de corrente

* Aula 03 - Amplificadores com MOSFETs (1/2)
  1. Configuração fonte comum
    * Ganho, impedâncias de entrada e saída
    * Degeneração de fonte
    * Impacto do efeito de modulação de canal
    * Carga ativa

* Aula 04 - Amplificadores com MOSFETs (2/2)
  1. Configuração Porta-Comum
    * Ganho
    * Impedâncias de entrada e saída
  2. Configuração Dreno-Comum
    * Ganho
    * Impedâncias de entrada e saída
