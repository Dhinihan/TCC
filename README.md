# Percepção coletiva da comunidade de desenvolvimento em relação ao dbunit

## Composição do repositório

Este repositório é composto pelos seguintes elementos:

- Pasta scripts: Os scripts utilizados para a extração dos dados que deram base à pesquisa.
- Pasta www: O site que guarda o trabalho.
- Pasta attachments: Os gráficos que foram gerados durante a pesquisa
- Pasta backup: Os dados utilizados durante a pesquisa

## Resumo do Trabalho

Neste trabalho estudamos a percepção geral da comunidade de desenvolvedores de software em relação a ferramenta dbunit. O dbunit é uma extensão do Junit feita para controlar o estado do banco de dados antes de cada teste. Ele é a principal ferramenta para integração de testes automáticos com o banco de dados em Java, além de ter versões para outras linguagens como php e .NET. Para isso analisamos perguntas e respostas no site Stack Overflow relacionadas a esta ferramenta.

Desta forma nos propusemos a responder às seguintes questões de pesquisa: Qual é o tipo de pergunta mais feita pelos usuários do dbunit no Stack Overflow? (Q1); Quais são os temas mais comuns nas postagens do Stack Overflow relacionadas ao dbunit. (Q2); Qual é a qualidade das respostas oferecidas pelos usuários do site (Q3); e As diferenças entre os usuários do dbunit e de outras tecnologias de desenvolvimento de software no Stack Overflow (Q4).

Em relação à Q1 descobrimos que há um empate entre questões do tipo “O que?” e “Como?” e um menor número de perguntas do tipo “Porquê”, mas estas são praticamente duas vezes mais visualizadas do que os outros dois tipos de questões. Esse tipo de distribuição não é incomum para outras ferramentas. Em relação à Q2 encontramos três temas que se destacam: “Exceções e problemas com o Maven”, “Dúvidas gerais sobre o dbunit” e “Integração com outras ferramentas” sendo que este último tema além de ser o mais presente, concentra a maioria das perguntas do tipo “Por quê”. Em relação à Q3 descobrimos que a grande maioria das perguntas são respondidas e quase metade delas tem uma resposta aceita que é próximo da média do site. Finalmente em relação a Q4 descobrimos que o dbunit mostrou um incremento de perguntas no início do Stack Overflow e se estabilizou nos últimos anos e que este crescimento segue o padrão do próprio Stack Overflow. Porém o dbunit tem um número pequeno de mais de perguntas se comparado com outras ferramentas como Hibernate e Spring que aparecem frequentemente juntos com o dbunit nas perguntas do site.

## Scripts

Diversos scripts foram utilizados neste trabalho, segue uma explicação dos principais:

### crawler-questions.py

Este script percorre o arquivo com um dump de todas as postagens do Stack Overflow no formato xml e salva no banco de dados todas as questões que contenham o texto *dbunit* no corpo.

### crawler-answers.py

Este script percorre o arquivo com um dump de todas as postagens do Stack Overflow no formato xml e salva no banco de dados todas as respostas às questões marcadas como relacionadas com o dbunit.

### classify-posts.py

Este script foi utilizado para classificar manualmente os tipos de postagens relacionadas com o dbunit encontradas no stack overflow. A cada iteração ele sorteia um script ainda não classificiado, formata o texto para facilitar a visualização no terminal e registra a classificação digitada pelo usuáro no banco de dados. As classificações possíveis são

- "O quê"
- "Como"
- "Por quê"
- "Não referencia diretamente dbunit"

### extract-themes.py

Este script seleciona todas as perguntas  dos tipos *O quê*, *Como* e *Por quê* e atribui uma probabilidade de cada uma delas pertencer a um "tema".
Estes temas são definidos pela recorrência de palavras em comum entre as perguntas.

### make-plots.py

Este script gera diversos gráficos relacionados ao trabalho.

### process-posts.py

