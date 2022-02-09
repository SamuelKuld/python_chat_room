import os

from matplotlib.pyplot import connect
from utils.sockets import socket_connection
from utils import sockets
import socket


def clear():
    os.system("cls")


def main():
    socket_server = socket_connection()
    socket_server.server_setup()
    while True:
        connection, addr = socket_server.server_connect()
        print("sending")
        connection.send(bytes("test", encoding="ASCII"))
        item = connection.recv(2048)
        print(item)
        connection.send(item)
        connection.close()


main()
