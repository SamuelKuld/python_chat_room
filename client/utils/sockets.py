import socket


class socket_connection():
    def __init__(self, address=socket.gethostname(), port=80):
        self.address = address
        self.port = port
        self.socket_internal_connection = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.socket_internal_connection.connect((address, port))

    def send(self, message):
        self.socket_internal_connection.send(message)

    def server_send(self, message, connection):
        connection.send(message)

    def server_connect(self, message):
        self.socket_internal_connection.bind((self.address, self.port))
        self.socket_internal_connection.listen()
        connection, address = self.socket_internal_connection.accept()
        self.server_send(message, connection)

    def receive(self):
        return self.socket_internal_connection.recv(2048)

    def destroy(self):
        self.socket_internal_connection.close()
