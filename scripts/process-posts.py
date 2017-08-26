import connection
import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
import html


cachedStopWords = stopwords.words("english")
regex_code = re.compile(r'<code>[^<]*<\/code>')
regex_tags = re.compile(r'(<!--.*?-->|<[^>]*>)')
regex_white_space = re.compile(r'\s+')
tokenizer = RegexpTokenizer(r'\w+')
stemmer = SnowballStemmer("english")

connection.run_sql('select body, id from post')
posts = connection.results()

i = 1
for post in posts:
    body = post[0]
    body = regex_code.sub('', body)
    body = regex_tags.sub('', body)
    body = html.unescape(body)
    body = regex_white_space.sub(" ", body)
    body = ' '.join(tokenizer.tokenize(body))
    body = ' '.join([word for word in body.split() if word.lower() not in cachedStopWords])
    body = ' '.join([stemmer.stem(word) for word in body.split()])
    connection.run_sql('update post set stemmed_body = %s where id = %s', (body, post[1]))
    print ('%s posts processados' % i)
    i += 1

