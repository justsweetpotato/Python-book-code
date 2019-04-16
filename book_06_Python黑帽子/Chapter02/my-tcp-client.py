# -*- coding: utf-8 -*-
import socket

target_host = ""
target_port = 9999

# 建立一个 socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端
client.connect((target_host, target_port))

# 发送一些数据
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

# 接收一些数据
response = client.recv(4096)

print response

