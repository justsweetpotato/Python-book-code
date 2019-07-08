#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from time import sleep


def func1():
    messages = [
        ' 我是小米 ',
        ' 我是小米的哥哥大米 ',
        ' 我是雷布斯'
    ]

    while True:
        for msg in messages:
            sys.stdout.flush()
            # sys.stdout.write(f'\r{msg}')
            sys.stdout.write('\r{}'.format(msg))
            sleep(1)


def func2():
    messages = [
        "\r\033[K我是小米",
        "\r\033[K我是小米的哥哥大米",
        "\r\033[K我是雷布斯"
    ]

    while True:
        for msg in messages:
            print(msg, end='\r')
            sleep(1)

# func1()
# func2()
