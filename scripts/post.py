from xml.etree import ElementTree
import connection

class Post:



    def __init__(self, text):
        self.data = ElementTree.fromstring(text).attrib

    def save(self):
        sql = """
            insert into post (
                id, title, body, tags, answer_count, accepted_answer_id, creation_date, last_activity_date, last_editor_user_id, score, last_edit_date, post_type_id, comment_count, view_count, owner_user_id, owner_display_name
            ) values (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
        """
        values = []
        values.append(self.data.get('Id', None))
        values.append(self.data.get('Title', None))
        values.append(self.data.get('Body', None))
        values.append(self.data.get('Tags', None))
        values.append(self.data.get('AnswerCount', None))
        values.append(self.data.get('AcceptedAnswerId', None))
        values.append(self.data.get('CreationDate', None))
        values.append(self.data.get('LastActivityDate', None))
        values.append(self.data.get('LastEditorUserId', None))
        values.append(self.data.get('Score', None))
        values.append(self.data.get('LastEditDate', None))
        values.append(self.data.get('PostTypeId', None))
        values.append(self.data.get('CommentCount', None))
        values.append(self.data.get('ViewCount', None))
        values.append(self.data.get('OwnerUserId', None))
        values.append(self.data.get('OwnerDisplayName', None))
        connection.run_sql(sql, values)
