import turtle
import time
from math import *
from draw_tools import draw_axes

SC = turtle.Screen()
SC.colormode(255)
SC.bgcolor((180,180,180))
SC.setup(1500,750)
SC.setworldcoordinates(-1000,-500,1000,500)
# SC.tracer(0)

TA = turtle.Turtle()
TA.color('red')
TA.fillcolor('yellow')
TA.speed(0)
TA.width(2)
# TA.hideturtle()

t = 0
while t <= 2 * pi:
    x = 100 * cos(t)
    y = 100 * sin(t)
    if t == 0:
        TA.teleport(x, y)
        TA.begin_fill()

    t += 0.05
    TA.goto(x, y)
TA.end_fill()


SC.tracer(0)
axis = turtle.Turtle()
draw_axes(axis, -1000, 1000, -500, 500, step=50)
SC.update()
SC.tracer(1)
SC.mainloop()
