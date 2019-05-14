#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from collections import Counter
#
# some_data = [1, 1, 2, 3, "1", "1", "2"]
#
# result = Counter(some_data)
#
# if __name__ == '__main__':
#     print(result)

some_data = [1, 1, 2, 3, "1", "1", "2"]
counter = {}

for data in some_data:
    counter.setdefault(data, 0)
    if data in counter:
        counter[data] += 1

print(counter)
