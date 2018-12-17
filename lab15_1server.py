#!/usr/bin/env python3

import socket
import random

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
names = ('Bohdan', 'Serhii', 'Mykola')
phrases = ('English, man, do you speak it?',
           'Nicht fershtein',
           'Wat?')

host = '127.0.0.1'
port = 9999

serversocket.bind((host, port))
serversocket.listen(5)

print('the server is waiting for connection')

clientsocket = None
while not clientsocket:
    clientsocket, addr = serversocket.accept()
    print('Got a connection from {}'.format(addr))

while True:
    clientsocket.send('Welcome! What is your name?'.encode('utf-8'))
    client_answer = clientsocket.recv(1024)
    print(client_answer.decode('utf-8'))
    if client_answer.decode('utf-8') in names:
        clientsocket.send('Nice to meet you '.encode('utf-8') + client_answer)
        clientsocket.send('\n'.encode('utf-8'))
    elif client_answer.decode('utf-8') == "What is your name?":
        clientsocket.send('My name is Bot\n'.encode('utf-8'))
    elif client_answer.decode('utf-8') == "Goodbye":
        clientsocket.send('Bye\n'.encode('utf-8'))
        break
    else:
        server_answer = random.choice(phrases)
        clientsocket.send(server_answer.encode('utf-8'))
        clientsocket.send('\n'.encode('utf-8'))
clientsocket.close()
