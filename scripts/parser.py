import re
import html


class Parser:

    def __init__(self, file):
        self.file = file

    def get_next_post(self, tag=None, max_tries=1000000):
        post_text = ''

        for i in range(max_tries):
            post_text = self.read_row()
            if post_text is None:
                return None
            if tag is None:
                return post_text
            if self.post_matches_tag_alt(post_text, tag):
                return post_text

        return None

    def post_matches_tag_alt(self, post, tag):
        matches = re.search('Tags="[^"]*%s[^"]*"' % tag, post)

        if matches is None:
            return False

        return True

    def read_row(self):
        end_candidate = False
        for line in file:
            return line

    def split_tags(self, tags_text):
        decoded_tags = html.unescape(tags_text)
        unbounded_tags = re.search('^<(.*)>$', decoded_tags).group(1)
        spltted_tags = unbounded_tags.split('><')
        return spltted_tags

file = open('../raw/Posts.xml')
parser = Parser(file)
post = parser.get_next_post(tag='dbunit')
print(post)
