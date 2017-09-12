from bow import DocumentClass
import operator


def build(documents, N = 1000):
    dclass = DocumentClass()
    for document in documents:
        dclass(document)
    vocabulary = []
    sorted_x = sorted(dclass.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(N):
        if(len(sorted_x[i][0]) > 1):
            vocabulary.append(sorted_x[i][0])

    return vocabulary