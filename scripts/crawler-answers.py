from parser import Parser
import connection
from post import Post

ids = Post.get_question_ids();

file = open('../raw/Posts.xml')
parser = Parser(file)
i = 1
while True:
    post = parser.get_next_post(questions=ids)
    if post is None:
        break;
    post.save()
    print (i, ' posts salvos')
    i += 1
