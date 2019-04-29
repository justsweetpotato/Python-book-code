#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle
import time

turtle.color('blue', 'red')

turtle.begin_fill()

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()
time.sleep(2)
turtle.done
