#!/usr/bin/env python3
import socket
import threading

# https://www.youtube.com/watch?v=3QiPPX-KeSc&t=1384s

HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
# "192.168.1.151"
IP_HOST = socket.gethostbyname(socket.gethostname())
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
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] - {msg}")

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