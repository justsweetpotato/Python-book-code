#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps


def profiled(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)

    wrapper.ncalls = lambda: ncalls
    return wrapper


@profiled
def add(x, y):
    return x + y


print(add(1, 2))
print(add(3, 4))
print(add.ncalls())
