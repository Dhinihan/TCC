from sklearn.feature_extraction.text import CountVectorizer
import lda
import numpy as np


def assign(documents, vocabulary, topics = 5):
    vectorizer = CountVectorizer(vocabulary = vocabulary)
    X = vectorizer.fit_transform(documents)
    model = lda.LDA(n_topics=topics, random_state=1)
    model.fit(X)

    topic_word = model.components_
    n_top_words = 10
    topics = []

    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocabulary)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
        topics.append(' '.join(topic_words))

    return model.transform(X), topics