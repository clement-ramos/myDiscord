import settings
from server import Server
from channel import Channel
from message import Message
from user import User
from role import Role
from datetime import datetime


class BackMain:
    def __init__(self):
        self.current_user = None
        self.current_server = None
        self.current_channel = None
        self.currents_message = []
        self.servers = []
        self.channels = []
        self.messages = []
        self.users = []
        self.roles = []

    # Server methods (get, update, delete) #
    def create_server(self, name, roles, owner_id, created_at=None): # create server
        # create server
        sql = "INSERT INTO servers (owner_id, name, created_at) VALUES (%s, %s, %s)"
        val = (owner_id, name, created_at)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) inserted", datetime.now())
        self.servers.append(Server(settings.cursor.lastrowid, owner_id, name, created_at))
        for role in roles:
            self.create_role(role, settings.cursor.lastrowid)

    def delete_server(self, server_id):
        # delete server
        sql = "DELETE FROM servers WHERE id = %s"
        val = (server_id,)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) deleted", datetime.now())
        for server in self.servers:
            if server.server_id == server_id:
                self.servers.remove(server)

    def get_servers(self):
        # get all servers from servers table
        sql = "SELECT * FROM servers"
        settings.cursor.execute(sql)
        result = settings.cursor.fetchall()
        for row in result:
            self.servers.append(Server(row[0], row[1], row[2], row[3]))

    def change_server_name(self, server_id, name):
        # change server name
        sql = "UPDATE servers SET name = %s WHERE id = %s"
        val = (name, server_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        for server in self.servers:
            if server.server_id == server_id:
                server.name = name

    def return_server(self, server_id):
        # return server object
        for server in self.servers:
            if server.server_id == server_id:
                return server

    # Channel methods (get, update, delete) #

    def get_channels(self):
        # get all channels from servers using server_id from known servers
        for server in self.servers:
            sql = "SELECT * FROM channels WHERE server_id = %s"
            val = (server.server_id,)
            settings.cursor.execute(sql, val)
            result = settings.cursor.fetchall()
            for row in result:
                self.channels.append(Channel(row[0], row[1], row[2], row[3]))
                server.channels.append(Channel(row[0], row[1], row[2], row[3]))

    def create_channel(self, name, type, server_id, created_at=None):
        # create new channel
        sql = "INSERT INTO channels (name, type, server_id, created_at) VALUES (%s, %s, %s, %s)"
        val = (name, type, server_id, created_at)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) inserted", datetime.now())
        self.channels.append(Channel(settings.cursor.lastrowid, name, type, created_at))
        for server in self.servers:
            if server.server_id == server_id:
                server.channels.append(Channel(settings.cursor.lastrowid, name, type, created_at))

    def delete_channel(self, channel_id):
        # delete channel
        sql = "DELETE FROM channels WHERE id = %s"
        val = (channel_id,)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) deleted", datetime.now())
        for channel in self.channels:
            if channel.channel_id == channel_id:
                self.channels.remove(channel)

    def change_channel_name(self, channel_id, name):
        # change channel name
        sql = "UPDATE channels SET name = %s WHERE id = %s"
        val = (name, channel_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        for channel in self.channels:
            if channel.channel_id == channel_id:
                channel.name = name

    def return_channel(self, channel_id):
        # return channel object
        for channel in self.channels:
            if channel.channel_id == channel_id:
                return channel

    # Role methods (get, update, delete) #
    def get_roles(self):
        # get all roles from roles table
        sql = "SELECT * FROM userroles"
        settings.cursor.execute(sql)
        result = settings.cursor.fetchall()
        for row in result:
            self.roles.append(Role(row[0], row[1], row[2], row[3]))

    def create_role(self, name, color, server_id, role_id ,created_at=None):
        # create new role
        sql = "INSERT INTO userroles (name, color, server_id, role_id, created_at) VALUES (%s, %s, %s, %s, %s)"
        val = (name, color, server_id, role_id, created_at)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) inserted", datetime.now())
        self.roles.append(Role(settings.cursor.lastrowid, server_id, name, color))

    def delete_role(self, role_id):
        # delete role
        sql = "DELETE FROM userroles WHERE id = %s"
        val = (role_id,)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) deleted", datetime.now())
        for role in self.roles:
            if role.role_id == role_id:
                self.roles.remove(role)

    def change_role_name(self, role_id, name):
        # change role name
        sql = "UPDATE userroles SET name = %s WHERE id = %s"
        val = (name, role_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        for role in self.roles:
            if role.role_id == role_id:
                role.name = name

    def change_role_color(self, role_id, color):
        # change role color
        sql = "UPDATE userroles SET color = %s WHERE id = %s"
        val = (color, role_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        for role in self.roles:
            if role.role_id == role_id:
                role.color = color

    def return_role(self, role_id):
        # return role object
        for role in self.roles:
            if role.role_id == role_id:
                return role

    # User methods (get, update, delete) #

    def get_users(self):
        # get all users from users table
        sql = "SELECT * FROM users"
        settings.cursor.execute(sql)
        result = settings.cursor.fetchall()
        for row in result:
            self.users.append(User(row[0], row[3], row[4], row[5]))

    def create_user(self, first_name, last_name, username, email, password, created_at=None):
        # create new user
        sql = "INSERT INTO users (first_name, name,username ,email, password_hash, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (first_name, last_name, username, email, password, created_at)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) inserted", datetime.now())
        self.users.append(User(settings.cursor.lastrowid,username, password, email))

    def delete_user(self, user_id):
        # delete user
        sql = "DELETE FROM users WHERE id = %s"
        val = (user_id,)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) deleted", datetime.now())
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)

    def chance_username(self, user_id, username):
        # change username
        sql = "UPDATE users SET username = %s WHERE id = %s"
        val = (username, user_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        for user in self.users:
            if user.user_id == user_id:
                user.username = username

    def chance_password(self, user_id, password):
        # change password
        sql = "UPDATE users SET password_hash = %s WHERE id = %s"
        val = (password, user_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        for user in self.users:
            if user.user_id == user_id:
                user.password = password

    def chance_email(self, user_id, email):
        # change email
        sql = "UPDATE users SET email = %s WHERE id = %s"
        val = (email, user_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        for user in self.users:
            if user.user_id == user_id:
                user.email = email

    def return_user(self, user_id):
        # return user object
        for user in self.users:
            if user.user_id == user_id:
                return user

    # Message methods (get, update, delete) #
    def get_messages(self):
        # get all messages from messages table
        sql = "SELECT * FROM messages"
        settings.cursor.execute(sql)
        result = settings.cursor.fetchall()
        for row in result:
            self.messages.append(Message(row[0], row[1], row[2], row[3], row[4], row[5]))
            for channel in self.channels:
                if channel.channel_id == row[2]:
                    channel.messages.append(Message(row[0], row[1], row[2], row[3], row[4], row[5]))

    def create_message(self, content, user_id, channel_id, created_at=None, edited_at=None):
        # create new message
        sql = "INSERT INTO messages (content, user_id, channel_id, created_at, modified_at) VALUES (%s, %s, %s, %s, %s)"
        val = (content, user_id, channel_id, created_at, edited_at)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) inserted", datetime.now())
        self.messages.append(Message(settings.cursor.lastrowid, content, user_id, channel_id, created_at))
        for channel in self.channels:
            if channel.channel_id == channel_id:
                channel.messages.append(Message(settings.cursor.lastrowid, content, user_id, channel_id, created_at))

    def delete_message(self, message_id):
        # delete message
        sql = "DELETE FROM messages WHERE id = %s"
        val = (message_id,)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) deleted", datetime.now())
        for message in self.messages:
            if message.message_id == message_id:
                self.messages.remove(message)

    def change_message_content(self, message_id, content):
        # change message content and edited_at
        sql = "UPDATE messages SET content = %s, modified_at = %s WHERE id = %s"
        val = (content, datetime.now(), message_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        for message in self.messages:
            if message.message_id == message_id:
                message.content = content
                message.edited_at = datetime.now()

    def return_message(self, message_id):
        # return message object
        for message in self.messages:
            if message.message_id == message_id:
                return message

    # Application methods #
    def run(self):
        self.get_all()

    def get_all(self):
        self.get_servers()
        self.get_channels()
        self.get_messages()
        self.get_users()
        self.get_roles()