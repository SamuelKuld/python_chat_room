import socket
'''
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))
'''


class socket_connection():
    def __init__(self, address=socket.gethostname(), port=80):
        self.address = address
        self.port = port
        self.connection = socket.socket(socket.AF_INET,
                                        socket.SOCK_STREAM)

    def connect(self):
        self.connection.connect((self.address,
                                 self.port))

    def send(self, message):
        self.connect()
        self.connection = socket.socket(socket.AF_INET,
                                        socket.SOCK_STREAM)
        self.connection.bind((socket.gethostname(), self.port))
        self.connection.listen(5)
        (client_socket, address) = self.connection.accept()
        client_socket.send(bytes(("confirmation"), encoding="ASCII"))
        client_socket.send(bytes(str(len(message)), encoding="ASCII"))
        client_socket.send(bytes(message, encoding="ASCII"))
        client_socket.close()

    def receive(self):
        self.connect()
        confirmation = self.connection.recv(13)
        if confirmation == "confirmation":
            length_of_message = int.from_bytes(
                self.connection.recv(4269), byteorder="big")
            message = self.connection.recv(length_of_message)
            self.connection.close()
            return message.decode()
        else:
            return None
