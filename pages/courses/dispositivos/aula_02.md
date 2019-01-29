title: Dispositivos Eletrônicos
aula: 02
menu: courses
date: 2018.2

---
### Unidade 01 : Conceitos gerais, junção PN e Diodos
## Princípios de Condução de Corrente Elétrica em Sólidos

### Plano de Aula:
* Materiais Condutores, Isolates e Semicondutores
* Propriedades do Silício Intrínseco
* Dopagem e seus efeitos (ou sobre como modificar algumas das propriedades do semicondutor)
* Deriva e difusão de portadores

---

## Materiais Condutores, Isolantes e Semicondutores
A física dos cemicondutores tem base no estudo das iteraçãos atômicas e propriedades dos materiais, e explica como estes materiais iteragem eletricamente. A partir desses conceitos, desenvolvemos o estudo dessas iterações físicas, e com a utilização de modelos básicos dos átomos podemos compreender o que faz com que determinado material se torne um condutor, isolante ou semicondutor.

O modelo do átomo de Bohr, estabelece que o átomo tem várias camadas (órbitas) externas de elétrons. Em cada órbita do átomo é estabelecido quantidades específicas de elétrons que caruam de acordo com o número atômico desse átomo. Ou seja, diferentes materiais têm quantidades diferentes de elétrons em sua camada de valência (ultima camada).

A quantidade de elétrons nessa ultima camada fixa o comportamento desse material devido a sua ligação com outros átomos. Exemplos: Sódio (1e- em sua camada de valência), Neon (8e-) e Silício (4e-).

O que estabelece a propriedade elétrica do material (se condutor, isolante ou semicondutor) é a força da ligação atômica entre seus átomos formadores:

1. Isolantes:
  A ligação atômica em materiais isolantes é muito forte. Em geral é formada por ligações iônicas. Por ser muito forte ela não favorece a movimentação de elétrons livres (partículas que carregam carga) em sua superfície. Por isso as características físicas assumidas por esse material em geral envolvem baixa condutividade elétrica e térmica, e alto ponto de fusão.

  Um exemplo de material isolante é o cloreto de sódio (NaCl) formado por átomos de Sódio (com um elétron na camada de valência) e de Cloro (que têm sete elétrons em sua camada de valência).

2. Metais:
  Em geral formados por átomos de material com poucos elétrons fora de sua ultima camada cheia. Esses elétrons são, portanto, fracamente acoplados ao núcleo atômico. A ligação entre os átomos formadores de metais é muito frca e favorece uma alta densidade de elétrons livres.

  Tomemos como exemplo o alumínio (Al), que tem apenas três elétrons em sua camada de valência. Sua ligação com outros átomos de alumínio é feita pelo compartilhamento desses ultimos três elétrons que estão na camada M do átomo (3a camada) que adimite um total de oito elétrons para um subnível p de energia.

  Essa ligação feita pelo compartilhamente de elétrons de camadas incompletas entre átomos do mesmo material, garante ao metal características como maleabilidade e alta condutividade elétrica e térmica, além de baixo ponto de fusão.

  Como essa ligação metálica é feita através do compartilhamento de elétrons entre vários átomos do mesmo material, os átomos (íons positivos) ficam imersos em uma nuvem de elétrons (íons negativos), garantindo uma ligação quasi-iônica.

3. Semicondutores:
  Nesse ultimo caso, a ligação atômica é mais estável do que nos metais. Os átomos desses materiais também dividem seus elétrons na camada de valência, ams se completam de forma a estabilizar em uma estrutura cristalina.

  Tomando como exemplo o material mais utilizado na industria de semicondutores, o Śilício (Si) têm quatro elétrons em sua terceira (e ultima) camada. A estrutura cristalina é formada então okea ligação covalente entre esses átomos.

  A ligação covalente é estabelecida quando átomos compartilham seus elétrons com os átomos vizinhos, completando as camadas de valência entre si.

