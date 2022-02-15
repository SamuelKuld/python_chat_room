import socket


class socket_connection():
    def __init__(self, address=socket.gethostname(), port=80):
        self.address = address
        self.port = port
        self.socket_internal_connection = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket_internal_connection.connect((self.address, self.port))

    def send(self, message):
        self.socket_internal_connection.send(message)

    def receive(self, address=socket.gethostname(), port=80):
        info = self.socket_internal_connection.recv(2048)
        return info

    def server_setup(self):
        self.socket_internal_connection.bind((self.address, self.port))
        self.socket_internal_connection.listen()

    def server_send(self, message, connection):
        connection.send(bytes(message, encoding="ASCII"))
        return message

    def server_connect(self):
        return self.socket_internal_connection.accept()

    def close(self):
        self.socket_internal_connection.close()
