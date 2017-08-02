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
  - [Perguntas por Tipo](attachments/perguntas_por_tipo.png)
  - [Perguntas por Tipo Desconsiderando Não Relevantes](attachments/perguntas_por_tipo_desconsiderando_não_relevantes.png)
  - [Respostas por Tipo de Pergunta](attachments/respostas_por_tipo_de_pergunta.png)
  - [Respostas por Tipo de Pergunta Desconsiderando Não Relevantes](attachments/respostas_por_tipo_de_pergunta_desconsiderando_não_relevantes.png)
  - [Perguntas por Presença de Resposta Aceita](attachments/perguntas_por_presença_de_resposta_aceita.png)
  - [Perguntas por Presença de Resposta](attachments/perguntas_por_presença_de_resposta.png)
  - [Perguntas por Presença de Resposta e Resposta Aceita](attachments/perguntas_por_presença_de_resposta_e_resposta_aceita.png)
  - [Perguntas dividas pela presença de código](attachments/perguntas_dividas_pela_presença_de_código.png)
  - [Respostas dividas pela presença de código](attachments/respostas_dividas_pela_presença_de_código.png)
  - [Domínios mais Frequentes em Respostas](attachments/domínios_mais_frequentes_em_respostas.pdf)
  - [Domínios mais Frequentes em Perguntas](attachments/domínios_mais_frequentes_em_perguntas.pdf)
  - [Dados Agregados Sobre o Tempo até a Resposta Aceita](attachments/dados_agregados_sobre_o_tempo_até_a_resposta_aceita.pdf)
  - [Dados Agregados Sobre o Tempo até uma Resposta](attachments/dados_agregados_sobre_o_tempo_até_uma_resposta.pdf)
  - [Número de perguntas por ano](attachments/número_de_perguntas_por_ano.png)

- Todos os gráficos e tabelas foram gerados pelo script [make_plots](scripts/make_plots.py)

## TODO

- Organizar log antigo
- Melhorar organização dos scripts