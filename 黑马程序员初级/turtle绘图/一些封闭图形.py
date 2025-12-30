from draw_tools import sci,tti,draw_axes,easy_axis
from math import sin,cos,pi
import turtle
import time

SC = sci()
TA = tti()
easy_axis(SC)

"""摆线"""
t = 0
while t <= 2 * pi:
    x = 100 * (t - sin(t))
    y = 100 * (1 - cos(t))

    if t == 0:
        TA.teleport(x,y)
        TA.begin_fill()

    t += 0.05
    TA.goto(x,y)
TA.end_fill()

easy_axis(SC)
time.sleep(2)
TA.clear()

"""星形线"""
t = 0
while t <= 2 * pi:
    x = 100 * ( cos(t) ) ** 3
    y = 100 * ( sin(t) ) ** 3

    if t == 0:
        TA.teleport(x,y)
        TA.begin_fill()

    t += 0.05
    TA.goto(x,y)
TA.end_fill()

easy_axis(SC)
time.sleep(2)
TA.clear()

SC.mainloop()