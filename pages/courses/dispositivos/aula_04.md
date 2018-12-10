title: Dispositivos Eletrônicos
aula: 04
menu: courses
date: 2018.2

---

# Dispositivos Eletrônicos
## Unidade 01 : Conceitos gerais, junção PN e Diodos

---

Introdução à física da junção PN (2/2)
======================================

## Plano de Aula:
* Jução PN sob polarização direta
* Características I-V da junção PN

---

##Jução PN sob polarização direta

Na aula anterior estudamos o comportamento físico da junção PN quando conectada à fonte externa em polarização inversa (o potencial mais alto da fonte conectado ao lado do material de tipo-n). Vimos que essa conexão aumenta a barreira potencial que existe ao longo da junção, fazendo com que seja mais difícil que os portadores de carga possam trafegar livremente entre os lados do dispositivo.

Nessa aula, devemos estudar a situação inversa da aula anterior, conectaremos a fonte de tensão sob polarização direta. Nessa situação o potencial mais elevado da fonte é conectado ao material de tipo-p do componente, e o potencial mais baixo é conectado ao lado com material tipo-n. Ora, se na situação anterior a barreira potencial da junção aumentava sob polarização inversa, é de se esperar que ao início de nossa análise devemos supor que em polarização direta a barreira de potencial irá diminiuir, o que de fato acontece.

Ainda do nosso estudo do dispositivo em equilíbrio, vimos que a barreira de potencial determina a capacidade de condução do dispositivo formado pela junção: quanto maior a barreira, menor a corrente que passa pelo componente. Ao se polarizar diretamente esse componente com tensão externa \(V_F\) vê-se que elétrons são **fornecidos** ao lado tipo-n e lacunas ao lado tipo-p, o que faz com que o equilíbrio seja perturbado.

Apesar da perturbação formada pelo fornecimento de elétrons e lacunas, a barreira potencial ainda vai existir enquanto a tensão externa \(V_F<V_0\). No momento em que \(V_F=V_0\) podemos supor que a barreira potencial desaparece e o componente passa a conduzir corrente de difusão, pois os gradientes de concentração ainda são diferentes e não existe mais corrente de deriva forte o suficiente para cancelar a componente de difusão induzida pela fonte extern.

Ora! Mas como determinar a corrente que passa pela junção quando aplicamos uma tensão externa em polarização direta? Ou ainda, devemos supor que a corrente que passa pelo componente deve ser a mesma para qualquer valor de tensão aplicado em polarização direta ao componente? Tudo a seu tempo.

Por hora, vamos lembrar da equação que descreve o cálculo do potencial interno da junção em equilíbrio, que vimos na aula anterior \(|V_0|=\frac{kT}{q}\ln{\left(\frac{p_p}{p_n}\right)}\). E se assumirmos que \(V_T=\frac{kT}{q}\), também conhecido como *tensão térmica* e equivale a \(V_T\approx26\,V\,@\,T=300\,K\). Podmeos reescrever a equação anterior de forma que a concentração de portadores majoritátios do lado *p* em equilíbrio termodinamico seja

$$
p_{n,e}=\frac{p_{p,e}}{\exp{\left(\frac{V_0}{V_T}\right)}}
$$

Podemos supor tabém que quando um potêncial externo é adicionado em polarização direta à esse circuito, o estado de equilíbrio é perturbado, supomos portanto que em estado de polarização direta, as distribuições de portadores positivos pode ser caracterizada pela equação

$$
p_{n,F}=\frac{p_{p,F}}{\exp{\left(\frac{V_0-V_F}{V_T}\right)}}
$$  

Perceba que pelas equações de \(p_{n,e}\) e \(p_{n,F}\) podemos esperar que a concentração de portadores de carga positivas minoritárias (as lacunas que estão no lado do semicondutor tipo-n) seja muito maior no estado de polarização direta do que quando a junção está em equilíbrio termodinâmico. Em outras palavras, o aumento na concentração de portadores minoritários acontece devido a um desequilibrio induzido pela tensão externa aplicada; o que força a junção a passar do estado de equilíbrio para polarização direta. A mudança na concentração de portadores minoritários gerada em ambos os lados proporciona uma mudança na corrente de difusão. Agora devemos avaliar qual é essa variação dos portadores de carga minoritários e seu impacto na corrente de difusão.

