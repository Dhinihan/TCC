# Log

## Extraindo informações

#### Classificação

- Os posts de perguntas serão classificados nos sequintes tipos
  - Perguntas do tipo **"O Que?"**: A possível solução que o usuário propõe apresenta algum erro
  - Perguntas do tipo **"Como?"**: O usuário ainda não identificou uma possível solução
  - Perguntas do tipo **"Por Que?"**: O usuário sabe uma solução, mas quer entendê-la melhor. Ou o usuário gotaria de entender melhor as suas possibilidades
  - Perguntas não relacionadas ao dbunit

- Criarei um campo no banco de dados com o nome question_type que apenas será aplicável a posts com post\_type\_id = 1

- Criarei o script [classify_posts](scripts/classify_posts.py) que sorteará uma pergunta e podirá que a classifique com números de 1 a 4 a partir da seguinte regra:
  - Perguntas do tipo "O Que?": 1
  - Perguntas do tipo "Como?": 2
  - Perguntas do tipo "Por Que?": 3
  - Perguntas não relacionadas ao dbunit: 4

- Algumas perguntas são marcadas com o valor 6, indicndo que precisarei avaliá-las com mais cuidado

- Durante a leitura, várias perguntas relacionadas a banco de dados com multiplos schemas

- Quando as perguntas foram "Dbunit é a melhor forma? Ou deveria usar outra ferramenta", classifiquei no "por que"

- Algumas perguntas envolvem a integração de várias bibliotecas e o dbunit é apenas uma delas, mesmo assim classifiquei as perguntas dentro de (1,2,3)

- Considerei questões que citavam dbunit apenas para descartá-lo como uma opção viável no tipo 4

- Bibliotecas que aparentemente aparecem junto com dbunit: arquillian, spring, unitils, phpunit

- Mesmo que a resposta da questão possa ser "Você deveria usar dbunit", se a pergunta não citar dbunit, classifiquei com 4

#### Extração de informações em gráficos e tabelas

- As seguintes informações puderam ser extraídas diretamente dos dados
  - [Postagens dividas por perguntas e respostas](attachments/postagens_dividas_por_perguntas_e_respostas.png)
  - [Perguntas por Tipo](attachments/perguntas_por_tipo.png)
  - [Perguntas por Tipo Desconsiderando Não Relevantes](attachments/perguntas_por_tipo_desconsiderando_não_relevantes.png)
  - [Respostas por Tipo de Pergunta](attachments/respostas_por_tipo_de_pergunta.png)
  - [Respostas por Tipo de Pergunta Desconsiderando Não Relevantes](attachments/respostas_por_tipo_de_pergunta_desconsiderando_não_relevantes.png)
  - [Perguntas por Presença de Resposta Aceita](attachments/perguntas_por_presença_de_resposta_aceita.png)
  - [Perguntas por Presença de Resposta](attachments/perguntas_por_presença_de_resposta.png)
  - [Perguntas por Presença de Resposta e Resposta Aceita](attachments/perguntas_por_presença_de_resposta_e_resposta_aceita.png)
  - [Perguntas divididas pela presença de código](attachments/perguntas_divididas_pela_presença_de_código.png)
  - [Respostas divididas pela presença de código](attachments/respostas_divididas_pela_presença_de_código.png)
  - [Domínios mais Frequentes em Respostas](attachments/domínios_mais_frequentes_em_respostas.pdf)
  - [Domínios mais Frequentes em Perguntas](attachments/domínios_mais_frequentes_em_perguntas.pdf)
  - [Dados Agregados Sobre o Tempo até a Resposta Aceita](attachments/dados_agregados_sobre_o_tempo_até_a_resposta_aceita.pdf)
  - [Dados Agregados Sobre o Tempo até uma Resposta](attachments/dados_agregados_sobre_o_tempo_até_uma_resposta.pdf)
  - [Número de perguntas por ano](attachments/número_de_perguntas_por_ano.png)

- Todos os gráficos e tabelas foram gerados pelo script [make_plots](scripts/make_plots.py)

#### Primeiro rascunho: resultados preliminares

