from sqlite3 import connect
import sys
import socket
import socketserver
import time

newSock = socket.socket()
host = socket.gethostname
s_ip = socket.gethostbyname(host)
port = 1602

newSock.bind(host, port)

name = input('Enter you nickname: ')
newSock.listen(1)

conn, add= newSock.accept()
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send(name.encode())

while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)