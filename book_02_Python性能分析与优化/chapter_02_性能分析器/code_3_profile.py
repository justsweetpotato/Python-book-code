#!/usr/bin/env python

import profile


class Cached():  # 函数返回值缓存
    def __init__(self, fn):
        self.fn = fn
        self.cache = {}

    def __call__(self, *args, **kwargs):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = self.fn(*args)
            return self.cache[args]


@Cached  # 相差不大
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def fib_seq(n):
    seq = []
    for i in range(0, n + 1):
        seq.append(fib(i))
    return seq


profile.run('fib_seq(3000)')

