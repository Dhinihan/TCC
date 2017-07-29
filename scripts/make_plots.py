from tcc_plots import pie
from tcc_plots import table
from tcc_plots import graph

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
""",
    "Perguntas por Presença de Resposta e Resposta Aceita",
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
    "Perguntas dividas pela presença de código"
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
    "Respostas dividas pela presença de código"
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
    SELECT date_trunc('year', post.creation_date) AS created,
           count(*) AS sum_bandwidth
    FROM post
    WHERE post.post_type_id = 1
      AND post.question_type <> 4
    GROUP BY 1
    ORDER BY 1
    """,
    "Número de perguntas por ano"
)