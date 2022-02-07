import os
from utils import sockets
import socket


def clear():
    os.system("cls")


def main():
    socket_server = sockets.socket_connection(
        socket.gethostname(),
        80)
    socket_server.send("test")


main()
