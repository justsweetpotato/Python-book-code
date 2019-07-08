#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想在函数上添加一个包装器，增加额外的操作处理 (比如日志、计时等)。
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n: int) -> None:
    '''
    Count down
    '''
    while n > 0:
        n -= 1


countdown(100000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
print(countdown.__dict__)
countdown.__wrapped__(10)  # @wraps 有一个重要特征是它能让你通过属性 __wrapped__ 直接访问被包装函数。
from inspect import signature

print(signature(countdown))  # __wrapped__ 属性还能让被装饰函数正确暴露底层的参数签名信息。
