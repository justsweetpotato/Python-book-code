#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(object):
    def __init__(self):
        print("I am A's __init__")


class B(A):
    # 默认隐式继承父类的 __init__

    # 重写父类的 __init__
    # def __init__(self):
    #     print("I am B's __init")

    # 显示继承父类的 __init__
    def __init__(self):
        # super(B, self).__init__()
        super().__init__()


b = B()
