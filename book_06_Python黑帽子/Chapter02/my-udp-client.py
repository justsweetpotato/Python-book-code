# -*- coding: utf-8 -*-
import socket

target_host = "www.baidu.com"
target_port = 80

# 建立一个 socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送一些数据
client.sendto("Hello World!", (target_host, target_port))

# 接收一些数据
data, addr = client.recvfrom(4096)

print "来自{}: {}".format(addr[0], data)

