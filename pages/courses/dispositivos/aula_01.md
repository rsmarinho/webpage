title: Dispositivos Eletrônicos
aula: 01
menu: courses
date: 2018.2

---

# Dispositivos Eletrônicos
## Unidade 01 : Conceitos gerais, junção PN e Diodos

---

Revisão e Contextualização
==========================

# Plano de Aula:
* Contextualização da disciplina
* Revisão sobre fontes reais de sinais
* Fontes de corrente controlada
* Cálculo de correntes e tensões com objetivos de caracterização

---

## Contextualização

Na disiciplina de sinais e sistemas vocês aprenderam (ou aprenderão) a estrutura de um sinal analógico e sobre como representá-lo em frequência. Aprenderam sobre amostragem e digitalização de um sinal analógico e sobre como reconstruí-lo de tal forma que a informação contida nesse sinal possa ser reconstituída.

O que não deve ter ficado claro, porém, é que a transformação de um sinal analógico para um sinal digital é *meramente* um artifício matemático que permite a operação desses sinais em outro domínio, ou em abstrações de processadores lógicos. O que deve ficar claro nessa situação é que o sinal *elétrico* que trafega pelos componentes ainda é analógico! Ou seja, o processamento elétrico de qualquer sinal é feito analogicamente.

Nesse contexto, podemos afirmar que a engenharia é feita de abstrações e compartimentalização de problemas. O que na (\(\mu\)-)eletrônica pode ser traduzido com a afirmação de que eventualmente você encontrará problemas em que será necessário estimar um dispositivo "forçando" uma corrente ou uma tensão em determinado ponto de um circuito.

<img class="center" src=/static/figures/ alt="drawing">

O circuito da figura acima, por exemplo, pode ser considerado uma abstração básica que demonstra características de circuitos encontrados em eletrônica.

Em uma estrutura mais completa podemos, por exemplo, visualizar o circuito eletrônico como uma fonte equivalente de Thèvenin conectada na entrada do próximo circuito.

## Fontes ideais vs. Fontes reais
Devemos supor que no mundo real fontes ideais não existem, pois caso existissem seria gerado um paradoxo (ao conectar seus terminais positivo e negativo a corrente que passa no curto-circuito deveria ser infinita). Ora se fontes ideais não existem, o que fazer? A representação de uma fonte real com uma resistência de fonte responde a esse questionamento e estabelece dois modelos de fontes que são equivalentes: O modelo de fonte equivalente de Norton e o modelo de fonte equivalente de Thèvenin.

<img class="center" src=/static/figures/ alt="equivalente_norton_thevenin">

Agora, com os equivalente de fonte, como estabeler se a ligação forçada em determinado ponto do circuito é de corrente e de tensão? Em outras palavras, ao conectar uma fonte *real* a determinado circuito, como saber se essa fonte real funciona como uma fonte de tensão ou uma fonte de corrente? Bem, essa resposta depende do referencial. Suponha por exemplo o circuito representado na figura abaixo:

<img class="center" src=/static/figures/ alt="exemplo_fontes_tensao_corrente">

Devemos calcular a corrente injetada na resistência de carga \(R_L\) e a tensão medida em seus terminais. Para esses casos suponha que a resistência \(R_L\) possa assumir quatro valores diferentes: No caso (a) quando \(R_L>>R_S\) temos \(R_L=1k\Omega\), \(R_L=10k\Omega\). No caso (b) quando \(R_L<<R_S\) temos \(R_L=1m\Omega\), \(R_L=10\mu\Omega\).

---
No caso (a) temos que:
$$
v_L(R_L=1k) = 1.5\frac{1k}{1k+1}=1.498\,V, \\ i_L(R_L=1k)=\frac{1.498}{1k}=1.498\,mA
$$e$$
v_L(R_L=10k) = 1.5\frac{10k}{10k+1}=1.498\,V, \\ i_L(R_L=10k)=\frac{1.498}{10k}=0.1498\,mA
$$
No caso (b) temos que:
$$
v_L(R_L=10^{-3}) = 1.5\frac{10^{-3}}{10^{-3}+1}=1.498\,mV,\\ i_L(R_L=10^{-3})=\frac{1.498\times10^{-3}}{10^{-3}}=1.498\,A
$$$$
v_L(R_L=10^{-2}) = 1.5\frac{10^{-2}}{10^{-2}+1}=14.85\,mV,\\ i_L(R_L=10^{-2})=\frac{1.498\times10^{-3}}{10^{-2}}=1.48\,A
$$

---
Repare que na situação (a), quando \(R_L>>R_S\), a tensão na carga permanece (quasi-) estável, enquanto a corrente modifica muito. No caso (b), quando \(R_L<<R_S\) acontece a situação contrária, a corrente permanece (quasi-) estável e a tensão modifica muito.

Diz-se então que na situação (a) a fonte é de tensão pois o circuito está sendo alimentado por uma tensão fixa. Enquanto na situação (b) é dito que a fonte é de corrente pois o circuito está sendo alimentado por uma corrente fixa.

## Fonte de Corrente Controlada
Em alguns casos, existem circuitos que são representados por fontes de corrente controladas. Usualmente, a relação entre o controle de corrente é dado por um fator de multiplicação (\(k\)); entretanto, quando essas fontes são utilizadas para modelagem de dispositivos
e possível que essa relação possa ser representada por uma função não-linear.

Fontes de corrente controladas são estruturas de duas portas diferenciais, como representado na figura abaixo. Perceba que à saída é conectada uma fonte de corrente de valor \(i=k\times v_C\), onde \(v_C\) é o sinal aplicado aos terminais de entrada da fonte, e \(k\) é o termo que multiplica a referência de corrente.

<img class="center" src=/static/figures/ alt="fonte_corrente_controlada">

Várias coisas podem ser modeladas com fontes de corrente controladas por tensão (CCCV), Por exemplo, podemos modelar o comportamento de um diodo conectando os terminais de entrada da CCCV com os terminais de saída da seguinte forma

<img class="center" src=/static/figures/ alt="fonte_corrente_controlada">

Nesse caso, entretanto a relação I-V do circuito é uma relação não linear pois descreve o comportamento I-V de um diodo. Portanto, a relação de corrente vs. tensão nos terminais do diodo é representada por
$$
i=I_D=f(v_D)=k_1\exp{(k_2v_D)}
$$

## Cálculo de correntes e tensões com objetivos de caracterização

Esta modelagem não linear do diodo serve para reforçar um dos objetivos da disciplina, o de desenvolver habilidades no projeto de amplificadores. Para isso, estamos interessados dentre outras coisas na *relação entre tensões* em pares diferentes de terminais (o que descreve ganho), na relação entre tensão e uma corrente (o que descreve uma resistência), ou em uma combinação dessas características.

---
*Exemplo:*
