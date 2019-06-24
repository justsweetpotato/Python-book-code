#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup

with open('data.txt', 'r', encoding='utf-8') as f:
    data = f.read()


def func_re():
    title = re.findall(r'<title>(.*?)</title>', data)
    print(title)


def func_soup():
    soup = BeautifulSoup(data, 'html.parser')
    print(soup.title)


if __name__ == '__main__':
    import time
    s_time = time.time()
    func_re()
    print(time.time() - s_time)

    s_time = time.time()
    func_soup()
    print(time.time() - s_time)
