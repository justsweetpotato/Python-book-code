#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Calculator(object):
    def fib_cached(self, n, cache):
        if n < 2:
            return 1

        try:
            result = cache[n]
        except:
            cache[n] = self.fib_cached(n - 2, cache) + self.fib_cached(n - 1, cache)
            result = cache[n]

        return result


c = Calculator()
cache = {}

print(c.fib_cached(40, cache))
