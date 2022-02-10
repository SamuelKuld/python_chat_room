import os
import time
from matplotlib.pyplot import connect
from utils.sockets import socket_connection
from utils.threader import threader


def clear():
    os.system("cls")


connections = {}


def write_chat_to_file(chat):
    with open("chats.txt", "a+") as chats:
        chats.write(chat + "\n")


def handle_connection(arg_tuple):
    global last_chat
    while True:
        connection, sent_username = arg_tuple
        item = connection.recv(2048)
        item_decoded = item.decode()
        print(f"{sent_username.decode()} : {item_decoded}")

        for username, value in connections.items():
            if connection != value:
                value.send(
                    bytes(f"{sent_username.decode()} : {item_decoded}", encoding="ASCII"))
                write_chat_to_file(
                    f"{sent_username.decode()} : {item_decoded} : {time.time()}")


def main():
    socket_server = socket_connection()
    socket_server.server_setup()
    amount = 0
    while True:
        print("Connection")
        amount += 1
        connection, addr = socket_server.server_connect()
        username = connection.recv(4096)
        write_chat_to_file(username.decode() + " joined ")
        connections[username.decode()] = connection
        connection_handle = threader("connection" + str(amount),
                                     handle_connection, (connection, username))
        connection_handle.start()


main()
