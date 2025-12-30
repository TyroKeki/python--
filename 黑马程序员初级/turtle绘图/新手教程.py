from turtle import *
import time

def triangle():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    time.sleep(0.5)


def how_to_fill():
    color('red')
    fillcolor('yellow')
    speed(0)
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    time.sleep(0.5)

def rectangle():
    color('red')
    fillcolor('yellow')
    begin_fill()
    for i in range(4):
        forward(100)
        right(90)
    end_fill()
    time.sleep(0.5)

def random_example():
    from random import random
    for i in range(100):
        steps = int(random() * 100)
        angle = int(random() * 360)
        right(angle)
        fd(steps)

triangle()
clear()
rectangle()
clear()
how_to_fill()
mainloop()
