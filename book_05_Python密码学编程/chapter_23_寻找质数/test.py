#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pyperclip


def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    IsPrime[1] = False  # 1不为素数
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]


if __name__ == "__main__":
    start = time.time()
    prime = eratosthenes(1000)
    print(prime)
    pyperclip.copy(str(prime))
    print(time.time() - start)
