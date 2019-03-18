#!/usr/bin/env python

class Foo():
    def __init__(self, a):
        self.a = a

    def func(self):
        self.a = 2
        return self.a

f = Foo(1)
print(f.a)
print(f.func())
print(f.a)