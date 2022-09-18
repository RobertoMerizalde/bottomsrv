#!/usr/bin/env python3
import socket
import pickle

my_dict = {
    "lon": -4323.243,
    "lat": 532.533,
    "name": "gps-coord.",
    "city": "Austin"
}





HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
IP_HOST = "192.168.1.151"
ADDR = (IP_HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    # message = msg.encode(FORMAT)
    message = msg
    # msg_length = len(message)
    # send_length = str(msg_length).encode(FORMAT)
    # send_length += b' ' * (HEADER - len(send_length))
    # client.send(send_length)
    client.send(message)


my_object = pickle.dumps(my_dict)


send(my_object)
# input()
# send("Hello fdf")
# input()
# send("Hello brothjtda")
input()
send(DISCONNECT_MESSAGE)