import os
from utils.sockets import socket_connection
from utils import sockets
import socket


def clear():
    os.system("cls")


def main():
    socket_server = socket_connection()
    socket_server.server_connect("test")


main()
