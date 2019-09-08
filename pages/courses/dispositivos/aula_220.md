title: Dispositivos Eletrônicos
aula: 21
menu: courses
date: 2018.2

---

# Dispositivos Eletrônicos
## Unidade 03 : Transistores CMOS
 
---

Resposta em Frequência (1/2)
============================

## Plano de Aula:
* Resposta em frequências: Conceitos preliminares
* Curva (e regras) de Bode
* Resposta passa-baixa e passa-alta
* Resposta em frequência de Amplificadores
* Exemplo numérico

---

Até agora agora a gente utilizou topologias de amplificadores, tanto com
bipolar quanto com o mosfet, em que a gente fazia uso de capacitores de 
acoplamento para acoplar a fonte do sinal na entrada, bem como para 
acoplar o sinal de saída do amplificador à carga. Em outra situação
utilizamos um capacitor em paralelo à fonte de corrente conectada ao 
terminal emissor do transistor TBJ, de forma a formar um curto-circuito
AC. Nesses casos os valores de capacitâncias muito elevadas sem nos 
preocuparmos com as limitações (preço, tamanho, capacitância) de 
projeto.

Entretanto, o que pode acontecer caso não seja possível a escolha 
arbitrária de valores de capacitância? Como sabemos que a impedancia
do capacitor é inversamente proporcional à frequência, então ao fixarmos
o valor de capacitância do capacitor e estamos trabalhando em uma 
frequência baixa, então a capacitância se torna alta, e vice-e-versa.

Do mesmo modo, para uma dada baixa frequência, os capacitores da figura
abaixo, por exemplo, desacoplam o sinal pois a impedância é elevada.

<img src=/static/figures/circuito_adaptacao.png alt="drawing" width=50%/>

O Capacitor \(C_{C_1}\), por exemplo, desacopla o sinal em baixa frequência
bem como os capacitores \(C_{C_2}\) e \(C_{E}\). Em outras palavras em 
cada um dos casos, e para baixas frequências, os capacitores deixam de 
funcionar como curtos-circuitos AC e apresentam uma alta impedância.

Então, nos três casos veremos que o sinal na resistência de carga vai 
diminuir, podemos ver isso como uma diminuição de ganho.
---
Quando a impedância de by-pass aumenta o ganho do amplificador diminui 
(como vimos em aulas anteriores)
