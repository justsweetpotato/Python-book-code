#!/usr/bin/env python

from socket import *
from time import ctime

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(("", 7891))

while True:
    print("等待消息...")
    data, addr = udpSerSock.recvfrom(1024)
    print("...连接来自:", addr)
    print(data.decode("utf-8"))
    udpSerSock.sendto((ctime() + ": 已接收").encode(), addr)
    print("已向", addr, "回复")

udpSerSock.close()
