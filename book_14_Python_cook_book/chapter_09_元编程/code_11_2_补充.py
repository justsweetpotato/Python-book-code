#!/usr/bin/env python
# -*- coding: utf-8 -*-

def a(x, debug=False):
    if debug:
        print('Calling a')


def b(x, y, z, debug=False):
    if debug:
        print('Calling b')


def c(x, y, debug=False):
    if debug:
        print('Calling c')


from functools import wraps
import inspect


def optional_debug(func):
    if 'debug' in inspect.getfullargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper

@optional_debug
def a(x):
    pass

@optional_debug
def b(x, y, z):
    pass

@optional_debug
def c(x, y):
    pass

a(1)
b(1, 2, 3)
c(1, 2)
