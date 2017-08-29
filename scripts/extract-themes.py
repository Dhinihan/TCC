import connection
import re
import html
import operator
from bow import DocumentClass
from sklearn.feature_extraction.text import CountVectorizer
import lda
import lda.datasets
import numpy as np

connection.run_sql('select stemmed_body, id from post where question_type <> 4')
posts = connection.results()
regex_tags = re.compile(r'(<!--.*?-->|<[^>]*>)')
documents = []
dclass = DocumentClass()

for post in posts:
    body = post[0]
    body = regex_tags.sub('', body)
    body = html.unescape(body)
    dclass(body)
    documents.append(body)

vocabulary = []
sorted_x = sorted(dclass.items(), key=operator.itemgetter(1), reverse=True)
for i in range(1500):
    vocabulary.append(sorted_x[i][0])

vectorizer = CountVectorizer(vocabulary = vocabulary)
X = vectorizer.fit_transform(documents)

print(X.shape)
print(X.sum())

model = lda.LDA(n_topics=5, n_iter=1500, random_state=1)
vocab = vocabulary
model.fit(X)
topic_word = model.components_
n_top_words = 20

for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))