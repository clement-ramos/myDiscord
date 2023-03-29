from datetime import datetime
import settings


class Role:
    def __init__(self, name, color, permissions, server_id ,role_id=None):
        self.role_id = role_id
        self.name = name
        self.color = color
        self.permissions = permissions
        self.server_id = server_id
        self.created_at = datetime.now()

    def change_name(self, new_name):
        # update role name using role_id
        sql = "UPDATE userroles SET name = %s WHERE role_id = %s"
        val = (new_name, self.role_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        self.name = new_name

    def change_color(self, new_color):
        # update role color using role_id
        sql = "UPDATE userroles SET color = %s WHERE role_id = %s"
        val = (new_color, self.role_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        self.color = new_color

    def add_permissions(self, new_permissions):
        # update role permissions using role_id
        sql = "UPDATE userroles SET permissions = %s WHERE role_id = %s"
        val = (new_permissions, self.role_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        self.permissions = new_permissions

    def remove_permissions(self, old_permissions):
        # update role permissions using role_id
        sql = "UPDATE userroles SET permissions = %s WHERE role_id = %s"
        val = (old_permissions, self.role_id)
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) affected", datetime.now())
        self.permissions = old_permissions
