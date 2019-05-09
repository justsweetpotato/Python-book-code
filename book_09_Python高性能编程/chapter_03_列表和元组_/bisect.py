#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bisect
import random


def find_closet(haystack, needle):
    i = bisect.bisect_left(haystack, needle)  # 返回所在 value 的索引
    if i == len(haystack):
        return i - 1
    elif haystack[i] == needle:
        return i
    elif i > 0:
        j = i - 1
        if haystack[i] - needle > needle - [haystack][j]:
            return j
    return i


important_numbers = []
for i in range(10):
    new_number = random.randint(0, 1000)
    bisect.insort(important_numbers, new_number)

print(important_numbers)

closest_index = find_closet(important_numbers, -250)
print("Closest value to -250: ", important_numbers[closest_index])

closest_index = find_closet(important_numbers, 500)
print("Closest value to 500: ", important_numbers[closest_index])

closest_index = find_closet(important_numbers, 1100)
print("Closet value to 1100: ", important_numbers[closest_index])
