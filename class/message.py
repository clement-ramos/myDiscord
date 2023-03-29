from datetime import datetime
import settings


class Message:
    def __init__(self, message_id, author, content, channel_id, created_at=None, edited_at=None):
        self.message_id = message_id
        self.channel_id = channel_id
        self.author = author
        self.content = content
        self.created_at = created_at
        self.edited_at = edited_at

    def edit(self, new_content):
        # update message content using message_id and channel_id
        sql = "UPDATE messages SET content = %s WHERE id = %s AND channel_id = %s"
        val = (new_content, self.message_id, self.channel_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        self.content = new_content

        # update edited_at using message_id and channel_id
        sql = "UPDATE messages SET modified_at = %s WHERE id = %s AND channel_id = %s"
        val = (datetime.now(), self.message_id, self.channel_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        self.edited_at = datetime.now()

    def delete(self):
        # delete message using message_id and channel_id
        sql = "DELETE FROM messages WHERE id = %s AND channel_id = %s"
        val = (self.message_id, self.channel_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())

