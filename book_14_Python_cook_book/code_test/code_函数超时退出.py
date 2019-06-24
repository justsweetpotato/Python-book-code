#!/usr/bin/env python
# -*- coding: utf-8 -*-
from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut
import time


@func_set_timeout(5)  # 函数执行多少秒后退出
def task():
    index = 1
    while True:
        print('{} hello world!'.format(index))
        time.sleep(1)
        index += 1


if __name__ == '__main__':
    try:
        task()
    except FunctionTimedOut as e:
        print("超时退出...", str(e))
