#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:
    def speak(self):
        print('Im A.speak')

    def run(self):
        print('Im A.run')


class B:
    def __init__(self):
        self._a = A()

    def sing(self):
        print('Im B.sing')

    def __getattr__(self, item):
        return getattr(self._a, item)


b = B()
b.sing()
b.speak()
b.run()