Este script salva no banco de dados uma versão do texto com as palavras *stemizadas* e sem as *stop words* para melhorar o desempenho da classificação dos temas com LDA

### view-themes.py

Este script mostra as perguntas de um dos temas encontrados no script *extract-themes.py* na ordem de probabilidade da postagem participar do tema. A opção *--topic* recebe o índice do tópico que será visualizado. A opção *--n-posts* recebe o número de post para mostrar. A opção *--assending* pode ser marcada para mostrar as postagens com menor probablidade de pertencer ao tópico.


### outros scripts

Os outros scripts deste trabalho são auxiliares aos scripts mencionados neste documento. Não são implementados para que sejam executados separadamente.
Para configurar o banco de dados que estes scripts irão consumir é necessário editar o script *connection.py*


## Gráficos

A pasta *attachments* contém diversos gráficos utilizados neste trabalho. Segue um índice com os links diretos para as imagens:

- [Dados Agregados Sobre O Tempo Até A Resposta Aceita](attachments/dados_agregados_sobre_o_tempo_até_a_resposta_aceita.pdf)
- [Dados Agregados Sobre O Tempo Até Uma Resposta](attachments/dados_agregados_sobre_o_tempo_até_uma_resposta.pdf)
- [Domínios Mais Frequentes Em Perguntas](attachments/domínios_mais_frequentes_em_perguntas.pdf)
- [Domínios Mais Frequentes Em Respostas](attachments/domínios_mais_frequentes_em_respostas.pdf)
- [Média De Respostas Por Pergunta](attachments/média_de_respostas_por_pergunta.png)
- [Número De Perguntas Por Ano - Dbunit](attachments/número_de_perguntas_por_ano_-_dbunit.png)
- [Número Médio De Visualizações Por Tema](attachments/número_médio_de_visualizações_por_tema.png)
- [Número Médio De Visualizações Por Tipo De Pergunta](attachments/número_médio_de_visualizações_por_tipo_de_pergunta.png)
- [Perguntas Divididas Pela Presença De Código](attachments/perguntas_divididas_pela_presença_de_código.png)
- [Perguntas Por Presença De Resposta](attachments/perguntas_por_presença_de_resposta.png)
- [Perguntas Por Presença De Resposta Aceita](attachments/perguntas_por_presença_de_resposta_aceita.png)
- [Perguntas Por Presença De Resposta E Resposta Aceita](attachments/perguntas_por_presença_de_resposta_e_resposta_aceita.png)
- [Perguntas Por Presença De Resposta E Resposta Aceita - Dbunit](attachments/perguntas_por_presença_de_resposta_e_resposta_aceita_-_dbunit.png)
- [Perguntas Por Presença De Resposta E Resposta Aceita - Geral](attachments/perguntas_por_presença_de_resposta_e_resposta_aceita_-_geral.png)
- [Perguntas Por Tema Mais Presente](attachments/perguntas_por_tema_mais_presente.png)
- [Perguntas Por Tipo](attachments/perguntas_por_tipo.png)
- [Perguntas Por Tipo - Android](attachments/perguntas_por_tipo_-_android.png)
- [Perguntas Por Tipo - Swing](attachments/perguntas_por_tipo_-_swing.png)
- [Perguntas Por Tipo Desconsiderando Não Relevantes](attachments/perguntas_por_tipo_desconsiderando_não_relevantes.png)
- [Postagens Dividas Por Perguntas E Respostas](attachments/postagens_dividas_por_perguntas_e_respostas.png)
- [Probabilidade De Uma Pergunta Ser De Um Tema Pelo Seu Tipo](attachments/probabilidade_de_uma_pergunta_ser_de_um_tema_pelo_seu_tipo.png)
- [Proporções De Presença De Resposta Por Tema](attachments/proporções_de_presença_de_resposta_por_tema.png)
- [Proporções De Presença De Resposta Por Tipo De Pergunta](attachments/proporções_de_presença_de_resposta_por_tipo_de_pergunta.png)
- [Respostas Divididas Pela Presença De Código](attachments/respostas_divididas_pela_presença_de_código.png)
- [Respostas Por Tipo De Pergunta](attachments/respostas_por_tipo_de_pergunta.png)
- [Respostas Por Tipo De Pergunta Desconsiderando Não Relevantes](attachments/respostas_por_tipo_de_pergunta_desconsiderando_não_relevantes.png)
- [Tipo De Perguntas Do Tema 1](attachments/tipo_de_perguntas_do_tema_1.png)
- [Tipo De Perguntas Do Tema 2](attachments/tipo_de_perguntas_do_tema_2.png)
- [Tipo De Perguntas Do Tema 2 (integração Com Outras Ferramentas)](attachments/tipo_de_perguntas_do_tema_2_(integração_com_outras_ferramentas).png)
- [Tipo De Perguntas Do Tema 3](attachments/tipo_de_perguntas_do_tema_3.png)
- [Total De Perguntas Por Ano - Geral  ](attachments/total_de_perguntas_por_ano_-_geral.png)

