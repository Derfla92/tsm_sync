#! /usr/bin/env python3

from encodings import utf_8
from socket import *


addr = ("0.0.0.0",8080)

serversocket = socket(AF_INET,SOCK_STREAM)
#serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
server = serversocket.bind(addr)
serversocket.listen()
fd, address = serversocket.accept()
print(address)
while True:



    recv = fd.recv(512)

    print(recv.decode("UTF-8"))
fd.close()
    