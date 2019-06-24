#!/usr/bin/env python
# -*- coding: utf-8 -*-

def spam(a, b, c, d):
    print(a, b, c, d)


from functools import partial

s1 = partial(spam, 1)
s1(2, 3, 4)

s2 = partial(spam, d=42)
s2(1, 2, 3)

# ----------------分割线----------------
points = [(1, 2), (3, 4), (4, 6), (7, 8)]

import math


def distance(p1, p2):
    # 计算两个坐标点的距离
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


print(distance(points[1], points[2]))

# 按到原点的距离排序坐标点
pt = (0, 0)
points.sort(key=partial(distance, pt))
print(points)
