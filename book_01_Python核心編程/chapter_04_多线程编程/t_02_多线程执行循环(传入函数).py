#!/usr/bin/env python

from atexit import register
import threading
from time import sleep, ctime, time

loops = [4, 2]


def loop(nloop, nsec):
    print("开始循环", nloop, 'at:', ctime())
    sleep(nsec)
    print("结束循环", nloop, 'at:', ctime())


def main():
    print("开始 at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    # for i in nloops:
    #     threads[i].join()

    # print("全部完成 at:", ctime())


@register
def _atexit():
    print("全部完成 at:", ctime())
    print("耗时 at:", time() - start_time)


if __name__ == '__main__':
    start_time = time()
    main()
    # register(_atexit)