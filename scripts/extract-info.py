import connection
from html.parser import HTMLParser
from urllib.parse import urlparse

connection.run_sql('select body, id from post')
posts = connection.results()

class LinkFinder(HTMLParser):
    def set_post (self, post_id):
        self.post_id = post_id

    def handle_starttag(self, tag, attrs):
        if (tag == 'a'):
            for attr in attrs:
                if (attr[0] == 'href'):
                    self.insert_link(attr[1])

    def insert_link(self, link):
        connection.run_sql(
            'SELECT count(*) FROM cited_links WHERE post = %s AND link = %s',
            [self.post_id, link]
        )
        previous_results = connection.results()

        if previous_results[0][0] > 0:
            return

        location = urlparse(link).netloc

        print(location)

        connection.run_sql(
            'INSERT INTO cited_links (post, link, location) VALUES (%s, %s, %s)',
            [self.post_id, link, location]
        )

for post in posts:
    body = post[0]
    parser = LinkFinder()
    parser.set_post(post[1])
    parser.feed(body)

