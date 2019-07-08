#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想给类方法或静态方法提供装饰器

# 给类或静态方法提供装饰器是很简单的，不过要确保装饰器在 @classmethod 或 @staticmethod 之前。例如：

import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r

    return wrapper


class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


s = Spam()
s.instance_method(10000000)
Spam.class_method(10000000)
Spam.static_method(10000000)