title: Dispositivos Eletrônicos
aula: 19
menu: courses
date: 2018.2

---

# Dispositivos Eletrônicos
## Unidade 03 : Transistores CMOS
---

Modelo equivalente para pequenos sinais e polarização
=====================================================

Essa é a aula 19 mosfets: modelo equivalente para pequenos sinais
e polarização

+++
Então tá aqui o plano da aula, a gente vai começar pelo modelo
equivalente para análise de pequenos sinais, como a gente tinha visto
tanto para o diodo quanto para transistor bipolar, em termos da
transcondutância e resistência de saída. Em seguida a gente vai abordar
os circuitos de polarização tanto com tensão vgs fixa, como com o
resistor de degeneração de fonte que é o equivalende ao resistor de
desgeneração do emisso, no caso do bipolar. E também por polarização
por espelho de corrente.

+++
Tal como a gente viu no caso do transistor bipolar, a gente procede da
mesma forma para converter o modelo não linear em um modelo linearizado
para a análise de pequenos sinais em torno de um ponto de polarização.

Então vejam aqui no caso não linear, se a gente tiver um transistor cujo
a corrente de dreno é dada por

$$
\frac{1}{2}\mu_nC_{ox}\frac{W}{L}(V_{GS}-V_{TH})^2
$$

isso vai se converter apenas numa transcondutância gmvgs por que a
corrente de dreno só depende de vgs, não depende nesse caso de vds.
E aqui a gente vê que a porta, por causa da estrutura física do
transistor (têm um isolante logo abaixo da porta com material condutor),
então a gente vai dizer que em baixa frequência não tem corrente de
porta, portanto o circuito é aberto como está aqui. Então a gente vai
com o mesmo circuito aberto para o modelo de pequeno sinal.

Agora, se por outro lado a gente leva em consideração o efeito de
modulação do canal, a gente tem então uma corrente de dreno:

$$
\frac{1}{2}\mu_nC_{ox}\frac{W}{L}(V_{GS}-V_{TH})^2(1+\lambda V_{DS})
$$

então essa corrente de dreno não somente depende de vgs que é a tensão
de controlo, como também depende de vds e aí dá origem a nossa
resistência r0 do nosso modelo de pequenos sinais equivalente.

+++
Então como é que a gente faz?
Se a gente considerar o primeiro caso como o caso mais simples onde
não há modulação do comprimento do canal. Então a gente pega a equação
e fazemos simplesmente a derivada, a única derivada que existe é da
nossa corrente de dreno em relação há tensão vgs. Isso a gente faz
com o vds de polarização, sem variação, sem flutuação. Então aí a
derivada é relativamente simples, então dá essa expressão daqui que é

$$
\frac{d I_{D0}}{d V_{GS}}=\mu_nC_{ox}\frac{W}{L}(V_{GS}-V_{TH})
$$

Se colocarmos a expressão em termos de corrente de dreno sobre tensão
VGS (devemos nesse caso considerar vgh pois é constante), então

$$
g_m=\frac{2I_{D0}}{V_{GS}-V_{TH}}=\sqrt{2\mu_nC_{ox}\frac{W}{L}I_D}
$$

Essa expressão a gente vai usar bastante.

+++
Se a gente agora considerar o efeito de modulação de canal, então a
gente vai fazer a transcondutância do mesmo jeito, vamos considerar
variações de corrente de dreno em relação de flutuações de tensão vgs
para um vds fixo, onde não haja variação de tensão de polarização vds.
Então no fim das contas, fazendo a derivada da equação em relação a vgs,
então o termo (1+\lambda*vds) passa a ser uma constante.

Lembrando ainda que nesse caso, apesar da equação s*ID0/(vgs-vth) ser
identica ao caso anterior, considera-se que Id0 obedece a relação da
modulação de corrente.

+++
Slide 06

Então, vejam aí, as expressões sempre querem nos dizre alguma coisa.

Como por exemplo podemos maximizar a transcondutância? Imaginemos uma
aplicação onde a corrente de dreno do transistor é limitada por questões
de autonomia de bateria, por exemplo para maximizar seu tempo de vida,
como faríamos para maximizar a transcondutância. Lembrando que no caso
do bipolar a transcondutância depende apenas da corrente do coletor,
da corrente de polarização, nesse caso não temos como mexer na
trascondutância para determinada corrente de polarização de coletor.

No caso do MOS, como a expressão é diferente, podemos variar a relação
de vgs, já que além da corrente de polarização Id gm é indiretamente
proporcional a vgs-vth. Portanto a transcondutância do transistor
cmos é variavel para uma corrente fixa.

Mas como diminuir vgs-vth para? Nesse caso, para manter o mesmo Id0
e variar vth, devemos compensar a equação variando a razão W/L.

+++

Diferentemente do trnasistor bipolar podemos de certa forma controlar
a transcondutância. Nesse caso, podemos compara os dois transistores
pelo seus ganhos de pequenos sinais.

Nesse caso, para que o ganho de transcondutância do mos seja igual a
do bipolar, devemos fazer com que (vgs-vth)/2 seja igual a vt, e para
que a transcondutância seja maior (vgs-vth) tem que ser menor do que
2*vt.

Comparativamente, é preciso um transistor MOS muito maior do que o
bipolar (em boa parte dos casos) para um mesmo valor de ganho de
transcondutância e corrente de polarização.

+++
É preciso agora conhecermos as características de um sinal ac dito
"pequeno" para que o circuito equivalente de pequenos sinais possa
ser utilizado durante a análise.

---

Exemplo 02:
----------
Nesse caso, queremos projetar o circuito de polarização para que o
transistor opere em um ponto de polarização determinado. Para o circuito
mostrado na figura, devemos então determinar o valor do resistor \(R_1\).

No problema, queremos que o transistor opere na fronteira de saturação,
portanto \(V_{DS}=V_{GS}-V_{TH}\)

---
Slide 20
--------
No espelho de corrente da figura, devemos atentar para o transistor
\(M_1\) que sempre estará em saturação. Isso acontece porque
\(V_{DS}=V_{GS}\), como \(V_{TH}\) em um transistor MOS do tipo N é
sempre positivo Para o caso do transistor operando em saturação, temos
que \(V_{GS}\) é sempre inferior a \(V_{DS}\), pois
\(V_{GS}-V_{TH}=V_{DS}\).

No caso do espelho de corrente da figura, como o