## Banco de Dados

- Na pasta backup há o *dump* mais recente utilizado neste trabalho, segue uma breve explicação do seu esquema:

### post

A tabela post guarda todas as postagens (sejam perguntas ou respostas) que contenham a palavra dbunit no seu corpo. A tabela é composta pelos seguintes atributos:

- **id**: Identificador do post no *Stack Overflow*
- **title**: Título da postagem
- **body**: Corpo do texto sem modificações
- **answer\_count**: Número de respostas
- **accepted\_answer\_id**: Número de respostas
- **creation\_date**: Data de criação da postagem
- **last\_activity\_date**: Data da última atividade da postagem
- **last\_editor\_user\_id**: Id do último usuário que a editou
- **score**: Número de "pontos" atribuídos à postagem pelos usuários do site
- **last\_edit\_date**: Data da última edição da postagem
- **post\_type\_id**: Tipo da postagem (1 - Pergunta, 2 - Resposta)
- **comment\_count**: Número de comentários na postagem
- **view\_count**: Número de visualizações na postagem
- **owner\_user\_id**: Id do usuário que criou a postagem
- **owner\_display\_name**: apelido do usuário que criou a postagem
- **closed\_date**: Data que a postagem foi fechada
- **favorite\_count**: Número de pessoas que favoritaram a postagem
- **last\_editor\_display\_name**: Nome do último usuário que editou a postagem
- **parent\_id**: Id da pergunta respondida pela postagem
- **stemmed\_body**: Corpo do texto simplificado
- **question\_type**: Tipo de pergunta (1 - O quê, 2 - Como, 3 - Porque, 4 - Não Relevante)
- **topics**: Lista de probabilidades de a postagem pertencer ao tema cujo identificador é o índice da lista

### cited\_links

Tabela que guarda informações sobre todos os links citados nas postagens. A tabela é composta pelos seguintes atributos:

- **id**: Identificador do link
- **post**: Post que citou o link
- **link**: Texto do link
- **location**: Domínio do link

### outside\_data

Tabela que guarda informações trazidas de outras fontes para a geração de gráficos. A tabela é composta pelos seguintes atributos:

- **id**: Identificador da informação
- **origin**: Origem da informação
- **description**: Descrição da informação
- **value**: Valor da informação
- **table\_description**: Descrição da tabela ou do gráfico a qual a informação é utilizada

### question\_type

Tabela que guarda os tipos de perguntas utilizadas neste trabalho. A tabela é composta pelos seguintes atributos:

- **id**: Código do tipo de pergunta
- **description**: Descrição do tipo de pergunta

### topic

Tabela que guarda os tópicos encontrados utilizando o script *extract\_themes.py*. A tabela é composta pelos seguintes atributos:

- **id**: Código do tema
- **words**: Palavras que definem o tema
