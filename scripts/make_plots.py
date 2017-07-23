import pie_chart

pie_chart.plot(
    'question_type',
    "Perguntas por Tipo",
    """
        WHERE post_type_id = 1
    """
)

pie_chart.plot('question_type',
    "Perguntas por Tipo Desconsiderando Não Relevantes",
    """
        WHERE post_type_id = 1
        AND question_type.id <> 4
    """
)
