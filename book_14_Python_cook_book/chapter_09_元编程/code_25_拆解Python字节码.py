#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想通过将你的代码反编译成低级的字节码来查看它底层的工作机制。

# dis 模块可以被用来输出任何Python函数的反编译结果。例如：

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff!')

import dis
dis.dis(countdown)

# 当你想要知道你的程序底层的运行机制的时候，dis 模块是很有用的。比如如果你想试着理解性能特征。 被 dis() 函数解析的原始字节码如下所示：

print(countdown.__code__.co_code)

