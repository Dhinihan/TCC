from tcc_plots import pie
from tcc_plots import table
from tcc_plots import graph

pie.plot("""
SELECT CASE
           WHEN post_type_id = 1 THEN 'Perguntas'
           ELSE 'Respostas'
       END AS descricao,
       count(*) AS n
FROM post
GROUP BY descricao
""",
    "Postagens dividas por perguntas e respostas",
)

pie.plot("""
    SELECT question_type.description, count(*) FROM post
    LEFT JOIN question_type ON question_type.id = post.question_type
    WHERE post_type_id = 1
    GROUP BY question_type.description, question_type.id
    ORDER BY question_type.id
""",
    "Perguntas por Tipo",
)

pie.plot("""
    SELECT question_type.description, count(*) FROM post
    LEFT JOIN question_type ON question_type.id = post.question_type
    WHERE post_type_id = 1
    AND question_type.id <> 4
    GROUP BY question_type.description, question_type.id
    ORDER BY question_type.id
""",
    "Perguntas por Tipo Desconsiderando Não Relevantes",
)

pie.plot("""
    SELECT question_type.description,
           count(*)
    FROM post AS response
    LEFT JOIN post AS question ON question.id = response.parent_id
    LEFT JOIN question_type ON question_type.id = question.question_type
    WHERE response.post_type_id <> 1
    GROUP BY question_type.description,
             question_type.id
    ORDER BY question_type.id
""",
    "Respostas por Tipo de Pergunta",
)

pie.plot("""
    SELECT question_type.description,
           count(*)
    FROM post AS response
    LEFT JOIN post AS question ON question.id = response.parent_id
    LEFT JOIN question_type ON question_type.id = question.question_type
    WHERE response.post_type_id <> 1
      AND question.question_type <> 4
    GROUP BY question_type.description,
             question_type.id
    ORDER BY question_type.id
""",
    "Respostas por Tipo de Pergunta Desconsiderando Não Relevantes",
)

pie.plot("""
    SELECT CASE
               WHEN accepted_answer_id IS NULL THEN 'Perguntas \nsem Resposta \nAceita'
               ELSE 'Perguntas \ncom Resposta \nAceita'
           END AS descricao,
           count(*) AS n
    FROM post
    WHERE post.post_type_id = 1
      AND post.question_type <> 4
    GROUP BY descricao
""",
    "Perguntas por Presença de Resposta Aceita",
)

pie.plot("""
    SELECT CASE
               WHEN EXISTS
                      (SELECT id
                       FROM post AS response
                       WHERE response.parent_id = post.id) THEN 'Perguntas com Resposta'
               ELSE 'Perguntas sem Resposta'
           END AS descricao,
           count(*) AS n
    FROM post
    WHERE post.post_type_id = 1
      AND post.question_type <> 4
    GROUP BY descricao
""",
    "Perguntas por Presença de Resposta",
)

pie.plot("""
SELECT CASE
           WHEN NOT EXISTS
                  (SELECT id
                   FROM post AS response
                   WHERE response.parent_id = post.id) THEN 'Perguntas sem\nResposta'
           WHEN accepted_answer_id IS NULL THEN 'Perguntas sem\nResposta\nAceita'
           ELSE 'Perguntas com\nResposta\nAceita'
       END AS descricao,
       count(*) AS n
FROM post
WHERE post.post_type_id = 1
  AND post.question_type <> 4
GROUP BY descricao
ORDER BY descricao
""",
    "Perguntas por Presença de Resposta e Resposta Aceita - Dbunit",
)

pie.plot(
    """
    SELECT CASE
               WHEN post.body LIKE '%<code>%' THEN 'Com código'
               ELSE 'Sem código'
           END AS descricao,
           count(*) AS n
    FROM post
    WHERE post.post_type_id = 1
      AND post.question_type <> 4
    GROUP BY descricao
    """,
    "Perguntas divididas pela presença de código"
)

pie.plot(
    """
    SELECT CASE
               WHEN question.body LIKE '%<code>%' THEN 'Com código'
               ELSE 'Sem código'
           END AS descricao,
           count(*) AS n
    FROM post as response
    LEFT JOIN post as question ON question.id = response.parent_id
    WHERE response.post_type_id <> 1
      AND question.question_type <> 4
    GROUP BY descricao
    """,
    "Respostas divididas pela presença de código"
)

table.plot(
    """
    SELECT count(*) AS n, cited_links.location
    FROM cited_links
    LEFT JOIN post as response ON response.id = cited_links.post AND response.post_type_id <> 1
    LEFT JOIN post as question ON question.id = response.parent_id
    WHERE question.question_type <> 4
    AND cited_links.location <> ''
    GROUP BY cited_links.location
    ORDER BY n DESC
    """,
    "Domínios mais Frequentes em Respostas",
    ('Ocorrências', 'Domínio')
)

