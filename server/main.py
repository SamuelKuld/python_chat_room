import os

from matplotlib.pyplot import connect
from utils.sockets import socket_connection
from utils import sockets
import socket
from utils.threader import threader


def clear():
    os.system("cls")


connections = []


def handle_connection(connection):
    print(connections)
    while True:
        item = connection.recv(2048)
        print(item)
        for i in connections:
            i.send(item)


def main():
    socket_server = socket_connection()
    socket_server.server_setup()
    amount = 0
    while True:
        print("Connection")
        amount += 1
        connection, addr = socket_server.server_connect()
        connections.append(connection)
        connection_handle = threader("connection" + str(amount),
                                     handle_connection, connection)
        connection_handle.start()


main()
