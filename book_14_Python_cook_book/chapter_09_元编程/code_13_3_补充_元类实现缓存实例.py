#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name


a = Spam('Guido')
b = Spam('Diana')
c = Spam('Guido')
print(a is b)
print(a is c)