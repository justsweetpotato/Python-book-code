#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class A:
#     def spam(self, x):
#         print('A.spam', x)
#
#     def foo(self):
#         print('A.foo')
#
#
# class B(A):
#     def spam(self, x):
#         print('B.spam', x)
#         super().spam(x)
#
#     def bar(self):
#         print('B.bar')


class A:
    def spam(self, x):
        print('A.spam', x)

    def foo(self):
        print('A.foo')


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print('B.spam', x)
        self._a.spam(x)

    def bar(self):
        print('B.bar')

    def __getattr__(self, name):
        return getattr(self._a, name)


b = B()
b.spam(3)
b.bar()
b.foo()
