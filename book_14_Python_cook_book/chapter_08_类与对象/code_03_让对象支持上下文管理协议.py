#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()

if __name__ == '__main__':
    from functools import partial

    conn = LazyConnection(('www.python.org', 80))

    with conn as s1:
        pass

        with conn as s2:
            s1.send(b'GET /index.html HTTP/1.0\r\n')
            s1.send(b'Host: www.python.org\r\n')
            s1.send(b'\r\n')
            resp = b''.join(iter(partial(s1.recv, 8192), b''))
            print(resp.decode())
