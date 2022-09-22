#!/usr/bin/env python3
import socket
import threading
import pickle
import struct
import sys
import re

HEADER = 1024
FORMAT = "utf-8"
backlog = 5
# PORT = 8090
# IP_HOST = "192.168.1.93"

PORT = 5050
IP_HOST = socket.gethostbyname(socket.gethostname())
DISCONNECT_MESSAGE = 'disconnect'
print(IP_HOST)



# Create a TCP socket
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("[ERROR] creating socket: %s" %e)
    sys.exit(1)

# Enable reuse address/port
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to the port
server_address = (IP_HOST, PORT)

server.bind(server_address)


def handle_client(conn, addr):
    #{addr[0], addr[1]}
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:

        msg = conn.recv(HEADER).decode(FORMAT)

        if msg:
            init_result = re.search(r'^[#+]', msg)
            commit_result = re.search(r'^\d+', msg)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif init_result:
                conn.send("LOAD".encode(FORMAT))
            elif commit_result:
                conn.send("ON".encode(FORMAT))
            else:
                print(f"[{addr}] {msg}")


    conn.close()
    print("Server Closed")



def start():
    # Listen to clients, backlog argument specifies the max no. of queued connections
    server.listen(backlog)
    print(f"[LISTENING] server is listening on {IP_HOST}")
    while True:
        print("[WAITING] to receive message from client...")

        try:
            conn, addr = server.accept()
            # print('Connected by %s:%s' % (addr[0], addr[1]))
        except KeyboardInterrupt:
            break
        except socket.error as msg:
            print('%s' % (msg,))


        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")




print("[STARTING] server is starting...")
start()




# my_object = pickle.loads(msg_length)
# msg_length = len(msg_length)
# msg = conn.recv(HEADER).decode(FORMAT)