table.plot(
    """
    SELECT count(*) AS n,
           cited_links.location
    FROM cited_links
    LEFT JOIN post ON post.id = cited_links.post
    WHERE post.question_type <> 4
    AND post.post_type_id = 1
    AND cited_links.location <> ''
    GROUP BY cited_links.location
    ORDER BY n DESC
    """,
    "Domínios mais Frequentes em Perguntas",
    ('Ocorrências', 'Domínio')
)

table.plot_transpose(
    """
    SELECT median(response.creation_date - question.creation_date) AS median,
           avg(response.creation_date - question.creation_date) AS average,
           max(response.creation_date - question.creation_date) AS maximum
    FROM post AS question
    LEFT JOIN post AS response ON response.id = question.accepted_answer_id
    WHERE question.post_type_id = 1
      AND question.question_type <> 4
      AND question.accepted_answer_id IS NOT NULL
    """,
    "Dados Agregados Sobre o Tempo até a Resposta Aceita",
    ('Função Agregada', 'Valor')
)

table.plot_transpose(
    """
    SELECT median(response.creation_date - question.creation_date) AS median,
           avg(response.creation_date - question.creation_date) AS average,
           max(response.creation_date - question.creation_date) AS maximum
    FROM post AS question
    LEFT JOIN post AS response ON response.parent_id = question.id
    AND response.creation_date <= ALL
      (SELECT creation_date
       FROM post AS other_response
       WHERE other_response.parent_id = question.id)
    WHERE question.post_type_id = 1
      AND question.question_type <> 4
      AND question.accepted_answer_id IS NOT NULL
    """,
    "Dados Agregados Sobre o Tempo até uma Resposta",
    ('Função Agregada', 'Valor')
)

graph.plot(
    """
    SELECT to_char(date_trunc('year', post.creation_date), 'YYYY') AS created,
           count(*) AS sum_bandwidth
    FROM post
    WHERE post.post_type_id = 1
      AND post.question_type <> 4
      AND post.creation_date < '2017-01-01'
    GROUP BY 1
    ORDER BY 1
    """,
    "Número de perguntas por ano - dbunit"
)

pie.plot("""
SELECT
  ( SELECT CASE
               WHEN topics[1] > 0.5 THEN 'Exceções e problemas\ncom o Maven\n(TEMA 1)'
               WHEN topics[2] > 0.5 THEN 'Integração com\noutras ferramentas\n(TEMA 2)'
               WHEN topics[3] > 0.5 THEN 'Dúvidas gerais\nde dbunit\n(TEMA 3)'
               ELSE 'Não se encaixa\nem nenhum tema'
           END) AS tema,
       count(*) AS n
FROM post
WHERE question_type <> 4
GROUP BY tema
ORDER BY tema
""",
    "Perguntas por tema mais presente",
)

pie.plot("""
SELECT question_type.description, count(*) FROM post
LEFT JOIN question_type ON question_type.id = post.question_type
WHERE post_type_id = 1
AND question_type.id <> 4
AND topics[1] > 0.5
GROUP BY question_type.description, question_type.id
ORDER BY question_type.id
""",
    "Tipo de perguntas do tema 1",
)

pie.plot("""
SELECT question_type.description, count(*) FROM post
LEFT JOIN question_type ON question_type.id = post.question_type
WHERE post_type_id = 1
AND question_type.id <> 4
AND topics[2] > 0.5
GROUP BY question_type.description, question_type.id
ORDER BY question_type.id
""",
    "Tipo de perguntas do tema 2 (Integração com outras ferramentas)",
)

pie.plot("""
SELECT question_type.description, count(*) FROM post
LEFT JOIN question_type ON question_type.id = post.question_type
WHERE post_type_id = 1
AND question_type.id <> 4
AND topics[3] > 0.5
GROUP BY question_type.description, question_type.id
ORDER BY question_type.id
""",
    "Tipo de perguntas do tema 3",
)

graph.plot("""
  SELECT question_type.description,
         avg(topics[1]),
         avg(topics[2]),
         avg(topics[3])
  FROM post
  LEFT JOIN question_type ON question_type.id = post.question_type
  WHERE question_type <> 4
  GROUP BY question_type.description, question_type.id
  ORDER BY question_type.id
  """,
  "Probabilidade de uma pergunta ser de um tema pelo seu tipo",
  legend=('Tema 1', 'Tema 2', 'Tema 3')
)

