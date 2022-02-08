import os
from utils import sockets
import socket


def clear():
    os.system("cls")


def main():
    socket_server = sockets.socket_connection()
    while True:
        message = socket_server.receive()
        socket_server.send(message)


main()
