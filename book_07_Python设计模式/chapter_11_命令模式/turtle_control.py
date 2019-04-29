#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle

turtle.setup(400, 400)

screen = turtle.Screen()

screen.title("Keyboard drawing!")

t = turtle.Turtle()
distance = 10


def advance():
    t.forward(distance)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def retreat():
    t.backward(10)


def quit():
    screen.bye()


screen.onkey(advance, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(retreat, "s")
screen.onkey(quit, "Escape")
screen.listen()
screen.mainloop()
