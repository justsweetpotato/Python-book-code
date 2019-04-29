#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)


def main():
    print(fact(0))
    print(fact(1))
    print(fact(5))


if __name__ == '__main__':
    main()

