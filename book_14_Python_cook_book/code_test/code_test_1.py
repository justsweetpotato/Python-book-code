#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def pwd(func):
    def wrapper():
        print(os.getcwd())
        return func
    return wrapper

@pwd
def pp():
    return "已完成"