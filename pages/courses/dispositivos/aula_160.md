title: Dispositivos Eletrônicos
aula: 16
menu: courses
date: 2018.2

---

O segundo assunto que é o par diferencial: para que ele existe? no que
ele é usado?

Entao vejam só, se a gente viu aqui né? Então o nosso vout, vejam só
nesse circuito amplificador que está mostrado na figura quem é vout,
que é a tensão na saída do amplificador, vai ser dado por vcc, menos Rc
vezes a corrente de Q1 (IC). Aqui a gente tá mostrando um amplificador
em configuração emissor comum, tá? Então vai ser vcc menos rc vezes a
corrente de q1, e a corrente em q1 é controlada pelo nosso sinal do
microfone, variando a tenção no microfone eu vario a corrente em q1 --
de coletor -- e portanto eu vario o meu vout, aqui.

Então a gente percebe que vout é dependente de vcc então se vcc mudar,
se houver uma flutuaçõa em vcc, vai haver uma flutuação em vout. entõa
suponha por exemplo que nõa existe sinal de entrada (entrada nulo)
entõa vout vai ser um nivel de tensão a priori fixo que vai ser depdente
de vcc e da corrente de polarização do transistor, esse valor vai ser
fixo. Só que se vcc variar, vout também vai variar, então eu vou ter uma
flutuação em vout mas que não é devida a presença de sinal, mas sim por
conta de uma variação em vcc. Mas de onde viria esa variação em vcc.
Por exemplo, na primeira unidade, a gente viu como fazer fontes a
partir de retificadores e a gente viu que existia riipple na carga, uma
variação de tensão fornecida à carga.

A tensão fornecida à carga aqui é vcc, e a carga é o meu amplificador,
tá? então vai haver uma flutuação maior ou menos, dependendo se eu
utilizo um regulador de tensão ou não, mas vai sermpre haver uma
flutuação em vcc que vai influenciar o vout. E o problema é sobretudo
o fato de que nos cenários em que o valor do sinal é pequeno em relação
à essa flutuação de vcc. Vejam só, por exemplo a tensão de pico em um
microfone (mesmo um primeiro estágio) pode ser da ordem de alguns
milivolts enquanto o ripple no vcc pode ser de dezenas ou até de
centenas de milivolts no retificador.

então a variação de vcc nesse caso se traduzirá como interferencia em
60hz se o retificador for de meia onda ou 120hz se o retificador for de
onda completa. Em ambas as situações os sinais de interferência são
audíveis, então será entendido um chiado somado à nosso sinal de
amplificador que vai para o falante (na saída do nosso amplificador).

+++

Aqui o que está ilustrado, e o que eu comentei a depender das relações
de amplitudes pode ser que nosso vout pode ser muito maior do que o
sinal de interesse, tá e pra colocar um exempli bem prático, vocês já
devem ter percebido por exemplo, se vocês tocarem na ponta de um
osciloscopio você vai observar um sinal de 60hz, por vezes centenas de
milivolts. Por que a gente vive imerso em campos de 60hz já que a gente
tem  as antenas imensas que são os fios de toda rede elétrica que nos
circuinda.

Então a gente observa também os 60 hz quando a gente toca por exemplo
na ponta de um microfone, se você tiver por exemplo um microfone com
acesso, se você tocar com o dedo, você vai escutar um barulho bem
grande.

Então como é que a gente faz, estando imerso nesses campos de 60hz como
é que a gente faz, por exemplo pra medir sinais de ECG, aqueles sinais
que a gente coloca os eletrodos ao longo do corpo e sabendo que sinais
de ecg são muito pequenos ao passo em que o nosso corpo está imerso em
sinais de 60hz por vezes de grande amplitude

+++

Então como é que a gente faz? Este é por exemplo uma das grandes
aplicações dos pares diferenciais, é o de tornar os sistemas mais
imunes a ruido.

Então o par diferencial é esse, que está mostrado em principio.
primeiramente vamos mostrar esse circuito que está ai abaixo, depois
vamos completar com a polarização.

Então ele tem transistores cujos emissores estão conectados, e também
com resistências de coletores que a gente supõe identicas (rc1 = rc2).
Então na ausencia de sinal, supondo que o microfone tem ausencia de
sinal (tensão nula), e supondo que as tensões de polarização são
idênticas, tanto na base de q1 quanto na base de q2; a tensõa no ponto
x vai ser, vcc menos rc1 vezes a corrente de coletor de q1, e essa
tensão no ponto x ela vai obviamente depender de vcc.

