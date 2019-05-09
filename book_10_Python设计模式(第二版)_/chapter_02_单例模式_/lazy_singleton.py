#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Singleton():
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called...")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()
print("Object created", Singleton.getInstance())
s1 = Singleton()

