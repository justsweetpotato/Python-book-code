#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 现在，假如你想实现单例模式（只能创建唯一实例的类），实现起来也很简单：

class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

# a = Spam()
# b = Spam()
# print(Spam.__dict__)
# # print(a is b)
# # c = Spam()
# print(a is c)
