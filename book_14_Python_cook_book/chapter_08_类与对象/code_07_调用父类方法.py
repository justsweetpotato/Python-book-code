#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在子类中调用父类某个已经被覆盖的方法.
class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()


b = B()
b.spam()


