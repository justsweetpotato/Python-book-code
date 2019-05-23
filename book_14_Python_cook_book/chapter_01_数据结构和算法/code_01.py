#!/usr/bin/env python
# -*- coding: utf-8 -*-


def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


if __name__ == '__main__':
    print(drop_first_last([1, 2, 4]))
