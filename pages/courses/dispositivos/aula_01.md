title: Dispositivos Eletrônicos
aula: 02
menu: courses
date: 2018.2

---

# Dispositivos Eletrônicos
## Unidade 01 : Conceitos gerais, junção PN e Diodos

---

Princípios de Condução de Corrente Elétrica em Sólidos
======================================================

## Plano de Aula:
* Condutores, Isolantes e Semicondutores.
* Propriedades do Silício Intrínseco.
* Dopagem e seus efeitos (ou sobre como modificar algumas das propriedades do semicondutor).
* Deriva e difusão de portadores.

---

# Portadoras de carga em semicondutores

Sabe-se que a corrente elétrica é definida como o movimento direcionado de elétrons ao longo de uma superfície. Apesar desse conceito parecer simples, existe muitas considerações que precisam ser levadas em consideração para compreender o mecanismo que descreve a corrente elétrica em dispositivos semicondutores. Primeiramente definimos um semicondutor como um material que pode se comportar como condutor ou isolante. No mundo real, a maioria dos semicondutores são formados por cristais de átomos do grupo IV (coluna 14 na [tabela periódica](https://www.ptable.com/?lang=pt)).

Nesse caso, em que situação o semicondutor funcionará como um condutor ou um isolante? Ou de outra maneira, como transformar um semicondutor em um condutor ou em um isolante? Antes de responder essas perguntas devemos primeiramente compreender a passagem o movimento que transforma um elétron da camada de valência em um elétron livre na superfície cristalina formada, por exemplo, por silício.

De acordo com o modelo do átomo de Bohr, os elétrons orbitam o núcleo de um átomo que é formado por prótons e neutrons. Independente das características desse átomo (peso atômico, número de prótons e neutrons, etc.) os elétrons que orbitam esse núcelo podem passar de uma camada para outra e se *desprender* da orbita desse átomo. Para que isso aconteça é necessário que esse elétron receba uma quantidade específica de energia; essa quantidade de energia \(E_g\) assume um valor diferente para cada elemento da tabela periódica.

## Confinamento de elétrons nas camadas do átomo

O movimento de partículas do átomo (incluindo os elétrons) é modelado na física quantica como *ondas de matéria*. De maneira simplificada, as ondas de matéria funcionam como ondas estacionárias. Suponha que uma corda conectada em ambas as extremidades à superfícies fixas seja excitada por harmônicos simples em frequências que variam linearmente, para as cordas fixadas são produzidos padrões de ondas estacionárias somente em certas frequências de excitação (modos).

<img class="center" src=/static/figures/standing_waves.jpg alt="drawing">

Em outras palavras, a onda estacionária gerada pela excitação da corda está confinada devido ao tamanho limitado estabelecido pelas extremidades da corda que estão conectadas às superficies fixas. Além disso, percebemos que as ondas estacionárias geradas pela excitação dessa corda, não assumem qualquer frequência. Dizemos então que a frequência de vibração da corda é quantizada e segue a equação \(L=n\lambda/2\), onde \(L\) é o comprimento da corda, \(n\) é um número inteiro que define a quantidade de modos e \(\lambda\) é a larguda da onda estacionária.

Analogamente ao caso da corda fixa, e como o movimento dos elétrons é modelado por ondas de matéria, supõe-se que os elétrons estão presos (confinados) nas órbitas (modos) do átomo. Um elétron pode saltar de uma órbita a outra de acordo com a quantidade de energia que ele *recebe* (via calor, luz, etc.). Como nesse caso, as órbitas são quantizadas, a quantidade de energia necessária para que um elétron passe de um estado a outro também é quantizado. De uma outra forma, podemos compreender o estado de oscilação do átomo como bandas de energia. Um elétron têm energia o suficiente para estar em determinada banda de energia e pode transpor a barreira (*bandgap*) para uma outra banda de acordo com a energia externa que ele recebe. Esse valor de energia, além de variar de acordo com a banda de energia do elétron, também varia de acordo com o elemento da tabela períódica. Por exemplo, a energia necessária para que um elétron que se encontre na camada de valência se *soltar* do átomo (e virar um elétron livre) no do Silício é de 1.12eV e o do Germânio de 0.66eV.

Finalmente, denomina-se elétron-volt a energia necessária para que um elétron vença a barreira de potencial de 1V, lembrando que um elétron tem carga de \(1.6\times10^{-19}C\).

---

Para entender um pouco melhor a diferença de condutores isolantes e semicondutores é preciso entender a estrutura atômica. Tomemos nesse caso o átomo de hidrogênio isolado, que é o mais simples deles, Bohr estabeleceu que os níveis de energia que os eletrons podem ocupar são níveis discretos e que seguem a equação

$$ E_n=-\frac{mq^4}{8\varepsilon_0^2h^2}\frac{1}{n^2}=\frac{-13,6eV}{n^2}$$

onde n é o número quantico e 1 eV é a quantidade de energia necessária para que um elétron consiga transpor uma barreira de potêncial igual a um volt.

A equação de Bohr estabelece os níveis de energia correspondentes a cada orbita de um átomo. Significando que: Definido por *n*, o número quantico principal estabelece a energia do nível em que se encontra o elétron obedecendo a relação de Bohr da equação anterior.
