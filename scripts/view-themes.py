import connection
import argparse
from post import Post

parser = argparse.ArgumentParser(description='Show posts ordered by topics')
parser.add_argument('topic', type=int, help='the index of the topic to order')
parser.add_argument('-n', '--n-posts', dest='number_of_posts', type=int, default=10, help='the number of posts to show')
parser.add_argument('-a', '--ascending', dest='is_ascending', type=bool, default=False, help='iverts the order')

args = parser.parse_args()
if args.is_ascending :
    direction = 'ASC'
else:
    direction = 'DESC'

connection.run_sql("""
    SELECT id,
           stemmed_body,
           body,
           title,
           topics
    FROM post
    WHERE question_type <> 4
    AND topics[%d] > 0.5
    ORDER BY topics[%d] %s
    LIMIT %d
""" % (args.topic, args.topic, direction, args.number_of_posts))

posts = connection.results()

for post in posts:
    Post.print(post[2], post[3], post[0])


