import os
import time
import socket
from utils.chat import *
from utils.threader import *
from utils.sockets import *


def clear():
    os.system("cls")


def main():
    pass


def test_thread(overflow):
    print("You are internal!")


def internal_thread_test():
    test = threader("internal_thread", "internal_threaded", test_thread)
    return test


def test():
    primary_thread = threader("test_thread", test_function, 3)
    primary_thread.start()
    test_chat()


def test_socket():
    socket_client = socket_connection()
    socket_client.connect()
    print(socket_client.receive())
    socket_client.send(bytes(input(), encoding="ASCII"))
    print(socket_client.receive())


if __name__ == '__main__':
    test_socket()
