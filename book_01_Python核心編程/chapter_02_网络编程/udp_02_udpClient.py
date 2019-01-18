#!/usr/bin/env python

from socket import *

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input("请输入消息: ")
    if not msg:
        break
    udpCliSock.sendto(msg.encode(), ("127.0.0.1", 7891))
    data, addr = udpCliSock.recvfrom(1024)
    if not data:
        break
    print("来自", addr, "的消息:", data.decode())

udpCliSock.close()
