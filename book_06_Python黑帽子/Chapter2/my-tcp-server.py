# -*- coding: utf-8 -*-
import socket
import threading

bind_ip = ''
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print("[*] Listening on {}:{}".format(bind_ip, bind_port))

# 这是客户处理线程
def handle_client(client_socket):
    # 打印客户端发送过来的内容
    request = client_socket.recv(1024)
    print("[*] Received: \r\n{}".format(request))

    # 返还一个数据包
    client_socket.send("ACK!")
    client_socket.close()


while True:
    client, addr = server.accept()
    print("[*] Accepted connection from: {}:{}".format(addr[0], addr[1]))

    # 挂起客户端线程， 处理传入数据
    client_handler = threading.Thread(target=handle_client, args=(client, ))
    client_handler.start()


