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