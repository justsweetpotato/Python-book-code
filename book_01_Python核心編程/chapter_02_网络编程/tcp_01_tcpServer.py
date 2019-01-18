#!/usr/bin/env python

from socket import *
from time import ctime, sleep
import os

# tcp_socket = socket(AF_INET, SOCK_STREAM)
# tcp_socket.bind(("", 7890))
# tcp_socket.listen(5)
#
# while True:
#     print("等待一个客户端连接...")
#     tcp_cli, addr = tcp_socket.accept()
#     print("...连接来自:", addr)
#
#     while True:
#         data = tcp_cli.recv(1024)
#         s_data = data.decode("gbk")
#         print(s_data)
#         if not data:
#             break
#         msg = (ctime() + ": 已接收\n").encode()
#         tcp_cli.send(msg)
#     tcp_cli.close()
#
# tcp_socket.close()

# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(("", 7890))
# tcpSerSock.listen(5)
#
# while True:
#     print("等待连接...")
#     tcpCliSock, addr = tcpSerSock.accept()
#     print("...连接来自:", addr)
#
#     while True:
#         data = tcpCliSock.recv(1024)
#         print(data.decode())
#
#         if not data:
#             print(addr, "连接终止.")
#             break
#         tcpCliSock.send((ctime() + ": 已接收\n").encode())
#     tcpCliSock.close()
# tcpSerSock.close()


def socketSever(host="", port=7891):
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口复用
    tcpSerSock.bind((host, port))
    tcpSerSock.listen(5)

    while True:
        print("等待客户端连接...")
        tcpCliSock, addr = tcpSerSock.accept()
        print("连接来自:", addr)

        while True:
            data = tcpCliSock.recv(1024)
            if not data:
                print("客户端断开连接")
                break
            data = data.decode("utf-8")
            print("客户端的消息: " + data)
            if data == 'date':
                msg = ctime()
                tcpCliSock.send(msg.encode())
            elif data == 'ls':
                msg = str(os.listdir(os.getcwd()))
                tcpCliSock.send(msg.encode())
            elif data == 'pwd':
                msg = os.getcwd()
                tcpCliSock.send(msg.encode())
            else:
                msg = "please input [ date | ls | pwd ]"
                tcpCliSock.send(msg.encode())
        tcpCliSock.close()

    tcpSerSock.close()


if __name__ == '__main__':
    try:
        socketSever()
    except Exception as e:
        print(e)
