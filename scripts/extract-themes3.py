import connection
import re
import html
import operator
from bow import DocumentClass
from sklearn.feature_extraction.text import CountVectorizer
import lda
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
from post import Post

connection.run_sql('select stemmed_body, id, title from post where question_type <> 4')
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
for i in range(2000):
    word = sorted_x[i][0]
    if(len(word) > 1):
        vocabulary.append(sorted_x[i][0])

shuffle(vocabulary)
vectorizer = CountVectorizer(vocabulary = vocabulary)
X = vectorizer.fit_transform(documents)
model = lda.LDA(n_topics=5, random_state=1, n_iter=100)
model.fit(X)
doc_topic_test = model.transform(X)
for i, topics in enumerate(doc_topic_test):
    Post.print(posts[i][0], posts[i][2])
    str_topics = map(str, topics)
    connection.run_sql("update post set topics = '{%s}' where id = %d" % (', '.join(str_topics), posts[i][1]));

# # topic_word = model.components_
# # n_top_words = 20

# # for i, topic_dist in enumerate(topic_word):
# #     topic_words = np.array(vocabulary)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
# #     print('Topic {}: {}'.format(i, ' '.join(topic_words)))
