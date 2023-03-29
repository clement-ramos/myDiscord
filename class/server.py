from datetime import datetime
import settings


class Server:
    def __init__(self, server_id, name, owner, created_at=None):
        self.server_id = server_id
        self.name = name
        self.owner = owner
        self.created_at = created_at
        self.channels = []

    def add_channel(self, channel):
        # add channel to server using server_id (channel_id is auto-incremented)
        sql = "INSERT INTO channels (server_id, name, type, created_at) VALUES (%s, %s, %s, %s)"
        val = (self.server_id, channel.name, channel.type, channel.created_at)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) inserted", datetime.now())
        self.channels.append(channel)

    def remove_channel(self, channel):
        # remove channel from server using channel_id
        sql = "DELETE FROM channels WHERE id = %s"
        val = (channel.channel_id,)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        self.channels.remove(channel)