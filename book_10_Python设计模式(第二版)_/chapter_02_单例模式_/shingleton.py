# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)

        return cls.instance


s1 = Singleton()
s2 = Singleton()
print(id(s1))
print(id(s2))



