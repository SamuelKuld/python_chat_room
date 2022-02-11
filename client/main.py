import os
import time
import socket
from utils.chat import *
from utils.threader import *
from utils.sockets import *


chat_buffer = []


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


def receive_always(arg_tuple):
    socket_thing, username = arg_tuple
    while True:
        message_received = socket_thing.receive().decode()
        clear()
        chat_buffer.append(message_received)
        for message in chat_buffer:
            print(message)
        print(chat_buffer)
        print("\n" + message_received,
              "\n" + username + " : ", end="")


def test_socket():
    socket_client = socket_connection()
    socket_client.connect()
    username = input(f"Username : ")
    socket_client.send(bytes(username, encoding="ASCII"))
    receiver = threader("receiver", receive_always, (socket_client, username))
    receiver.start()
    while True:
        information = input(f"{username} : ")
        chat_buffer.append(f"{username} : {information}")
        socket_client.send(bytes(information, encoding="ASCII"))


if __name__ == '__main__':
    test_socket()
