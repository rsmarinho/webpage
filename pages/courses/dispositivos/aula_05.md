title: Dispositivos Eletrônicos
aula: 05
menu: courses
date: 2018.2

---
### Unidade 01 : Conceitos gerais, junção PN e Diodos
## Modelos equivalentes para análise de circuitos com diodo

### Plano de Aula:
* Três modelos à escolha: Exponencial, Ideal e o de Queda de tensão constante
* Modelo para análise de pequenos sinais

---

Durante as aulas passadas estudamos o comportamento da junção PN que forma o dispositivo semicondutor o qual chamamos de diodo de junção (ou simplesmente *diodo*). O comportamento da junção apresenta um efeito unidirecional bem definido, de onde podemos inferir que: em polarização direta a corrente aumenta muito rapidamente (exponencialmente) em função da tensão aplicada nos terminais do componente. Entretanto, em polarização inversa, a corrente que atravessa a junção pode ser, em geral, negligenciada.

Em uma análise menos rigorosa, pode-se dizer que o comportamento do diodo (*ideal*) é o de *curto-circuito* em polarização direta (\(V_D>0\)), e o de um *circuito aberto* em polarização reversa (\(V_D<0\)). A representação simbólica do diodo é mostrada abaixo, o anodo é o terminal dito *positivo* pois é o terminal que conecta com o material dopado com átomos aceitadores (material tipo-p); o catodo é o terminal dito *negativo* pois é conectado ao material dopado com átomos doadores (material tipo-n).

<img class="displayed" src="/static/images/diode_symbol.png" width="40%" height="40%" />