Podemos expressar a alteração na concentração de lacunas no lado \(n\) como:
\begin{align}
\Delta p_n&=p_{n,F}-p_{n,e} \\
&= \frac{p_{p,F}}{\exp{\left(\frac{V_0-V_F}{V_T}\right)}} - \frac{p_{p,e}}{\exp{\left(\frac{V_0}{V_T}\right)}}
\end{align}

O que nos leva a
\begin{align}
\Delta p_n&\approx\frac{N_A}{\exp{\left(\frac{V_0}{V_T}\right)}}\,\left[\exp{\left(\frac{V_F}{V_T}\right)}-1\right]
\end{align}

Uma vez que sabemos que \(p_{n,e}\approx N_A\) e que em polarização direta a concentração de portadores majoritátios não varia consideravelmente. De modo similar, devemos supor que a variação da concentração de portadores negativos minoritários \(\Delta n_p\) (lado semicondutor tipo-p), é descrita como
\begin{align}
\Delta n_p&\approx\frac{N_D}{\exp{\left(\frac{V_0}{V_T}\right)}}\,\left[\exp{\left(\frac{V_F}{V_T}\right)}-1\right]
\end{align}

Reforçamos aqui a relação de causa e efeito que acontece devido a polarização direta da junção que faz com que aumente a concentração de portadores minoritários em ambos os lados do dispositivo, o que por conseguinte sugere que as correntes de difusão de portadores devem aumentar proporcionalmente além de seus valores de equilíbrio. Podemos então assumir que:
\begin{align}
I_{tot,F}&\propto \Delta p_n + \Delta n_p \\
         &\propto \frac{N_A}{\exp{\left(\frac{V_0}{V_T}\right)}}\,\left[\exp{\left(\frac{V_F}{V_T}\right)}-1\right] +
                  \frac{N_A}{\exp{\left(\frac{V_0}{V_T}\right)}}\,\left[\exp{\left(\frac{V_F}{V_T}\right)}-1\right] \\
         &\propto \frac{(N_A+N_D)}{\exp{\left(\frac{V_0}{V_T}\right)}}\,\left[\exp{\left(\frac{V_F}{V_T}\right)}-1\right] \\
I_{tot,F}&= I_S\,\left[\exp{\left(\frac{V_F}{V_T}\right)}-1\right] \\
\end{align}

De onde introduzimos \(I_S\propto{(N_A+N_D)}/{\exp{\left(\frac{V_0}{V_T}\right)}}\), assim chamada de *corrente de saturação reversa*. Lembre ainda que na aula anterior definimos \(\exp{\left(\frac{V_0}{V_T}\right)}=N_AN_D/n_ i^2\). Portanto, podemos dizer ainda que
\begin{align}
I_S\propto\frac{(N_A+N_D)}{N_AN_D}\,n_i^2 \\
I_S\propto n_i^2\,\left[\frac{1}{N_A}+\frac{1}{N_D}\right] \\
\end{align}

A equação anterior indica que a corrente de saturação reversa de uma junção pn é função do semicondutor utilizado, dada pela densidade de portadores no semicondutor intrínseco, e da quantidade de átomos dopantes tipos doadores e aceitadores. De fato, pode-se provar que

$$
I_S=Aqn_i^2\,\left[\frac{D_n}{N_AL_n}+\frac{D_p}{N_DL_p}\right]
$$

