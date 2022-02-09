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


def receive_always(socket_thing):
    while True:
        print(socket_thing.receive())


def test_socket():
    socket_client = socket_connection()
    socket_client.connect()

    receiver = threader("receiver", receive_always, socket_client)
    receiver.start()
    while True:
        socket_client.send(bytes(input(), encoding="ASCII"))


if __name__ == '__main__':
    test_socket()
