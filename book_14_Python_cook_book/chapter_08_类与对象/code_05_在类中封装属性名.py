#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        print('public_method')

    def _internal_method(self):
        print('_internal_method')


class B:
    def __init__(self):
        self.__private = 0
        self.test = 'test'

    def __private_method(self):
        print('__private_method')

    def public_method(self):
        print('public_method')
        print('[*] run __private_method from public_method')
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1


a = A()
print('[X] a.__internal:', a._internal)
print('[O] a.public:', a.public)
a.public_method()
a._internal_method()
print()
b = B()
print('[X] b.__private:', b._B__private)
b._B__private_method()
b.public_method()
print()
c = C()
print(c._C__private)
print(c._B__private)
print(c.test)