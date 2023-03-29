import mysql.connector as mysql
import socket


class MainServer:
    def __init__(self):
        pass

    def get_self_server_ip(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address