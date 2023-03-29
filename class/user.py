from datetime import datetime
import settings


class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.friends = []

    def send_message(self, message):
        # insert message into messages table using user_id
        sql = "INSERT INTO messages (user_id, channel_id, content, created_at, modified_at) VALUES (%s, %s, %s, %s, %s)"
        val = (self.user_id, message.channel_id, message.content, message.created_at, message.edited_at)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) inserted", datetime.now())

    def add_friend(self, friend):
        pass
        # add friend to user's friend list

    def remove_friend(self, friend):
        pass
        # remove friend from user's friend list

    def create_server(self, server):
        # create server using user_id
        sql = "INSERT INTO servers (owner_id, name, created_at) VALUES (%s, %s, %s)"
        val = (self.user_id, server.name, server.created_at)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) inserted", datetime.now())
