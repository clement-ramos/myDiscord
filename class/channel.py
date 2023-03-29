from datetime import datetime
import settings


class Channel:
    def __init__(self, channel_id, name, type, created_at=None):
        self.channel_id = channel_id
        self.name = name
        self.type = type
        self.messages = []
        self.created_at = created_at

    def add_message(self, message):
        # add message to channel
        sql = "INSERT INTO messages (user_id, channel_id, content, created_at, modified_at) VALUES (%s, %s, %s, %s, %s)"
        val = (message.user_id, self.channel_id, message.content, message.created_at, message.modified_at)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) inserted", datetime.now())
        self.messages.append(message)

    def change_name(self, new_name):
        # update channel name using channel_id
        sql = "UPDATE channels SET name = %s WHERE id = %s"
        val = (new_name, self.channel_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        self.name = new_name

    def delete(self):
        # delete channel using channel_id
        sql = "DELETE FROM channels WHERE id = %s"
        val = (self.channel_id,)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())