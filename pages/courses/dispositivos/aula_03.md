title: Dispositivos Eletrônicos
aula: 03
menu: courses
date: 2018.2

---
### Unidade 01 : Conceitos gerais, junção PN e Diodos
## Introdução à física da junção PN (1/2)

### Plano de Aula:
* Construção da Junção PN
* Junção PN em equilíbrio termodinâmico
* Junção PN sob polarização inversa

---

## Construção da junção PN

Até aqui estudamos separadamente os efeitos que o processo de dopagem exerce em semicondutores, produzindo elétrons ou lacunas livres. Também vimos que esses portadores de carga se movimentam no cristal de duas maneiras:

1. Através da aplicação de um campo elétrico, o que faz com que os elétrons (lacunas) se movimentam por um fenômeno chamado de deriva (**drift**). Ou seja, para que haja corrente de deriva é necessário campo elétrico.

2. Através do mecanismo de difusão, que establece um movimento de portadoras de carga devido à diferenças de concentração no semicondutor. Ou seja, para que haja corrente de difusão, é necessário que haja gradiente de concentração de portadores.

Podemos supor portanto, que em um semicondutor isolado nenhum dos dois fenômenos ocorre sem a aplicação de uma ação externa. Mas o que acontece quando conectamos (com uma solda metalúrgica imaginária) um cristal composto de Silício dopado com Fósforo (material *tipo-n*) com um cristal de Silício dopado com Boro (material *tipo-p*)?

Para responder a esse questionamento, faremos um exercício de imaginação: Imaginemos que esses dois cristais (tipo-n e tipo-p) existem isoladamente. Devemos assumir primeiramente que as concentrações de portadores em cada material é dada como está representado na figura abaixo

<img class="center" src=/static/figures/ alt="concentracoes_diferentes_materiais">

Quando esses cristais estão em equilíbrio termodinâmico (quando não existe nenhuma força externa sendo aplicada sobre o material, inclusive nenhuma mudança de temperatura), a densidade dos portadores de carga permanece a mesma ao longo de todo o material. No momento \(t=0^-\) em que as superfícies dos dois materiais são conectadas, passará a existir diferentes concentrações de portadores de carga ao longo do material. Por conseguinte, elétrons (e lacunas) darão início a um movimento de difusão pelo componente, na "tentativa" de preencher ambos os lados do componente e igualar a concentração ao longo do cristal formado por duas superfícies cristalinas dopadas inversamente.


## Junção PN em equilíbrio termodinâmico

Em outras palavras: Devemos supor que no instante \(t=0^-\) (quando os materiais acabam de se conectar) as densidades de elétrons e lacunas ainda são as mesmas de quando os materiais estavam isolados. No momento \(t=0\) em que o contato existe, as portadoras de carga dão início a um movimento de difusão, que acontece devido às diferentes concentrações de carga existentes na superfície formada e que agora têm diferentes valores de concentração de portadores em cada polo.

Ora, devemos nos perguntar portanto se esse movimento de portadores acontecerá indefinidamente, ou se essa corrente de difusão terá fim antes do momento em que as concentrações sejam as mesmas em ambos os lados do componente? Lembrando que até aqui não existem forças externas associadas à nosso experimento mental. Ao analisarmos o processo de conexão mais de perto, podemos desenvolver alguns diagramas para melhor entendimento.

<img class="center" src=/static/figures/ alt="imagens_t=1,2,3_do_processo_de_difusão">

Primeiramente sumpomos que os elétrons vão atravessar indefinidamente do material tipo-n (catodo) para o material tipo-p (anodo). Essa suposição seria verdadeira caso existisse no lado esquerdo um suprimento infinito de elétrons, e no lado direito um suprimento de lacunas, o que não é o caso. Perceba que ao passar do lado esquerdo para o lado direito o elétron deixa um íon positivo para trás, o mesmo acontece às lacunas que passam para o lado dopado tipo-n. A cada momento em que mais elétons e mais lacunas são difundidos para o lado de menor gradiente, mais íons (que não têm elétrons ou lacunas) são criados ao longo da junção *pn*.

Em determinado momento (\(t>0\)), os íons que estão presentes ao longo da junção formam um campo elétrico que acelera de volta os elétrons (lacunas) para o seu lado de origem. Nesse momento o componente formado pelo contato dos materiais (tipo-n e tipo-p) é dito em equilíbrio termodinâmico pois a corrente de difusão iniciada após o contato devido às diferentes concentrações em cada material é anulada pela corrente de deriva que existe ao longo da junção devido ao campo elétrico formado pelos íons deixados pelo processo de difusão de elétrons e lacunas. Dizemos então que em equilíbrio termodinâmico as correntes de difusão e deriva no material se anulam, e que:

$$
|I_{deriva,p}|=|I_{difusão,p}| \\
|I_{deriva,n}|=|I_{difusão,n}|
$$

>Os gradientes de concentração de elétrons (lacunas) livres forçam o movimento do material tipo-n (tipo-p) para o material tipo-p (tipo-n). A corrende de difusão gerada pelas diferentes concentrações faz com que íons positivos (negativos) sejam deixados para trás, pois não existe reposição das cargas no componente. Em determinado momento, os íons que agora existem ao longo da junção formam um campo elétrico que acelera os elétrons (lacunas) de volta ao material tipo-n (tipo-p), fazendo com que o componente entre em equilíbrio termodinâmico. Vê-se que nesse momento existe uma barreira potencial no interior do componente que existe devido aos íons posicionados ao longo da junção *pn*.

### Potencial de equilíbrio (\(V_0\))

Ao observarmos a figura abaixo, percebe-se que a diferença de densidades de portadores nos lados *p* e *n* leva (obviamente) a uma quantidade de cargas diferentes em ambos os lados. Podemos supor portanto, que o potencial no lado *p* é diferente do potencial do lado *n*. Ora! Já sabemos que em equilíbrio termodinâmico as correntes de deriva e difusão se anulam e portanto \(|I_{deriva,p}|=|I_{difusão,p}|\). Mas:

$$
|I_{deriva,p}|=|I_{difusão,p}| \\
q\mu_p pE = qD_p\frac{dp}{dx}
$$

Sabe-se, no entanto que \(E=-\frac{dV}{dx}\), e portanto

$$
-\mu_p\frac{dV}{dx}=\frac{D_p}{p}\frac{dp}{dx} \\
-\mu_p\int_{x_1}^{x_2}dV = D_p\int_{x_1}^{x_2}\frac{1}{p}dp \\
V(x_2)-V(x_1)=-\frac{D_p}{\mu_p}\ln{\left[\frac{p_p}{p_n}\right]}
$$

Fazendo \(V_0=V(x_2)-V(x_1)\) o potencial referente à junção pn na condição de equilíbrio termodinâmico. Além disso, sabemos que \(\frac{D_p}{\mu_n}=\frac{kT}{q}\) é a relação de Einstein; que \(p_p\approx N_A\) é a concentração de portadores de carga positivos no lado p (majoritátios) e \(p_n\approx \frac{n_i^2}{N_D}\) é aquantidade de portadores minoritários no lado n. Portanto, podemos reescrever a relação anterior na forma

$$
|V_0|=\frac{kT}{q}\ln{\left[\frac{N_AN_D}{n_i^2}\right]}
$$

Que é o valor do potencial dos terminais do componente formado pela junção pn em estado de equilíbrio termodinâmico.

---
*Exemplo:*
Suponha, por exemplo que uma junção PN formada por Silício dopado com características \(N_A=2\times10^6\,cm^{-3}\) e \(N_D=4\times10^{16}\,cm^{-3}\) e que está em temperatura ambiente (\(T=300\,K\)). Qual é o potencial interno \(V_0\) da junção pn?

*Resposta:*
Sabemos que:

* \(k = 1.38\times10^{-23}\,J/K\)
* \(q = 1.6\times10^{-19}\,C\)

Logo:

$$
V_0=\frac{(1.38\times10^{-23})\times300}{1.6\times10^{-19}}\ln{\left[\frac{(2\times10^{16})\times(4\times10^{16})}{(10^{10})^2}\right]} \\
V_0=0.768758\approx0.769\,V
$$

---

## Junção PN sob polarização reversa

Agora podemos dizer que a junção PN forma um dispositivo de dois terminais, o terminal conectado ao material dopado tipo-p e outro terminal conectado ao material dopado tipo-n. Portanto, a junção pode assumir somente três estados: (1) Quando a tensão aplicada no terminal p é maior do que a tensão aplicada no terminal n - polarização direta, (2) quando a tensão aplicada no terminal tipo n é maior do que a tensão aplicada no terminal tipo p - polarização reversa e (3) quando não existe tensão aplicada em nenhum de seus terminais e a junção PN está em aberto. Perceba que essa é uma idealização do modelo.