A tensão no ponto y vai ser vcc também, menos rc2 que multiplica a
corrente ic de q2. Então essa tensão no ponto y também depende de vcc.
Então se eu tiver um ripple em vcc esse ripple vai passar tanto para o
ponto x quanto para o ponto y. Mas se eu ao invés de tomar o ponto x em
relação ao terra, ou o ponto y em relação ao terra, tomar o ponto x em
relação ao ponto y vai haver a mesma flutuação em x e em y e de forma
que neste caso não haverá observação do ripple em vout.

Quando agora eu tiver sinal desse lado esquerdo aqui mostrado, então
neste caso, eu vou ter... o vx menos vy é igual ao vin (sinal de
entrada) multiplicado pelo ganho de tensão que a gente vai analizar.
Então o ripple desaparece nesse caso e essa é a grande vantagem. Então
se eu tiver 60hz de um lado e 60hz do outro e eu fizer a diferença,
então eu vou anular os 60hz. Só vou multiplicar a diferença de um
eletrodo em relação ao outro.

+++

Aqui fica explícito se eu aplicar o mesmo sinal em ambas as entradas.
Então eu tenho nesse caso a aplicação do sinal, através de capacitores
de acoplamento, o mesmo sinal aplicado na base de q1 e na base de q2.
Então eu vou ter no ponto x, vcc, composto de ripple, menos rc1 vezes a
corrente ic de q1 que é controlado por vin. Mas, também, do mesmo jeito
eu vou ter que a tensão no ponto y é vcc, que pode ter ripple, menos
rc2 vezes a corrente ic de q2, que também é controlado pela polarização
óbvio, mais o mesmo sinal de vin.

então nesse caso, a tensão no ponto vx é a mesma no ponto vy. Portanto
a diferença ai entre x e y também será nula. Isso acontece, nesse caso,
ao que a gente chama de sinal de modo comum. Então os 60hz seria esse
caso aplicado aos dois eletrodos. é preciso saber que o comprimento de
onda de 60hz, uma coisa que voces vao ver mais pra frente, ele é muito
grande, a priori não tem grande diferença independentemente da parte do
corpo, a gente teria praticamente o mesmo sinal qualquer que seja a
parte do corpo. Mas um eletrodo colocado no braço ele vai ter um sinal
diferente de um eletrodo de um eletrodo colocado na perna em termos do
sinal de eletrocardiograma. O sinal de 60hz ele vai ser praticamente o
mesmo, e o sinal de eletrocardiograma esse sim vai haver uma diferença
entre os dois pontos.

Então nesse caso a gente amplifica somente as diferenças então por isso
que a gente chama de par diferencial.

+++

Então a gente começa agora com esse par diferençal mais completo, então
ele tá polarizado aqui com uma fonte de corrente aqui embaixo. Agora
que a gente já viu como fazer uma fonte de corrente. Voces podem
utilizar um espelho de corrente ai para substituir o iee, e aqui a
gente tem mos transistores com os emissores acoplados e as duas
resistências rc identicas aqui e a alimentação vcc.

Agora, no caso dos estímulos a gente está chamando a tensão de entrada
vin1 aqui na base de q1 e vin2 na base de q2. Então vejam que a o que a
gente pode dizer nesse momento é que iee é igual a corrente de emissor
de ie1 mais a corrente de emissor ie2. okay?

+++

Pra simplificar a análise a gente vai adotar um beta muito grande, em
outras palavras podemos dizer que a corrente de coletor será igual a
corrente de emissor. Portanto, dessa forma ne? a corrente de emissor do
transistor q1 ie1 é igual a ic1 que é igual a is exponencial a vbe1
sobre vt (fazendo eta igual a zero), estamos suprimindo o termo menos
um da exponencial porque is é uma corrente muito pequena. Da mesma
forma ie2 igual a ic2 que é igual a is exponencial de vbe2 sobre vt.

E o nosso vbe1 menos vbe2, já que os nossos emissores estão acoplados,
então vbe1 menos vbe2 é vb1 menos vb2. quem é vb1? é vin1. Quem é vb2?
é vin2. Entõa se vocês fizerem uma relação entre as correntes... aqui é
pura matemática, então aqui ie1 sobre ie2 aí é exponencial de vbe1
menos vbe2 dividido por vt, e a gente já viu que vbe1 menos vbe2 é vin1
menos vin2. Então a gente vai chamar isso aqui de z onde x é a diferença
de tensão nas entradas, reportada a vt. Então a diferença dividido por
vt.

