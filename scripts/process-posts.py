import connection
from tcc_themes import stemmer

connection.run_sql('select body, id from post')
posts = connection.results()

for i, post in enumerate(posts):
    body = post[0]
    body = stemmer. process_text(body)
    connection.run_sql('update post set stemmed_body = %s where id = %s', (body, post[1]))
    if i % 100 == 0 and i > 0:
        print ("%d posts processados" % (i))

print ("%d posts processados" % (len(posts)))


