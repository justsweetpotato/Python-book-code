#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import socks
import requests
from bs4 import BeautifulSoup

addr = "127.0.0.1"
port = 1984

socks.set_default_proxy(socks.SOCKS5, addr, port)
socket.socket = socks.socksocket

# url = "https://www.google.com/"
url = "https://zh.wikipedia.org"
response = requests.get(url)
print(response.status_code)

data = response.content.decode()
soup = BeautifulSoup(data, features='html.parser')
print(soup.title)
