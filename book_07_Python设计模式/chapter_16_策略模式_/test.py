#!/usr/bin/env python
# -*- coding: utf-8 -*-

def execute(arg1, arg2, func=None):
    if func is None:
        return "缺少运算符, 无法计算"

    return func(arg1, arg2)


def addition(arg1, arg2):
    return arg1 + arg2


def subtraction(arg1, arg2):
    return arg1 - arg2


def main():
    print(execute(4, 6))
    print(execute(4, 6, addition))
    print(execute(4, 6, subtraction))



if __name__ == '__main__':
    main()