Até esse ponto, falamos apenas de algumas características físicas dos materiais em relação à suas ligações atômicas. Ao mesmo tempo, devemos notar que essas características são as que estabelecem a qualidade do material: Se isolante, condutor ou semicondutor. Especificamente na situação dos semicondutores, precisamos definir as características de cargas que passam por sua estrutura? Ou ainda *o que* essas cargas carregam? Ou mesmo se existe *mais de um tipo* de carga nesses materiais?

Para organizar o restante do texto, procuraremos daqui para frente responder algumas perguntas importantes:

* De onde vêm as cargas na superfície dos semicondutores?
* Que tipos de portadores de carga existem?
* Como podemos modificar a densidade das portadoras de cargas?
* Como as portadoras de carga se movimentam?

---

## Portadoras de carga e o conceito de bandgap

É sabido que o átomo é formado (simploriamente) por três partículas: O elétron, que têm carga (negativa) de \(Q_e=-1.6\times10^{-19}\), o prótom que têm carga (positiva) de \(Q_e=1.6\times10^{-19}\), e o neutron, que como o nome já sugere, não possui carga. Supenhamos agora que em uma superfície cristalina de Silício, por exemplo, o elétron possa se "soltar" de sua ligação covalente e se movimentar "livremente" pela superfície do cristal.

Como a carga do elétron é negativa, à esse elétron que se "soltou" de sua ligação covalente dá-se o nome de portador de carga negativa, pois agora ele passou a *conduzir* carga ao longo da superfície cristalina. Nessa situação esse elétron *ganhou* energia suficiente para sair de sua camada de valência e entrar na camada de condução.

Esse elétron que ganhou energia e passou da camada de valência para a camada de condução deixou para trás seu espaço na superfície cristalina que têm a mesma módulo da quantidade de carga do elétron mas "carrega" carga positiva.

Ao processo de "descolamento" do elétron da superfície cristalina, que ocorre quando o elétron ganha energia e deixa uma lacuna para trás, dá-se o nome de *geração*, pois ao ganhar energia o elétron se desliga do átomo (superfície) gerando duas partículas portadoras: Um portador de carga negativo (elétron livre) e um portador de cargas positivo (uma lacuna). Perceba que dizemos que o processo de geração gera *dois* portadores de carga, um positivo e um negativo. Isso porque a lacuna deixada pela geração do elétron livre têm características muito parecidas com uma partícula carregada (tem carga positiva, se move ao longo da superfície cristalina,...).

Quando o elétron livre encontra uma lacuna ambos "morrem", fazendo com que ambas as cargas (positiva e negativa) sumam. A esse processo dá-se o nome de *recombinação*. Portanto dois processos complementares são descritos: O processo de geração, quando um elétron se descola da superfície cristalina gerando dois portadores de carga (um positivo e um negativo) ambos de carga \(1.6\times10^{-19}\); e o processo de recombinação, matando ambos os portadores de carga (elétron e lacuna).

---
Um pequeno parêntese é necessário para explicar sobre a movimentação das lacunas ao longo da superfície cristalina. Esse movimento de lacunas acontece na verdade pelo processo de geração e recombinação dos elétrons. O eĺétron se separa no ponto A, gerando uma lacuna e se recombina com uma lacuna no ponto B. Supõe-se então que a lacuna moveu-se do ponto B para o ponto A. A figura abaixo demonstra uma sequência temporal da movimentação das lacunas devido à geração e recombinação de elétrons.

<img class="center" src=/static/figures/ alt="movimento_de_lacunas">

As lacunas se movimentam portanto mais lentamente do que os elétrons, pois seu movimento depende os processos de geração e recombinação, enquanto os elétrons livres podem mover-se livremente pela superfície.

---
### Energia de bandgap:
Quando observa-se experimentalmente a quantidade de elétrons nlivres na superfície de um material semicondutor, percebemos que essa quantidade aumenta com a temperatura. Esse resultado é esperado pois sabe-se que os elétrons ganham energia térmica que faz com que ele transponha a ligação iônica que existe em ele e o núcleo atômico. Em geral a representação gráfica da densidade de elétrons na superfície como função da temperatura pode ser vista como

