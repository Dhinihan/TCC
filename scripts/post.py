from xml.etree import ElementTree
import connection
import html
import re


class Post:

    @staticmethod
    def get_question_ids():
        sql = """
            select id from post where post_type_id = 1;
        """
        connection.run_sql(sql)
        return connection.results()

    @staticmethod
    def print(body, title, id = -1):
        OKGREEN = '\033[92m'
        OKBLUE = '\033[94m'
        BOLD = '\033[1m'
        ENDC = '\033[0m'

        regex_tags = re.compile(r'(<!--.*?-->|<[^>]*>)')
        regex_dbunit = re.compile(r'(dbunit)', re.IGNORECASE)

        body = regex_tags.sub('', body)
        body = html.unescape(body)
        body = regex_dbunit.sub(OKBLUE + BOLD + r'\1' + ENDC, body)
        print (OKGREEN + BOLD + title + ENDC + "\n")
        if (id != -1):
            print ("ID: %d\n" % id)
        print (body)

    def __init__(self, text):
        self.data = ElementTree.fromstring(text).attrib

    def save_if_question(self):
        if self.data['PostTypeId'] == '1':
            self.save()
            return True
        return False

    def save(self):
        sql = """
            insert into post (
                id,
                title,
                body,
                tags,
                parent_id,
                answer_count,
                accepted_answer_id,
                creation_date,
                last_activity_date,
                score,
                last_edit_date,
                last_editor_user_id,
                last_editor_display_name,
                post_type_id,
                comment_count,
                view_count,
                favorite_count,
                owner_user_id,
                owner_display_name,
                closed_date
            ) values (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
        """
        values = []
        values.append(self.data.get('Id', None))
        values.append(self.data.get('Title', None))
        values.append(self.data.get('Body', None))
        values.append(self.data.get('Tags', None))
        values.append(self.data.get('ParentId', None))
        values.append(self.data.get('AnswerCount', None))
        values.append(self.data.get('AcceptedAnswerId', None))
        values.append(self.data.get('CreationDate', None))
        values.append(self.data.get('LastActivityDate', None))
        values.append(self.data.get('Score', None))
        values.append(self.data.get('LastEditDate', None))
        values.append(self.data.get('LastEditorUserId', None))
        values.append(self.data.get('LastEditorDisplayName', None))
        values.append(self.data.get('PostTypeId', None))
        values.append(self.data.get('CommentCount', None))
        values.append(self.data.get('ViewCount', None))
        values.append(self.data.get('FavoriteCount', None))
        values.append(self.data.get('OwnerUserId', None))
        values.append(self.data.get('OwnerDisplayName', None))
        values.append(self.data.get('ClosedDate', None))
        connection.run_sql(sql, values)
