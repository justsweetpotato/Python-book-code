#!/usr/bin/env python

from time import sleep, ctime, time


def loop0():
    print("开始 loop0 at:", ctime())
    sleep(4)
    print("结束 loop0 at:", ctime())


def loop1():
    print("开始 loop1 at:", ctime())
    sleep(2)
    print("结束 loop1 at:", ctime())


def main():
    print("全部开始 at:", ctime())
    loop0()
    loop1()
    print("全部结束 at:", ctime())


if __name__ == '__main__':
    star_time = time()
    main()
    print("耗时:", time() - star_time)


