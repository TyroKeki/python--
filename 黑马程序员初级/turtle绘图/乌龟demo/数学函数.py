import turtle
import math


def plot_polar_function(r_func):
    """绘制极坐标函数 r = f(θ)"""
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    theta = 0
    while theta <= 2 * math.pi:
        r = r_func(theta)
        x = r * math.cos(theta) * 50
        y = r * math.sin(theta) * 50
        t.goto(x, y)
        t.pendown()
        theta += 0.01

# 示例：玫瑰曲线 r = cos(kθ)
plot_polar_function(lambda theta: math.cos(5 * theta))

