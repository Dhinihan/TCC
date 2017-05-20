import re
import html
from post import Post

class Parser:

    def __init__(self, file):
        self.file = file

    def get_next_post(self, tag=None, max_tries=10000000):
        post_text = ''

        for i in range(max_tries):
            # if i%100000 == 0:
            #     print (i/100000)
            post_text = self.read_row()
            if post_text is None:
                return None
            if tag is None:
                return Post(post_text)
            if self.post_matches_tag(post_text, tag):
                return Post(post_text)

        return None

    def post_matches_tag(self, post, tag):
        matches = re.search(tag, post, re.IGNORECASE)

        if matches is None:
            return False

        return True

    def read_row(self):
        end_candidate = False
        for line in self.file:
            return line

    def split_tags(self, tags_text):
        decoded_tags = html.unescape(tags_text)
        unbounded_tags = re.search('^<(.*)>$', decoded_tags).group(1)
        spltted_tags = unbounded_tags.split('><')
        return spltted_tags