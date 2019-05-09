#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


def binary_search(needle, haystack):
    # 对已排序的列表的高效搜索, 二分搜索
    imin, imax = 0, len(haystack)
    while True:
        if imin >= imax:
            return -1
        midpoint = (imin + imax) // 2
        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] < needle:
            imin = midpoint + 1
        else:
            return midpoint


if __name__ == '__main__':
    list_a = [i for i in range(10000000)]
    number = 9999999
    start_time = time.time()
    print(binary_search(number, list_a))
    print("耗时:", time.time() - start_time)
    start_time = time.time()
    print(list_a.index(9999999))
    print("耗时:", time.time() - start_time)

