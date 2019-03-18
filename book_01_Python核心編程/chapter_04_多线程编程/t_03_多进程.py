#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process
import os
import time

def run_proc():
    """子进程要执行的代码"""
    time.sleep(5)
    print('子进程运行中，ppid=%d... pid=%d...' % (os.getppid(), os.getpid()))  # os.getpid获取当前进程的进程号
    print('子进程将要结束...')

if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
    p1 = Process(target=run_proc)
    p2 = Process(target=run_proc)
    p1.start()
    p2.start()
    print('父进程运行完毕')