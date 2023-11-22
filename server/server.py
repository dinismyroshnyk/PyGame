import socket
from _thread import *
import sys
import pickle
from player import Player

server = '192.168.1.79'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")

pos = [(0, 0), (100, 100)]

def threaded_client(conn, Player):
    conn.send(pickle.dumps(pos[Player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            pos[Player] = data
            

            if not data:
                print("Disconnected")
                break
            else:
                if Player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break
    
    print("Lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,currentPlayer))
    currentPlayer += 1
