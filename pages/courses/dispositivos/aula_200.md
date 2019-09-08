title: Dispositivos Eletrônicos
aula: 20
menu: courses
date: 2018.2

---

#### Unidade 03 : Transistores CMOS

---

Amplificadores com MOSFETs (1/2)
================================

## Plano de Aula:
* Configuração Fonte-Comum
  * Ganho, impedâncias de entrada e saída
  * Degeneração de fonte
  * Impacto do efeito de modulação de canal
  * Carga ativa

---

Antes de começar devemos fazer algumas considerações. Lembramos que o 
projeto de um amplificador utilizando transistores é baseado no cálculo 
dos parâmetros de pequenos sinais do circuito do transistor, e na 
topologia desse circuito. Em outras palavras, encontrar o ponto de 
polarização do circuito de agordo com o ganho requerido pelo problema; 
para que o transistor opere nesse ponto de polarização o circiuto de 
apoio - circuito que é formado pelos resistores que estão conectados 
aos terminais do transistor, por exemplo - deve ser dimensionado tal 
que os valores de tensão e corrente nos terminais do transistor sejam 
fixados.

Nesse ponto devemos estabelecer alguns termos comuns ao estudo dos
amplificadores com CMOS, as três topologias básicas de ligação do 
transistor (e que se referem aos três terminais do transistor) são 
listadas na tabela abaixo:

| Entrada    | Saída   | Nome        |
|------------|---------|-------------|
| Porta      | Dreno   | FONTE comum |
| Fonte      | Dreno   | PORTA comum |
| Porta      | Fonte   | DRENO comum |

---
<font color="red">
aviso que deve fazer parte da aula 19
</font>

Antes de continuar, lembramos que nosso modelo de pequenos sinais se 
resume à uma análise simplificada do modelo. Nesse caso, somente são 
calculados três parâmetros: \(g_m\), \(R_{B}\) e \(r_o\). Além disso, 
apenas é possível o cálculo desses três parâmetros quando utilizamos 
o transistor bipolar, isso porque no transistor MOSFET, to terminal
de porta (equivalente nase no bipolar) apresenta uma resistência de
entrada idealmente infinita devia à estrutura física do transistor.

Portanto, para o transistor MOSFET como consideramos ao longo desse 
curso, a resistência de entrada \(r_{in}=\infty\). Apesar de isso ser 
falso em altas frequências, para cursos iniciais de dispositivos 
eletrônicos, devemos considerar algumas aproximações afim de facilitar
o entendimento. O fato de considerarmos \(r_{in}=\infty\) significa 
apenas que a corrente que entra no terminal porta do transistor é 
desprezível para fins de análise nos casos estudados nessa disciplina.

---

Nosso modelo de pequenos sinais somente leva em conta os dois
parâmetros: \(g_m\) e \(r_o\), e portanto, o 
