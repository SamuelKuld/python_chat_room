import socket
import os
import time
from matplotlib.pyplot import connect
from utils.sockets import socket_connection
from utils.threader import threader
from utils.client import client


def clear():
    os.system("cls")


connections = {}


def write_chat_to_file(chat):
    with open("chats.txt", "a+") as chats:
        chats.write(chat + "\n")


def handle_connection(arg_tuple):
    global last_chat
    while True:
        client_object, sent_username = arg_tuple
        try:
            item = client_object.connection_obj.recv(2048)
        except:
            break
        item_decoded = item.decode()
        if client_object.last_message == item_decoded:
            print(f"{client_object.ip} : ",
                  f"{client_object.name} :",
                  f"Client is attempting to spam : Message blocked")
            continue

        print(
            f"{sent_username.decode()} : '{item_decoded}'\n  [IP : {client_object.ip} at time {time.time()}] ")
        if time.time() - client_object.last_message_time <= 1:
            print(
                f"{client_object.ip} : ",
                f"{client_object.name} :",
                f"Client is attempting to spam : Message blocked")
            client_object.connection_obj.send(bytes(
                "Server : YoUrE seNdIngG ToO mAny MessAgEs", encoding="ASCII"))
            client_object.last_message_time = time.time()
            continue
        client_object.last_message = item_decoded
        try:
            for username, value in connections.items():
                if client_object.ip != value.ip:
                    try:
                        value.connection_obj.send(
                            bytes(f"{sent_username.decode()} : {item_decoded}", encoding="ASCII"))
                        write_chat_to_file(
                            f"{sent_username.decode()} : {item_decoded} : {time.time()}")
                        client_object.last_message_time = time.time()
                    except Exception as e:
                        del connections[username]
                        continue
        except:
            for username, value in connections.items():
                if client_object.ip != value.ip:
                    try:
                        value.connection_obj.send(
                            bytes(f"{sent_username.decode()} : {item_decoded}", encoding="ASCII"))
                        write_chat_to_file(
                            f"{sent_username.decode()} : {item_decoded} : {time.time()}")
                        client_object.last_message_time = time.time()
                    except Exception as e:
                        del connections[username]
                        continue


def main():
    socket_server = socket_connection()
    socket_server.server_setup()
    amount = 0
    while True:
        print("Connection")
        amount += 1
        connection, addr = socket_server.server_connect()
        username = connection.recv(4096)
        client_object = client(addr, username, connection)
        write_chat_to_file(username.decode() + " joined ")
        connections[username.decode()] = client_object
        connection_handle = threader("connection" + str(amount),
                                     handle_connection, (client_object, client_object.name))
        connection_handle.start()


main()
