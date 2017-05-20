from parser import Parser

file = open('../raw/Posts.xml')
parser = Parser(file)
i = 1
while True:
    post = parser.get_next_post(text='dbunit')
    if post is None:
        break;
    if post.save_if_question():
        print (i, ' posts salvos')
        i += 1