Então como a soma das correntes de emissor é igual a iee, que é
controlado por corrente, a gente chega as seguintes expressões: ie2 é
igual a iee que mutiplica e elevado a menos z dividido por um mais e
elevado a menos z. ie1 é ugual a iee que multiplica e elevado a z
dividido por um mais e elevado a z.

+++

Agora, se voces fizerem um pouco mais de matemática. então aqui tem as
expressões que vocês podem repetir em casa, então a gente vai chegar à
conclusão de que a nossa corrente de emissor é igual a iee sobre dois,
então metade dessa corrente de polarização, então iee, a corrente total.

iee sobre dois que multiplica um mais tangente hiperbolica de z sobre
2, lembrando que z é zin1 menos zin2 dividido por vt. Então ie2 é a iee
sobre dois, a mesma coisa, né? que multiplica por um menos tangente
hiperbolica de z sobre 2. Então se voce somar nessas equaçòes aqui ie1
mais ie1, vai ficar iee sobre dois que multiplica um mais tangente
hiperbolica de z sobre dois mais iee sobre dois mais um menos tangente
hiperbolica de z sobre dois. O que dá iee sobre dois que multiplica
dois, ou seja iee.

Então aqui, já que a gente tem as correntes de emissor que a gente tá
supondo aqui, desprezando beta, que é igual a corrente de coletor,
então o vout 1 vai ser vcc menos rc que multiplica ie1. Então da mesma
forma a gente tira aqui vout2, igual a vcc menos rc vezes ie2. Então
nosso vout que a gente já disse que é a  gente ia tirar a tensão
diferencial, sendo igual a vout1 menos vout2, vai ser dado por rc,
então vcc corta, vejam aí que é justamente essa vantagem, então vejam
aí que o vcc *e seu ripple* eles são suprimidos da equação. Então vai
ser igual a rc que multiplica ie2 menos ie1, que é igual, se você
utilizar as expressões anteriores, então vai ser dado por menos iee, a
corrente de polarização, vezes rc, que multiplica a tangente
hiperbolica de z sobre dois.

+++

Então se a gente pegar as expressões anteriores, tanto de ic1 (no caso
era de ie, mas a gente está supondo ic igual a ie), então agui a gente
vai ter uma curva em relação de vin1 e vin2 das correntes ic1 e ic2, né?
vejam só, então tanto analizando aqui nesse gráfico superior as
correntes como no gráfico inferior as tensoes. Então vejam só que
quando vin1 menos vin2 for igual a zero, veja ambas as tensões são
identicas, as correntes ic1 e ic2 vão ser dadas por iee sobre 2, normal,
né? Então os transisotres estão com os emissores conectados com as
bases com mesma tensão, são transistores identicos, então conduzirão
necessáriamente a mesma corrente. O total sendo iee, então conduzirão
iee sobre dois. Esse vai ser o valor.

Então se a gente fizer aqui nessas expressões de corrente de coletor,
se a gente fizer variar v1 menos v2, em que z é igual a v1 menos v2
sobre vt. Então a gente varia aqui partingo de 50mV. Então voces
percebam que para uma variação por exemplo de 25mv a gente tem 72.5%
da corrente iee vai ser conduzida pelo transistor q1 enquanto 27.5%
será conduzida pelo transistor q2.

Se por outro lado houver uma diferença de menos 50mV, então 87.4% da
corrente iee será conduzida pelo transistor q2 e apenas 12.6% da
corrente iee (total de polarização) será conduzida pelo transistor q1.

Então aqui em termos de tensão, quando vin1 menos vin2 é igual a zero,
então a gente já tem que as correntes ic1 e ic2 serão as mesmas e dadas
por iee sobre 2, então as tensões vão ser as mesmas e dadas por vcc
menos rc que multiplica a corrente de coletor no transistor que é iee
sobre dois.

+++

Slide 27

Determinação da excursão do sinal em modo comum na base dos transistores. Essa caracterização
é importante pois define os valores máximos e mínimos que um sinal em modo comum pode ter para que
o amplificador diferencial continue desprezando esse sinal.

Isso acontece pois como os amplificadores estarão sujeitos à situações invertidas, pois o sinal em modo
comum estará
