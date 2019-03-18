#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip3 install line_profiler

import line_profiler
import sys


def test():
    for i in range(10):
        print(i ** 2)
    print("End of the function")


prof = line_profiler.LineProfiler(test)  # 传入函数

prof.enable()  # 开始性能分析
test()
prof.disable()  # 停止性能分析

prof.print_stats(sys.stdout)  # 打印性能分析结果