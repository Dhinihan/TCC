# Log

## Extraindo informações

#### Classificação

- Os posts de perguntas serão classificados nos sequintes tipos
  - Perguntas do tipo **"O Que?"**: A possível solução que o usuário propõe apresenta algum erro
  - Perguntas do tipo **"Como?"**: O usuário ainda não identificou uma possível solução
  - Perguntas do tipo **"Por Que?"**: O usuário sabe uma solução, mas quer entendê-la melhor. Ou o usuário gotaria de entender melhor as suas possibilidades
  - Perguntas não relacionadas ao dbunit

- Criarei um campo no banco de dados com o nome question_type que apenas será aplicável a posts com post\_type\_id = 1

- Criaei o script classify\_posts.py que sorteará uma pergunta e podirá que a classifique com números de 1 a 4 a partir da seguinte regra:
  - Perguntas do tipo "O Que?": 1
  - Perguntas do tipo "Como?": 2
  - Perguntas do tipo "Por Que?": 3
  - Perguntas não relacionadas ao dbunit: 4

- Algumas perguntas são marcadas com o valor 6, indicndo que precisarei avaliá-las com mais cuidado

- Durante a leitura, várias perguntas relacionadas a banco de dados com multiplos schemas

- Quando as perguntas foram "Dbunit é a melhor forma? Ou deveria usar outra ferramenta", classifiquei no "por que"

- Algumas perguntas envolvem a integração de várias bibliotecas e o dbunit é apenas uma delas, mesmo assim classifiquei as perguntas dentro de (1,2,3)

- Considerei questões que citavam dbunit apenas para descartá-lo como uma opção viável no tipo 4

- Bibliotecas que aparentemente aparecem junto com dbunit: arquillian, spring, unitils

- Mesmo que a resposta da questão possa ser "Use dbunit", se a pergunta não citar dbunit, classifiquei com 4

#### Extração de informações em gráficos e tabelas

- As seguintes informações puderam ser extraídas diretamente dos dados
  - [Perguntas por Tipo]()
  - Perguntas por Tipo Desconsiderando Não Relevantes
  - Respostas por Tipo de Pergunta
  - Respostas por Tipo de Pergunta Desconsiderando Não Relevantes
  - Perguntas por Presença de Resposta Aceita
  - Perguntas por Presença de Resposta
  - Perguntas por Presença de Resposta e Resposta Aceita
  - Perguntas dividas pela presença de código
  - Respostas dividas pela presença de código
  - Domínios mais Frequentes em Respostas
  - Domínios mais Frequentes em Perguntas
  - Dados Agregados Sobre o Tempo até a Resposta Aceita
  - Dados Agregados Sobre o Tempo até uma Resposta
  - Número de perguntas por ano

- Todos os gráficos foram gerados por scripts em python para facilitar a reconstrução dos mesmos, além de documentar o método de extração

## TODO

- Organizar log antigo
- Melhorar organização dos scripts