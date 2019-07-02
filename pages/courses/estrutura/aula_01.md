title: Estrutura e concepção de circuitos integratos (CMOS)
aula: 01
menu: courses
date: 2018.2

---
### Unidade 01 : Elementos de Projeto em Microeletrônica CMOS
## Contextualização

### Plano de Aula:
* Contextualização e objetivos da disciplina
* O que é design de circuito elétrico
* Demonstração do conjunto de habilidades necessárias
* Notação que será utilizada na disciplina

---

## Contextualização e Objetivos

A microeletronica é uma das áreas da indústria com maior crescimento em pesquisa e desenvolvimento ([ver aqui](https://cic.unb.br/~rjacobi/ensino/Microeletronica/Concepcao1.pdf)). Apesar disso, o conjunto de informações necessárias para o desenvolvimento de um chip eletrônico que desenvolve uma simples tarefa (de amplificação, por exemplo), é muito grande.

O objetivo desse curso, é portanto, fazer com que o aluno aumente esse leque de habilidades necessárias para o desenho de um circuito microeletrônico (sobretudo de circuitos analógicos CMOS). Ao terminar o curso o aluno deverá ser capaz de à partir de um conjunto de especificações:

* Conseguir definir as tarefas que devem ser executadas
* Desenvolver (ou escolher) a topologia do circuito para que a(s) tarefa(s) sejam executadas
* Especificar os componentes do circuito, de forma que o circuito obedeça as especificações
* Executar o projeto do circuito, e executar os testes necessários para que o circuito seja produzido.


<img class="displayed" src="/static/images/analog_ic_process.png" width="70%" height="70%" />


## O que é o design de circuito elétrico?
É exatamente o processo de à partir das especificações, executar etapas para a criação de um circuito (*circuito solução*). O design elétrico requer modelos para criação e verificação do desenho do circuito, envolve testes de robustes e simulações características do circuito. Etapas importantes de um design de circuito elétrico envolvem:

1. Seleção da solução
  * Teste de designs pré existentes
  * Seleção de uma solução
2. Investigação da solução
  * Análise de performance (sem computador)
  * Determinação dos prós e contras da solução
3. Modificação da solução
  * Utilização de princípios chaves, conceitos e técnicas para implementação
  * Avaliação das modificações através de análise (sem computador)
4. Verificação da solução
  * Utilização de simulação com modelos precisos e verificação da solução
  * Teste de resposta: Grandes diferenças entre a *análise manual* e verificação com utilização do computador devem ser cuidadosamente examinadas.


---
*Exemplo:*