O modelo de um diodo não ideal ([o que é utilizado em um simulador de circuitos como PSPICE](http://www3.imperial.ac.uk/pls/portallive/docs/1/7292572.PDF), por exemplo), tenta tratar dos fenômenos não lineares que existem intrinsicamente no componente real. Um exemplo desse tipo de fenômeno é a dependencia da corrente \(I_S\) e da tensão \(V_T\) à temperatura, o que implica na variação relação I-V do componente com a temperatura ambiente.

Vamos desconsiderar esses efeitos e apresentar modelos de diodo que auxiliam cálculos rápidos na síntese e análise de circuitos.

### Diodo de junção real (modelo exponencial):

Quando desconsideramos fenômenos não-lineares intrínsecos ao componente, e assumimos que o diodo é formado *apenas* pela junção PN, podemos aproximar seu comportamento pela equação da junção obtida na aula passada (e reescrita aqui):
\begin{align}
I_{D}&= I_S\,\left[\exp{\left(\frac{V_D}{V_T}\right)}-1\right]
\end{align}

Além disso, quando consideramos valores de corrente mais usuais, em que da equação do diodo podemos despresar o termo unitário da equação, pois o termo exponencial é muito maior do que o termo unitário (lembre-se que a corrente inversa no silício é teoricamente da ordem de \(10^{-9}\)). Então, a relação I-V do diodo pode ser reescrita Como
\begin{align}
I_{D}&= I_S\,\exp{\left(\frac{V_D}{\eta V_T}\right)}
\end{align}

 O termo \(\eta\) é chamado de *fator de idealidade* e é utilizado na equação pois em condições normais os diodos não seguem a equação exponencial devido a diversas razões (veja explicações [aqui](https://www.pveducation.org/pvcdrom/ideality-factor) e [aqui](https://www.quora.com/What-is-ideality-factor-of-a-diode)). Dizemos que o diodo segue a equação exponencial, quando \(\eta=1\).

 Observe agora um simples circuito divisor de tensão

<img class="displayed" src="/static/images/voltage_divisor.png" width="30%" height="30%" />

Nesse caso é fácil calcular a corrente e a tensão no resistor \(R_2\), basta fazer \(I_{R1}=I_{R2}=V_{DD}/(R_1+R_2)\) e \(V_{R2}=I_{R2}R_2\). Mas e quando substituimos o resistor \(R_2\) por um diodo, que tem sua relação I-V que segue a equação (não-linear) exponencial? Como devemos proceder para o cálculo de tensão e corrente?

Ora, é preciso saber que nessa situação não existe resposta analítica para esse questionamento, os valores de tensão e corrente no diodo são calculados numericamente, através de iterações. Portanto, para obtermos os valores aproximados de tensão e corrente no circuito
<img class="displayed" src="/static/images/voltage_divisor_diode.png" width="30%" height="30%"/>
devemos proceder da seguinte forma:

1. **Extrair** as equações de corrente de Kirschoff (LCK);
2. **Estimar** a tensão no diodo \(V_D\);
3. **Calcular** a corrente no diodo \(I_D\);
4. Repete operação a partir de (2).

Perceba que nem sempre esse procedimento alcançará valores possíveis fisicamente (discrepantes ou absurdos), que são em geral tratados como erros de convergência. Nesse caso, deve-se retornar ao procedimento (2) e estimar o valor da corrente \(I_D\) e em (3) calcular a tensão \(V_D\). No exemplor, portanto, **extraímos** as equações do circuito:

* \(V_{DD}=RI_D + V_D\)
* \(I_{D}=I_S \exp\left(\frac{V_D}{\eta V_T}\right)\)

Agora vamos *estimar* a tensão \(V_D\) e *calcular* a corrente \(I_{D}\). Para isso, primeiramente obtemos as características do circuito como mostrado na figura, nesse caso portanto temos que:

* \(V_{DD}=10\,V\)
* \(R=1\,kV\)
* \(I_S=10^{-15}\,A\)
* \(\eta=1\)
* \(V_T=25.864\,mV\)

Para estimar a tensão \(V_D\) devemos inverter as equações de Kirschoff que encontramos, de tal forma que:

* \(I_{D}=\frac{V_{DD}-V_D}{R}\)
* \(V_{D}=\eta V_T \ln\left(\frac{I_D}{I_S}\right)\)

Procedendo com as iterações, temos:

|iteração|\(V_D\)|\(I_D\)|
|---|-------|-------|
|\(0\)|\(V_D=0\)|\(I_D=\frac{10-0}{10^3}=10\,mA\)|
|\(1\)|\(V_D=25.864\times 10^{-3}\ln\left(\frac{10\times 10^{-3}}{10^{-15}}\right)=0.714\,V\)|\(I_D=\frac{10-0.714}{10^3}=9.286\,mA\)|
|\(2\)|\(V_D=25.864\times 10^{-3}\ln\left(\frac{9.286\times 10^{-3}}{10^{-15}}\right)=0.772\,V\)|\(I_D=\frac{10-0.772}{10^3}=9.228\,mA\)|
|\(3\)|\(V_D=25.864\times 10^{-3}\ln\left(\frac{9.228\times 10^{-3}}{10^{-15}}\right)=0.772\,V\)|\(I_D=\frac{10-0.772}{10^3}=9.228\,mA\)|

Perceba que não é mais preciso que nenhuma iteração seja feita, pois já atingimos um valor fixo de \(V_D\) e \(I_D\) para o número de casas decimais estipuladas. Para valores mais precisos devemos utilizar mais casas decimais, e, portanto, mais iterações devem ser executadas.

---
*Exercício:*

Repita o exemplo anterior, mas agora *estime* o valor da corrente \(I_D\) no diodo e *calcule* o valor da tensão \(V_D\). Tente entender o que aconteceu e qual foi o motivo de isso ter acontecido.

---

### Modelo ideal

A quantidade de contas necessárias para obtenção da tensão e corrente no diodo pode rapidamente virar um inconveniente quando utilizamos o modelo exponencial. Em algumas situações, no entanto, podemos *aproximar* o diodo de junção por seu modelo ideal. Nos cenário, por exemplo, em que a tensão \(V_{DD}\) aplicada no circuito é muito maior do que a tensão no diodo, podemos simplesmente desprezar a tensão no diodo (\(V_D=0\)), caso ele esteja diretamente polarizado.
<img class="displayed" src="/static/images/voltage_divisor_diode.png" width="30%" height="30%" />

Por exemplo, na figura abaixo, se \(V_{DD}=100\) e \(R=1\,kV\), vemos que o diodo tem valores de  \(V_{D}\approx 833\,mV\) e \(I_D\approx 99.17\,mA\), calculados iterativamente. Quando utilizamos o modelo ideal de diodo, vemos que a corrente calculada é \(I_D= 100\,mA\), pois \(V_{D}= 0\,V\). Um erro menor do que \(1%\) quando comparamos com o valor anterior (calculado com o modelo exponencial).
<img class="displayed" src="/static/images/diode_ideal_iv_curve.png" width="30%" height="30%" />

O fato, portanto, de termos assumido \(V_{D}= 0\,V\) não implica em um erro grande na resposta da análise. O modelo ideal do diodo decorre, portanto, da constatação de que quando o diodo está reversamente polarizado a corrente é muito pequena (circuito-aberto), e quando em polarização direta a tensão em seus terminais é pequena (curto-circuito) quando comparada às tensões do circuito.

Mas como fica a relação I-V do circuito? Quando utilizamos o modelo de diodo ideal para visualizar as características I-V do modelo, devemos proceder como se a tensão \(V_{DD}\) aplicada ao circuito estivesse aumentando de valores muito baixos até valores muito altos. Portanto, para o circuito em questão não há passagem de corrente até que a tensão \(V_{DD}\leq 0\). Quando \(V_{DD}>0\) a começa a existir corrente que passa pelo circuito. Na ultima situação, podemos simplificar a corrente que passa pelo circuito (resistor e diodo), calculando a corrente que passa pelo resistor como \(I_D=V_{DD}/R\) (lembre-se:no modelo ideal \(V_D=0\) e portanto o diodo é um curto-circuito). Portanto a *curva característica* do circuito tem uma curva de angulação \(1/R\) para valores de \(V_{DD}>0\), como mostrado na figura:

<img class="displayed" src="/static/images/diode_circuit_iv_curve.png" width="25%" height="25%" />

Ora, essa é uma aproximação bastante *grosseira* e que serve em análises iniciais e que assume valores muito próximos do real quando os valores de tensão aplicados são muito elevados, como vimos anteriormente. No entanto, existe ainda uma outra aproximação do diodo (modelo) que se aproxima ainda mais do resultado obtido com a utilização do modelo exponencial, chamamos esse modelo de *modelo de queda de tensão constante*.

### Modelo queda de tensão constante

Em muitos circuitos o valor da tensão aplicada não será muito maior do que a queda de tensão provocada pelo diodo, no mais, fazer cálculo da corrente e tensão no diodo ainda é muito exaustivo (isso não vai mudar), e principalmente sujeito à erros. Nesses casos um melhor compromisso é utilizar o modelo de queda de tensão constante.

Antes de continuar com a descrição do modelo, vamos tomar como exemplo um diodo real (modelo D1N4002), que tem \(I_S=14.11\times 10^9\), \(\eta=1.984\). Quando calculamos os valores de tensão que devem ser aplicados como função da corrente, vemos que:
\begin{align}
I_D\approx I_S\exp\left(\frac{V_D}{\eta V_T}\right)&\Rightarrow V_D=\eta\,V_T\,\ln\left(\frac{I_D}{I_S}\right) \\
I_D=1\,mA &\Rightarrow V_D=0.574\,V \\
I_D=10\,mA &\Rightarrow V_D=0.692\,V \\
I_D=100\,mA &\Rightarrow V_D=0.810\,V \\
\end{align}
podemos observar que para uma grande faixa de valores de corrente, a tensão não passa de \(1\,V\). Nesses casos (em faixas de tensão da ordem de milli-amperes), podemos então adotar uma média de tensão para *ligar* o diodo. Em diversos casos o valor da média é de \(0.7\,V\) (no livro do Razavi é \(0.8\,V\)). Uma melhor representação do que o modelo ideal do diodo, portanto, é assumir que o diodo *liga* (curto-circuito) quando o \(V_D\geq 0.7\), e *desliga* (circuito aberto) quando é menor. Abaixo a curva característica representativa do modelo de queda de tensão constante:

<img class="displayed" src="/static/images/diode_constant_drop_iv_curve.png" width="30%" height="30%" />

O modelo de queda de tensão constante é um bom compromisso entre complexidade e precisão que pode ser utilizado em cálculos rápidos. Lembre-se que a resposta mais próxima da resposta exata do circuito envolve, em geral, muita conta. Mas nesses casos como saber qual modelo deve ser usado? Ora, isso vai depender da aplicação, e do quanto de precisão a resposta pede.

### Modelo de diodo para análise de pequenos sinais

 De uma maneira geral, em uma análise causa-efeito, percebe-se que ao variarmos a tensão aplicada no circuito (\(V_{CC}\), por exemplo) os valores de tensão nos terminais do diodo também se modificam. Esse comportamento faz variar a polarização do diodo e, por conseguinte, os valores de tensão-corrente. Portanto, problemas que envolvem variação da tensão nos terminais do diodo só podem ser  calculados utilizando o modelo exponencial, pois a utilização de modelos de tensão constantes fixa os valores de queda de tensão dos diodos do circuito.

 Em um circuito regulador de tensão diodos são utilizados para *fixar* a tensão de saída. Na verdade, o comportamento esperado desses circuitos é que a tensão regulada na saída sofra pequena variação quando uma grande variação acontece na tensão de entrada. Por exemplo, em um circuito regulador de tensão da figura abaixo, se a tensão de alimentação do circuito passar de \(10\,V\) para \(9\,V\) ou \(11\,V\), o comportamento esperado de \(V_O\) é que ele varie apenas (no máximo) algumas centenas de mili volts (lembre-se do comportamento exponencial da junção).

 <img class="displayed" src="/static/images/voltage_regulator_3diode.png" width="18%" height="18%" />

Como dito anteriormente, a tensão \(V_O\) desse circuito *só pode ser calculada com a utilização do modelo exponencial* (com o modelo de diodo ideal \(V_O=0\,\forall\,V_{CC}\), com o modelo de queda de tensão constante \(V_O=2.1\,V\,\forall\,V_{CC}\)). Nesse caso:

*Exemplo:*
Supondo que estamos trabalhando com o diodo de modelo N4002, que tem as seguintes características (**um notebook para jupyter para demonstração desse cálculo está disponível [aqui](/static/notebook_files/exemplo_iteracao.ipynb)**):

* \(I_s=14.1\times10^{-9}\), e
* \(\eta=1.984\)

que \(V_{DD}=10\,V\) e \(R=680\,\Omega\), e que estamos trabalhando em temperatura ambiente (assuma \(V_T=25.864\times10^{-3}\)), temos que:
\begin{align}
I_D=\frac{(V_{DD}-3V_D)}{R}&\Rightarrow V_D=\eta\,V_T\,\ln\left(\frac{I_D}{I_S}\right) \\
I_D=14.705\,mA &\Rightarrow V_D=0.711\,V \\
I_D=11.568\,mA &\Rightarrow V_D=0.698\,V \\
I_D=11.622\,mA &\Rightarrow V_D=0.699\,V \\
V_O=3V_D&=2.097\,V \\
\end{align}

Ainda, para diferentes valores de \(V_{DD}\). Se:

* \(V_{DD}=11\,V\Rightarrow V_O=2.115\,V\)
* \(V_{DD}=9\,V\Rightarrow V_O=2.076\,V\)

Repare na variação de \(V_O\) para diferentes valores de tensão \(V_{DD}\) (*E se os diodos fossem diferentes, como o cálculo seria feito?*). Mas será que existe uma maneira mais simples de calcular esse valor de tensão? A esposta à essa pergunta é resolver o problema com a utilização do modelo de pequenos sinais para o diodo.

Finalmente, o modelo de pequenos sinais se baseia no fato de que o diodo pode ser estimulado com a variação da tensão em seus terminais à partir de um ponto de operação DC. Uma vez polarizado com um valor de tensão e corrente fixos (DC) assume-se que: (1) se a variação do sinal de tensão \(V_D\) é muito pequena a variação da corrente do diodo é aproximadamente linear, (2) o valor de tensão é a soma do valor médio (\(V_D\)) com a variação em pequenos sinais (\(v_d(t)\)) que ocorre nos terminais do diodo. O passo a passo é o seguinte:

1. Calcula-se o valor médio (DC) da tensão e corrente, anulando-se todas as fontes variantes no tempo.
2. Anula-se as fontes DC, usa-se o modelo equivalente para pequenos sinais do diodo, e calcula-se as amplitudes de tensões  correntes que variam no tempo.
3. A resposta completa da tensão nos terminais do diodo é a soma da solução (1) com a solução (2), valor médio somado ao valor da variação no tempo.
