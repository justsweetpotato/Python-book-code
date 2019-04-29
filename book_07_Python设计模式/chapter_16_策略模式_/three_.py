#!/usr/bin/env python
# -*- coding: utf-8 -*-

def executor(arg1, arg2, func=None):
    if func is None:
        return "Stratedy not impolemented..."
    return func(arg1, arg2)


def strategy_addition(arg1, arg2):
    return arg1 + arg2


def strategy_subtraction(arg1, arg2):
    return arg1 - arg2


def main():
    print(executor(4, 6))
    print(executor(4, 6, strategy_addition))
    print(executor(4, 6, strategy_subtraction))


if __name__ == '__main__':
    main()
