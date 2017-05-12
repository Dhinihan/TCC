import re
import html


class Parser:

    def __init__(self, file):
        self.file = file

    def get_next_post(self, tag=None, max_tries=100000):
        post_text = ''

        for i in range(max_tries):
            print (str(i) + ': ', end='')
            post_text = self.read_row()
            if post_text is None:
                return None
            if tag is None:
                return post_text
            if self.post_matches_tag(post_text, tag):
                return post_text
            print('')

        return None

    def post_matches_tag(self, post, tag):
        matches = re.search('Tags="((?:&lt;[^;]+&gt;)+)"', post)

        if matches is None:
            return False

        tags_text = matches.group(1)
        tags = self.split_tags(tags_text)
        print (tags)
        return tag in tags

    def read_row(self):
        end_candidate = False
        row = ''
        for i in range(0, 1000000):
            character = self.file.read(1)
            if not character:
                return row

            row += character

            if end_candidate and character == '>':
                return row

            if character == '/':
                end_candidate = True
            else:
                end_candidate = False

    def split_tags(self, tags_text):
        decoded_tags = html.unescape(tags_text)
        unbounded_tags = re.search('^<(.*)>$', decoded_tags).group(1)
        spltted_tags = unbounded_tags.split('><')
        return spltted_tags

file = open('../raw/Posts.xml')
parser = Parser(file)
print (parser.get_next_post(tag='dbunit'))
print (parser.get_next_post(tag='dbunit'))
