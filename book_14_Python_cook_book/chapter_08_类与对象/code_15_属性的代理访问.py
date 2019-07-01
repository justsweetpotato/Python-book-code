#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:
    def spam(self, x):
        print('This is A spam is:', x)

    def foo(self):
        print('This is A foo')


class B1:
    '''简单代理'''

    def __init__(self):
        self._a = A()

    def spam(self, x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass


class B2:
    '''使用 __getattr__ 的代理, 代理方法比较多的时候'''

    def __init__(self):
        self._a = A()

    def bar(self):
        print('This is B2 bar')

    def __getattr__(self, name):
        '''这个方法在访问 attribute 不存在的时候被调用'''
        return getattr(self._a, name)


b = B2()
b.bar()
b.spam(42)
b.foo()


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print('getattr', name)
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setter:', name, value)
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar', self.x, y)


s = Spam(2)
p = Proxy(s)

print(p.x)
p.bar(3)
p.x = 37

