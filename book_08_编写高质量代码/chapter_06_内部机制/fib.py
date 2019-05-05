#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Fib(object):
    def __init__(self):
        self._a = 0
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._a, self._b = self._b, self._a + self._b
        return self._a


for i, f in enumerate(Fib()):
    print(f, end=" ")

    if i > 10:
        break

print("\n" + "#" * 50)


def fib2(n):
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a + b


for i, f in enumerate(fib2(10)):
    print(f, end=" ")
