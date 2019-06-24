#!/usr/bin/env python
# -*- coding: utf-8 -*-

def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)


def add(x, y):
    return x + y


# --- 方法- ----
def print_result(result):
    print('Got:', result)


apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hell0 ', 'w0rld!'), callback=print_result)


# --- 方法二 ---

class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('Hello ', 'World!'), callback=r.handler)


# --- 方法三 ---

def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello ', 'world?'), callback=handler)


# --- 方法四 ---

def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


handler = make_handler()
next(handler)
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('HELLO ', 'WORLD.'), callback=handler.send)