<img class="center" src=/static/figures/ alt="movimento_de_lacunas">

Esse gráfico estabelece as densidades de elétron na superfície tanto para o Silício como para o Germânio. Ambos os materiais têm quatro elétrons na camada de valência. O gráfico sugere, portanto que a quantidade de elétrons na camada de valência não é suficiente para estabelecer a quantidade de elétrons livres na superfície do material. Existe, portanto alguma outra característica que faz com que a quantidade de elétrons na camada condutora seja maior ou menos para um valor de temperatura estabelecido.

> Se você olhar com calma, preceberá que no silício é preciso mais energia (temperatura mais elevada) para que a densidade de elétrons livres seja a mesma do Germânio em uma temperatura mais baixa. Esta situação sugere que, no silício, o elétron está mais fortemente acoplado à seu núcleo do que no Germânio.

Esta característica é chamada de energia de bandgap, que determina a quantidade de energia necessária para que um elétron salte da camada de vaência para a camada de condução. Alguns valores de exemplos de energia de bandgap para diferentes materiais são:

* Silício: \(E_g=1.12\,eV\)
* Germânio: \(E_g=0.67\,eV\)
* Diamante: \(E_g=2.5\,eV\)

A essa altura, sabemos que a quantidade de elétrons livres aumenta co mo aumento da temperatura, mas como calcular essa quantidade de elétrons livres na superfície cristalina?

---
*Exemplo:*
Calcule a quantidade de elétrons livres na superfície do *Silício intrinseco* à uma temperatura de \(T=300\,K\).

*Resposta:*
A equação \(n_i=5.2\times10^{15}\exp{\frac{-E_g}{2kT}}\,cm^{-3}\) determina a quantidade de elétrons livres na superfície cristalina para o Silício intrínseco. Onde:

* \(T\) -> Temperatura absoluta (dada em Kelvin): \(T=300\,K\)
* \(E_g\) -> Energia de bandgap do material
* \(k\) -> Constante de Boltzmann: \(k=1.38\times10^{23}\,J/K\)

Vemos então que à temperatura ambiente o Silício têm densidade de elétrons aproximada de \(n_i\approx10^{10}\,cm^{-3}\)

---

>Quando o processo de geração acontece em uma superfície cristalina (o elétron ganha energia suficiente para entrar em banda de condução), são gerados dois portadores de carga: Um elétron livre e uma lacuna. Portanto, em um semicondutor intrinseco em temperatura ambiente, supomos \(n(=n_i)\) que é igual a densidade de lacunas (\(p\)). E de acordo com a equação da lei das massas, têm-se que

>$$
np=n_i^2
$$

Lembre-se que em um paralelepípedo de \(1\,cm^{-3}\) a concentração de átomos de Silício é de \(5\times10^{22}\,átomos\cdot cm^{3}\). Calculamos uma densidade de \(n_i\approx10^{10}\,cm^{-3}\) em temperatura ambiente, o que indica que existe uma proporção de \(1:5\times10^{12}\) elétrons livres por átomos de Silício. Logo, concluímos que na melhor das hipóteses o silício é um mau condutor. Essa conclusão nos leva a pergunta de como utilizá-lo como condutor, se sua concentração de portadores de carga é tão reduzida assim? A resposta à essa pergunta é: *devemos modificar a densidade de portadores de corrente*.

## Conceito de Dopagem
O procedimento utilizado na industria para modificar a resitsência de portadores de carga na superfície do Silício interesse é a de dopagem. Esse procedimento consiste em inserir materiais diferentes (impuresas) do Silício de forma a alterar a quantidade de elétrons em sua estrutura cristalina. Usualmente no Silício, dois materiais são mais utilizados para modificar a quantidade de elétrons na trelissa do Silício cristalina, o Fósforo (P), que contém cinco elétrons em sua camada de mais externa, e o Boro (B), com três elétrons em sua camada mais externa.
