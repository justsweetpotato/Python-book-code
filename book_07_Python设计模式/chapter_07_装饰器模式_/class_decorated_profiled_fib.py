#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


class ProfilingDecorator(object):
    def __init__(self, f):
        print("Profiling decorator initiated")
        self.f = f

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.f(*args)
        end_time = time.time()
        print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))
        return result


@ProfilingDecorator
def fib(n):
    print("Inside fib")
    if n < 2:
        return

    a, b = 0, 1
    for num in range(2, n):
        a, b = b, a + b

    return a


if __name__ == '__main__':
    n = 77
    print("Fib for n = {}: {}".format(n, fib(n)))
