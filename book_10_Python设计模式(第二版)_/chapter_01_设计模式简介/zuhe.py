#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(object):
    def a1(self):
        print("a1")


class B(object):
    def b(self):
        print("b")
        A().a1()


if __name__ == '__main__':
    objectB = B()
    objectB.b()
