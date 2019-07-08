#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想在类中定义装饰器，并将其作用在其他函数或方法上。

from functools import wraps


class A:
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)

        return wrapper


a = A()


@a.decorator1
def spam():
    pass


@A.decorator2
def grok():
    pass

# 仔细观察可以发现一个是实例调用，一个是类调用。
