#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from functools import wraps


class A:
    @classmethod
    def decorator1(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            r = func(*args, **kwargs)
            end = time.time()
            print('运行时间:', end - start)
            return r

        return wrapper

    @classmethod
    def decorator2(cls, func):
        ncalls = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal ncalls
            ncalls += 1
            return func(*args, **kwargs)

        wrapper.ncalls = lambda: ncalls
        return wrapper


@A.decorator1
@A.decorator2
def bar(n):
    while n > 0:
        n -= 1


bar(1000000)
bar(10000000)
bar(100000)
print("总调用次数:", bar.ncalls())
import sys
from pprint import pprint
pprint(sys.path)
