import connection
from post import Post
from tcc_themes import vocabulary
from tcc_themes import theme
from tcc_themes import stemmer

connection.run_sql('select stemmed_body, id, title from post where question_type <> 4')
posts = connection.results()
documents = []

for post in posts:
    text = post[0]
    stemmed_title = stemmer.process_text(post[2])
    text = text + ' ' + stemmed_title + ' ' + stemmed_title
    documents.append(text)

words = vocabulary.build(documents, N = 2500)
documents_themes, topics = theme.assign(documents, words, topics = 3)

connection.run_sql('delete from topic')
for i, topic in enumerate(topics):
    sql = "INSERT INTO topic VALUES (%s, %s)"
    values = [i + 1, topic]
    connection.run_sql(sql, values)

for i, topics in enumerate(documents_themes):
    str_topics = map(str, topics)
    connection.run_sql("update post set topics = '{%s}' where id = %d" % (', '.join(str_topics), posts[i][1]));

