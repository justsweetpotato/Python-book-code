#!/usr/bin/env python
# -*- coding: utf-8 -*-

def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    IsPrime[0] = False  # 0 不是质数
    IsPrime[1] = False  # 1 不是质数

    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False

    return [x for x in range(2, n + 1) if IsPrime[x]]


if __name__ == '__main__':
    print(eratosthenes(10))