Onde na equação \(A\) é a área da seção reta do dispositivo; \(L_n\) e \(L_p\) são *comprimento de difusão* de elétrons e de lacunas, respectivamete, sua ordem de grandeza é dada em dezenas de micrômetros. O desenvolvimento dessa equação é encontrado em livros mais avançados de semicondutores, como por exemplo [esse](https://www.amazon.com/Physics-Semiconductor-Devices-Simon-Sze/dp/0471143235/ref=sr_1_8?ie=UTF8&qid=1544391374&sr=8-8&keywords=of+Semiconductor+Devices) ou [esse](https://www.livrariadafisica.com.br/detalhe_produto.aspx?id=144433&titulo=Materiais+e+dispositivos+eletr%C3%B4nicos).

---
*Exemplo:*
Determine a corrente \(I_S\), para uma junção com as seguintes características:

* \(N_A=2\times10^{16}\,cm^{-3}=2\times10^{22}\,m^{-3}\)
* \(N_D=4\times10^{16}\,cm^{-3}=4\times10^{22}\,m^{-3}\)
* \(A=100\,\mu m^{2}=0.1\times10^{-9}\,m^2\)
* \(L_n=20\,\mu m=20\times10^{-6}\,m\)
* \(L_p=30\,\mu m=30\times10^{-6}\,m\)
* \(T=300\,K\)

*Resposta:*
Da aplicação direta da equação, e do fato que conhecemos

* \(n_i@300\,K\approx 1.08\times10^{10}\,cm^{-3}=1.08\times10^{16}\,m^{-3}\)
* \(q=1.6\times10^{-19}\,C\),
* \(D_n=34\,cm^2/s=34\times10^{-4}\,m^2/s\)
* \(D_p=12\,cm^2/s=12\times10^{-4}\,m^2/s\)

temos que:
\begin{align}
I_S&=Aqn_i^2\,\left[\frac{D_n}{N_AL_n}+\frac{D_p}{N_DL_p}\right] \\
   &=(0.1\times10^{-9})
      (1.6\times10^{-19})
      (1.08\times10^{16})^2
      \,\left[
        \frac{34\times10^{-4}}{(2\times10^{22})(20\times10^{-6})}+
        \frac{12\times10^{-4}}{(4\times10^{22})(30\times10^{-6})}
      \right] \\
   &=1.77\times10^{-17}\,A
\end{align}

Nota: Todos os valores foram passados para as unidades inteiras do SI (\(m\)), de tal forma que a corrente é dada em Coulomb por segundo. Tente fazer o mesmo exercício utilizando as subunidades dos valores, por exemplo em \(um\).

---

A partir do nosso exemplo, podemos concluir que a tensão de polarização inversa \(I_S\) por si só não contribui substancialmente para a corrente que passa pela junção. Além disso, como \(I_S\) é uma corrente muito pequena, é preciso que o termo exponencial deva assumir valores muito elevados para que a corrente \(I_{tot,F}\) assuma valores úteis, como por exemplo \(1\,mA\).

## Características I-V da junção PN

Até aqui estudamos separadamente os três estados possíveos de polarização da junção PN, a polarização direta, que acontece quando a tensão externa se sobrepôe ao potencial interno do dispositivo e força corrente de difusão . Sob polarização reversa, a barreira potencial no entorno da junção PN aumenta e inibe o fluxo de portadoras (consequentemente de corrente). E o equilíbrio estático, quando não existe nenhuma ação externa aplicada ao componente.

Em polarização direta, concluímos que a corrente total que passa pelo dispositivo formado pela junção dos dois materiais semicondutores dopados é dada por
\begin{align}
I_{D}&= I_S\,\left[\exp{\left(\frac{V_D}{V_T}\right)}-1\right]
\end{align}

A equação acima denota o comportamento da junção PN sob polarização direta mas também pode ser utilizada para modelar o comportamento da junção em polarização inversa até determinado valor. Perceba no entanto que essa equação denota a resposta da junção com restrições específicas impostas, notadamente valores de polarização \(V_D\) específicos. Por exemplo, caso a tensão \(V_D\) seja muito elevada, é provável que o diodo queime visto que a corrente \(I_D\) que passa antravés da junção é de carcaterística exponencial em relação à tensão \(V_D\) e, portanto, pode rapidamente alcançar valores que o componente não pode suportar.

Ainda sobre a equação de corrente \(I_D\), vemos que rapidametne este termo é maior do que um quando a tensão \(V_D\) aumenta. Como na equação a corrente \(I_S\) que é muito pequena, multiplica ambos os termos, podemos em algumas situações assumir que a relaão I-V do diodo pode ser reduzida para:
\begin{align}
I_{D}&= I_S\,\exp{\left(\frac{V_D}{V_T}\right)}
\end{align}

Em várias situações essa é a relação I-V que utilizaremos para modelagem do diodo.
