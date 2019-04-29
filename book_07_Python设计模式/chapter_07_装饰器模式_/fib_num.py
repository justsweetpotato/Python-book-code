#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(x):
    fib_list = []
    a, b = 0, 1

    while a < x:
        fib_list.append(a)
        a, b = b, a + b

    return fib_list


def fib2(x):
    fib_list = []
    a, b = 0, 1
    for i in range(x):
        if a > x:
            break

        fib_list.append(a)
        a, b = b, a + b

    return fib_list


if __name__ == '__main__':
    print(fib(10))
    print(fib2(10))