- **Revisão**: Questões de pesquisa
  - Q1​: Qual é o tipo de pergunta mais feita pelos usuários do dbunit no Stack Overflow.
  - Q2​: ​Quais são os temas mais comuns nas postagens do Stack Overflow relacionadas ao dbunit como.
  - Q3​: Qual é a qualidade das respostas oferecidas pelos usuários do site.
  - Q4​: As diferenças entre as dificuldades dos usuários do dbunit e de outras tecnologias de desenvolvimento de software.

- Análise dos dados

- Possíveis referências:
  - Nasehi SM, Sillito J, Maurer F, Burns C (2012) What makes a good code example? A study of programming Q&A in StackOverflow. In: Proceedings of the 2012 IEEE International Conference on Software Maintenance (ICSM’12). IEEE Computer Society, Washington, DC, pp 25–34
  -  Parnin C, Treude C, Grammel L, Storey MA (2012) Crowd documentation: exploring the coverage and the dynamics of API discussions on Stack Overflow. Technical Report GIT-CS-12-05. Georgia Institute of Technology. http://www.chrisparnin.me/pdf/crowddoc.pdf
  - Souza LBLd, Campos EC, Maia MDA (2014) Ranking crowd knowledge to assist software development. In: Proceedings of the 22nd International Conference on Program Comprehension (ICPC’14). ACM, New York, pp 72–82
  - Treude C, Barzilay O, Storey MA (2011) How Do Programmers ask and answer questions on the Web? (NIER Track). In: Proceedings of the 33rd International Conference on Software Engineering (ICSE’11). ACM, New York, pp 804–807

#### Primeira versão

- **Partes**:
  - Introdução/Motivação
    - Testes automáticos
    - Dificuldades com testes de integração
    - Dbunit
  - Questões de Pesquisa
    - Q1​: Qual é o tipo de pergunta mais feita pelos usuários do dbunit no Stack Overflow.
    - Q2​: ​Quais são os temas mais comuns nas postagens do Stack Overflow relacionadas ao dbunit como.
    - Q3​: Qual é a qualidade das respostas oferecidas pelos usuários do site.
    - Q4​: As diferenças entre as dificuldades dos usuários do dbunit e de outras tecnologias de desenvolvimento de software.
  - Levantamento de dados
    - Separando os dados para o banco de dados
    - Decidindo não usar IA
    - Classificação manual
    - Extração de informações
  - Análise de dados
    - Gráficos dos resultados (Q1)
    - (Q2) é preciso LDA
    - (Q3) é preciso comparar mais, mas há gráficos
    - (Q3) é preciso comparar mais
  - Conclusão / Próximos Passos
    - Ainda há muito a fazer
    - LDA e comparar

#### Extração de temas das postagens (Adiado)

- LDA (Latent Dirichlet Allocation)
  - Extrai tópicos de uma coleção de documentos
  - Atribui uma probabilidade de cada documento participar de um tópico
  - Relaciona cada tópico a palavras mais recorrentes
  - O número de tópicos é definido previamente
  - O método funciona de forma iterativa
  - [Boa referência](http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation)
  - [Biblioteca de python com implementação de LDA](https://pypi.python.org/pypi/lda)

- Testes para melhor captar os tópicos:
  - Documentos puro
  - Documentos sem código
  - Documentos sem código e sem "stop words"
  - Documentos sem código, sem "stop words" e com as palavras stemizadas

- Minerar os textos
  - Criar uma matrix de vocabulários
    - linhas representam postagens
    - colunas representam palavras
    - valores representam frequencia da palavra no documento
  - [Biblioteca de python](https://github.com/dmiro/bagofwords) Para bag of words
  - Sklearn tem implementação de matrix de vocabulários

- log likelihood
  - 1 tópicos:  -25 . 10⁶
  - 2 tópicos:  -25 . 10⁶
  - 3 tópicos:  -26 . 10⁶
  - 5 tópicos:  -26 . 10⁶
  - 8 tópicos:  -27 . 10⁶
  - 13 tópicos: -27 . 10⁶

- Temas
  - exceções com o java
  - integração com outras ferramentas
  - dúvidas gerais


## TODO

- Organizar log antigo
- Melhorar organização dos scripts
