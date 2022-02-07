import socket
'''
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))
'''


class socket_connection():
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.connection = socket.socket(socket.AF_INET,
                                        socket.SOCK_STREAM)

    def connect(self):
        self.connection.connect((self.address,
                                 self.port))

    def send(self, message):
        self.connection.bind((socket.gethostname(), self.port))
        self.connection.listen(5)
        (client_socket, address) = self.connection.accept()
        client_socket.send(bytes(str(len(message)), encoding="ASCII"))
        client_socket.send(bytes(message, encoding="ASCII"))
        client_socket.close()

    def receive(self):
        self.connection.connect((self.address, self.port))
        length_of_message = int.from_bytes(
            self.connection.recv(4269), byteorder="big")
        message = self.connection.recv(length_of_message)
        print(message)
        self.connection.close()
