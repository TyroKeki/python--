import turtle

def sci(trc=1):
    SC = turtle.Screen()
    SC.colormode(255)
    SC.bgcolor((180, 180, 180))
    SC.setup(1500, 750)
    SC.setworldcoordinates(-1000, -500, 1000, 500)
    SC.tracer(trc)
    return SC


def tti():
    TA = turtle.Turtle()
    TA.color('red')
    TA.fillcolor('yellow')
    TA.speed(0)
    TA.width(2)
    return TA

def draw_axes(t, x_min, x_max, y_min, y_max, step=1):
    # 绘制 x 轴
    t.penup()
    t.goto(x_min, 0)
    t.pendown()
    t.goto(x_max, 0)
    # x 轴箭头
    t.penup()
    t.goto(x_max - 0.3, 0.1)
    t.pendown()
    t.goto(x_max, 0)
    t.goto(x_max - 0.3, -0.1)

    # 绘制 y 轴
    t.penup()
    t.goto(0, y_min)
    t.pendown()
    t.goto(0, y_max)
    # y 轴箭头
    t.penup()
    t.goto(-0.1, y_max - 0.3)
    t.pendown()
    t.goto(0, y_max)
    t.goto(0.1, y_max - 0.3)

    # x 轴刻度和标签
    x = x_min
    while x <= x_max:
        if abs(x) < 1e-5:  # 跳过原点（已有 y 轴）
            x += step
            continue
        t.penup()
        t.goto(x, 0)
        t.pendown()
        t.goto(x, 0.05 if x > 0 else -0.05)  # 小刻度线
        t.penup()
        t.goto(x, -0.15)
        t.write(f"{x:.0f}", align="center", font=("Arial", 8, "normal"))
        x += step

    # y 轴刻度和标签
    y = y_min
    while y <= y_max:
        if abs(y) < 1e-5:  # 跳过原点
            y += step
            continue
        t.penup()
        t.goto(0, y)
        t.pendown()
        t.goto(0.05 if y > 0 else -0.05, y)
        t.penup()
        t.goto(-0.3, y - 0.05)
        t.write(f"{y:.0f}", align="right", font=("Arial", 8, "normal"))
        y += step

def easy_axis(SC):
    SC.tracer(0)
    axis = turtle.Turtle()
    draw_axes(axis, -1000, 1000, -500, 500, step=50)
    SC.update()
    SC.tracer(1)


if __name__ == '__main__':
    SC = turtle.Screen()
    SC.colormode(255)
    SC.bgcolor((180, 180, 180))
    SC.setup(1500, 750)
    SC.setworldcoordinates(-1000, -500, 1000, 500)
    SC.tracer(0)
    axis = turtle.Turtle()
    draw_axes(axis, -1000,1000,-500,500, 50)
    SC.update()
    SC.mainloop()