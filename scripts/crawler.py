from parser import Parser

file = open('../raw/Posts.xml')
parser = Parser(file)
i = 1
while True:
    print (i, ' posts salvos')
    i += 1
    post = parser.get_next_post(tag='dbunit')
    if post is None:
        break;
    post.save()