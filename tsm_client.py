#! /usr/bin/env python3

from socket import *

addr = ("127.0.0.1",8080)
clientsocket = socket(AF_INET, SOCK_STREAM)
client = clientsocket.bind(addr)

clientsocket.connect(addr)
clientsocket.send(b"hello")
