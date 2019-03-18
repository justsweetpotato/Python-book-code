#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.total = count

    def run(self):
        for i in range(self.total):
            time.sleep(1)
            print('Thread: %s - %s' % (self.name, i))


if __name__ == '__main__':
    t = MyThread(4)
    t2 = MyThread(3)

    t.start()
    t2.start()

    print('This program has finished')
