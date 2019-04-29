#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def fib(n):
    if n < 2:
        return 1

    return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    start_time = time.time()
    fib_seq = [fib(x) for x in range(1, 35)]
    end_time = time.time()

    print(
        "Calculating the list of {} Fibonacci numbers took {} seconds".format(
            len(fib_seq),
            end_time - start_time
        )
    )


# 可对比运行时间, 使用缓存优化结果非常明显

def fib_cached1(n, cache):
    if n < 2:
        return 1

    if n in cache:
        return cache[n]

    cache[n] = fib_cached1(n - 2, cache) + fib_cached1(n - 1, cache)
    return cache[n]


if __name__ == '__main__':
    cache = {}
    start_time = time.time()
    fib_seq = [fib_cached1(x, cache) for x in range(1, 350)]
    end_time = time.time()

    print(
        "Calculating the list of {} Fibonacci numbers took {} seconds".format(
            len(fib_seq),
            end_time - start_time
        )
    )
