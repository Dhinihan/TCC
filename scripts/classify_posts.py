import connection
import html
import re
from random import shuffle

OKGREEN = '\033[92m'
OKBLUE = '\033[94m'
BOLD = '\033[1m'
ENDC = '\033[0m'

regex_tags = re.compile(r'(<!--.*?-->|<[^>]*>)')
regex_dbunit = re.compile(r'(dbunit)', re.IGNORECASE)

connection.run_sql('select body, id, title from post where question_type is null and post_type_id = 1')
posts = connection.results()
connection.run_sql('select count(id) as conta from post where question_type is null and post_type_id = 1')
conta = connection.results()
conta = conta[0][0]

print(conta)

shuffle(posts)

for post in posts:
    body = post[0]
    title = post[2]
    body = regex_tags.sub('', body)
    body = html.unescape(body)
    body = regex_dbunit.sub(OKBLUE + BOLD + r'\1' + ENDC, body)
    conta -= 1
    print (OKGREEN + BOLD + title + ENDC + "\n")
    print (body)
    print ("\nFaltam classificar %s posts\n" % conta)
    print ("1: O quê")
    print ("2: Como")
    print ("3: Por quê")
    print ("4: Não referencia diretamente dbunit")
    print ("5: Parar")
    question_type = int(input("Classify: "))

    if question_type == 5:
        break

    connection.run_sql('update post set question_type = %s where id = %s', (question_type, post[1]))
    print("\n")

