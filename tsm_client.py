#! /usr/bin/env python3

from http import client
from socket import *

addr = ("192.168.1.227",8080)
clientsocket = socket(AF_INET, SOCK_STREAM)
#client = clientsocket.bind(addr)

clientsocket.connect(addr)
while True:

    message = input().encode()
    clientsocket.send(message)

clientsocket.close()