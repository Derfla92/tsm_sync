#! /usr/bin/env python3

from socket import *


addr = ("",8081)

serversocket = socket(AF_INET,SOCK_STREAM)
#serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
server = serversocket.bind(addr)
while True:
    serversocket.listen()

    fd, address = serversocket.accept()

    print(fd)
    print(address)