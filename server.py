#!/usr/bin/env python3
import socket
import threading
import pickle
import struct

# https://www.youtube.com/watch?v=3QiPPX-KeSc&t=1384s

HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
# "192.168.1.151"
# IP_HOST = socket.gethostbyname(socket.gethostname())
IP_HOST = "192.168.1.93"
print(IP_HOST)
print(socket.gethostname())
print()
ADDR = (IP_HOST, PORT)



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # msg_length = conn.recv(2300).decode(FORMAT)
        msg = conn.recv(1024)
        if msg:
            my_object = pickle.loads(msg)
            if my_object == DISCONNECT_MESSAGE:
                connected = False

            print(f"{my_object}")


    conn.close()



def start():
    server.listen()
    print(f"[LISTENING] server is listening on {IP_HOST}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")



print("[STARTING] server is starting...")
start()
