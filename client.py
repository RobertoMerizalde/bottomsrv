#!/usr/bin/env python3

import socket
import re

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.151"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):

    message = msg.encode(FORMAT)
    client.sendall(message)

    if msg == 'disconnect':
        client.close()
        print("Client Closed")

    # recv_msg = client.recv(1048).decode(FORMAT)
    #
    # if recv_msg:
    #     print(recv_msg)
    # else:
    #     return





active = True

while active:
    send_to_server = input("What would you like to send to the server?: ")

    if send_to_server == "disconnect":
        active = False

    length_msg = str(len(send_to_server))
    # whole_msg = f"{length_msg},{send_to_server}"

    send(send_to_server)



