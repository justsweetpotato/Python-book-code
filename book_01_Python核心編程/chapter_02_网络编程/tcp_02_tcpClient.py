#!/usr/bin/env python

from socket import *


# tcpCliScok = socket(AF_INET, SOCK_STREAM)
# tcpCliScok.connect(("127.0.0.1", 7890))
# print("已连接...")
#
# while True:
#     msg = input("请输入消息: ")
#     if not msg:
#         break
#     tcpCliScok.send(msg.encode())
#     data = tcpCliScok.recv(1024)
#     if not data:
#         break
#     print(data.decode("utf-8"))
#
# tcpCliScok.close()


def tcpClient(host="104.128.94.100", port=7890):
    tcpCliScok = socket(AF_INET, SOCK_STREAM)
    print(host)
    print(port)
    tcpCliScok.connect((host, port))
    print("已连接服务器 ('{}', {})".format(host, port))

    while True:
        msg = input("> ")
        if not msg:
            print("断开与服务器的连接")
            break
        tcpCliScok.send(msg.encode())

        data = tcpCliScok.recv(1024)
        msg = "服务器回复: " + data.decode("utf-8")
        print(msg)

    tcpCliScok.close()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 7891

    if host and port:
        port = int(port)
        try:
            tcpClient(host, port)
        except Exception as e:
            print(e)
    else:
        print("连接默认服务器")
        try:
            tcpClient()
        except Exception as e:
            print(e)
