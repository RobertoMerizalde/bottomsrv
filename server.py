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
IP_HOST = socket.gethostbyname(socket.gethostname())
# IP_HOST = "192.168.1.93"
print(IP_HOST)
print(socket.gethostname())
print()
ADDR = (IP_HOST, PORT)



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


# def handle_client(conn, addr):
#     data = b''
#     payload_size = struct.calcsize("Q")
#     print(f"[NEW CONNECTION] {addr} connected.")
#     while True:
#         while len(data) < payload_size:
#             packet = conn.recv(4 * 1024)
#             if not packet: break
#             data += packet
#         packed_msg_size = data[:payload_size]
#         print("packed_msg_size:: ", packed_msg_size)
#         data = data[payload_size:]
#         print("data:: ", data)
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # msg_length = conn.recv(2300).decode(FORMAT)
        msg = conn.recv(1000)
        if msg:
            my_object = pickle.loads(msg)
            print(f"{my_object}")
            print()

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
