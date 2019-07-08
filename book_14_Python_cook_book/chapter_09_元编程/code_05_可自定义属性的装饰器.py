#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想写一个装饰器来包装一个函数，并且允许用户提供参数在运行时控制装饰器行为。
# 引入一个访问函数，使用 nonlocal 来修改内部变量。 然后这个访问函数被作为一个属性赋值给包装函数。

from functools import wraps, partial
import logging


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

