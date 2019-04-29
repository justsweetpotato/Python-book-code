#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def fib(n):
    start_time = time.time()
    if n < 2:
        return

    a, b = 0, 1

    for num in range(2, n):
        a, b = b, a + b

    return fib


def profile_me(f, n):
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))

    return result


if __name__ == '__main__':
    n = 77
    print("Fibonacci number for n = {}: {}".format(n, profile_me(fib, n)))
