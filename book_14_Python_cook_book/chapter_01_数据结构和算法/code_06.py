#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