graph.plot("""
  SELECT question_type.description,
         avg(CASE WHEN NOT has_answer
             AND NOT has_accepted_answer THEN 1 ELSE 0 END),
         avg(CASE WHEN has_answer
             AND NOT has_accepted_answer THEN 1 ELSE 0 END),
         avg(CASE WHEN has_accepted_answer THEN 1 ELSE 0 END)
  FROM post
  JOIN answer_presence ON answer_presence.id = post.id
  JOIN question_type ON question_type.id = post.question_type
  WHERE post.question_type <> 4
  GROUP BY question_type.description
  """,
  "Proporções de presença de resposta por tipo de pergunta",
  legend=('Sem resposta', 'Sem resposta aceita', 'Com resposta aceita')
)

graph.plot("""
SELECT CASE
           WHEN topics[1] > 0.5 THEN 'TEMA 1'
           WHEN topics[2] > 0.5 THEN 'TEMA 2'
           WHEN topics[3] > 0.5 THEN 'TEMA 3'
           ELSE 'Outros'
       END AS tema,
       avg(CASE WHEN NOT has_answer
           AND NOT has_accepted_answer THEN 1 ELSE 0 END),
       avg(CASE WHEN has_answer
           AND NOT has_accepted_answer THEN 1 ELSE 0 END),
       avg(CASE WHEN has_accepted_answer THEN 1 ELSE 0 END)
FROM post
JOIN answer_presence ON answer_presence.id = post.id
JOIN question_type ON question_type.id = post.question_type
WHERE post.question_type <> 4
GROUP BY tema
ORDER BY tema
""",
  "Proporções de presença de resposta por tema",
  legend=('Sem resposta', 'Sem resposta aceita', 'Com resposta aceita')
)

graph.plot(
    """
    SELECT question_type.description,
       avg(view_count)
    FROM post
    INNER JOIN question_type ON question_type.id = post.question_type
    WHERE post.question_type <> 4
    GROUP BY question_type.description,
             question_type.id
    ORDER BY question_type.id
    """,
    "Número médio de visualizações por tipo de pergunta"
)

graph.plot(
    """
    SELECT CASE
               WHEN topics[1] > 0.5 THEN 'TEMA 1'
               WHEN topics[2] > 0.5 THEN 'TEMA 2'
               WHEN topics[3] > 0.5 THEN 'TEMA 3'
               ELSE 'Outros'
           END AS tema,
           avg(view_count)
    FROM post
    WHERE post.question_type <> 4
    GROUP BY tema
    ORDER BY tema
    """,
    "Número médio de visualizações por tema"
)

graph.plot(
    """
    SELECT to_char(date_trunc('year', post.creation_date), 'YYYY') AS created,
           count(*) AS sum_bandwidth
    FROM post
    WHERE post.post_type_id = 1
      AND post.question_type = 1
    GROUP BY 1
    ORDER BY 1
    """,
    "Teste 1"
)

graph.plot(
    """
    SELECT to_char(date_trunc('year', post.creation_date), 'YYYY') AS created,
           count(*) AS sum_bandwidth
    FROM post
    WHERE post.post_type_id = 1
      AND post.question_type = 2
    GROUP BY 1
    ORDER BY 1
    """,
    "Teste 2"
)

graph.plot(
    """
    SELECT to_char(date_trunc('year', post.creation_date), 'YYYY') AS created,
           count(*) AS sum_bandwidth
    FROM post
    WHERE post.post_type_id = 1
      AND post.question_type = 3
    GROUP BY 1
    ORDER BY 1
    """,
    "Teste 3"
)

pie.plot(
    """
    SELECT description,
           value
    FROM outside_data
    WHERE origin = 'Delfim et Al - Redocumenting API'
      AND table_description = 'Distribution of all questions in the classes - Android'
    """,
    "Perguntas por Tipo - Android",
)

pie.plot(
    """
    SELECT description,
           value
    FROM outside_data
    WHERE origin = 'Delfim et Al - Redocumenting API'
      AND table_description = 'Distribution of all questions in the classes - Swing'
        """,
    "Perguntas por Tipo - Swing",
)

pie.plot(
    """
    SELECT description,
           value
    FROM outside_data
    WHERE origin = 'StackOverflow'
      AND table_description = 'Perguntas divididas por presença de resposta'
      ORDER BY description
        """,
    "Perguntas por Presença de Resposta e Resposta Aceita - Geral",
)

graph.plot(
    """
    SELECT description,
           value
    FROM outside_data
    WHERE origin = 'StackOverflow'
      AND table_description = 'Média de respostas por pergunta'
      ORDER BY description
    """,
    "Média de respostas por pergunta"
)

graph.plot(
    """
    SELECT description,
           value
    FROM outside_data
    WHERE origin = 'StackOverflow'
      AND table_description = 'Total de perguntas por ano'
      ORDER BY description
    """,
    "Total de perguntas por ano - geral"
)
