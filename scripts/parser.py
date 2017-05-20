import re
import html
from post import Post

class Parser:

    def __init__(self, file):
        self.file = file

    def get_next_post(self, text=None, questions=None):
        self.question_map = None
        post_text = ''

        while True:
            post_text = self.read_row()
            if post_text is None:
                return None
            if text is None and questions is None:
                return Post(post_text)
            if text is not None and self.post_match_text(post_text, text):
                return Post(post_text)
            if questions is not None and self.post_is_answer_to_question(post_text, questions):
                return Post(post_text)

        return None


    def post_match_text(self, post, text):
        matches = re.search(text, post, re.IGNORECASE)

        if matches is None:
            return False


        return True

    def post_is_answer_to_question(self, post, questions):
        matches = re.search('ParentId="(\d+)"', post, re.IGNORECASE)

        if matches is None:
            return False

        if self.question_map is None:
            self.build_question_map(questions)

        return self.question_map.get(int(matches.group(1)), False)

    def build_question_map(self, questions):
        self.question_map = {}
        for id in questions:
            self.question_map[id[0]] = True

    def read_row(self):
        end_candidate = False
        for line in self.file:
            return line

    def jfhv(self):
        results = connection.results()
        id_map = {}

        for row in results:
            id_map[row[0]] = True