import turtle
import time
from math import *

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
TA.hideturtle()

TA.begin_fill()
t = 0
while TA.xcor() <= 1000:
    x = t * 30 - 1000
    y = 300  * sin(t)

    if t == 0:
        TA.penup()
        TA.goto(x, y)
        TA.pendown()

    t += 0.05
    TA.goto(x, y)


t = 0
while t <= 2 * pi + 0.5:
    x = 300 * cos(t)
    y = 300 * sin(t)

    if t == 0:
        TA.penup()
        TA.goto(x, y)
        TA.pendown()

    t += 0.05
    TA.goto(x, y)
TA.end_fill()

SC.update()
SC.mainloop()
