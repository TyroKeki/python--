import turtle
import random
import time


def draw_bar(t, x, height, color="black"):
    """绘制单个条形"""
    t.penup()
    t.goto(x, 0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()

    for _ in range(2):
        t.left(90)
        t.forward(height * 3)  # 高度放大3倍
        t.left(90)
        t.forward(15)  # 宽度固定
    t.end_fill()
    t.penup()


def highlight_bars(t, data, index1, index2, color="red"):
    """高亮两个需要交换的条形"""
    x1 = index1 * 20 - 300
    x2 = index2 * 20 - 300

    # 清除原来的条形
    t.pencolor("white")
    t.fillcolor("white")
    for i in [index1, index2]:
        draw_bar(t, i * 20 - 300, 50)  # 用白色覆盖

    # 用红色重新绘制
    t.pencolor(color)
    t.fillcolor(color)
    draw_bar(t, x1, data[index1])
    draw_bar(t, x2, data[index2])

    # 短暂暂停，让用户看到高亮效果
    turtle.update()
    time.sleep(0.5)


def update_bars(t, data):
    """更新整个条形图显示"""
    t.clear()  # 清除所有图形
    for i, value in enumerate(data):
        draw_bar(t, i * 20 - 300, value)


def visualize_sort(data):
    # 设置窗口
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")
    screen.tracer(0)  # 关闭自动更新，手动控制

    # 创建海龟
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # 初始绘制条形图
    update_bars(t, data)
    turtle.update()  # 手动更新屏幕

    # 冒泡排序过程可视化
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                # 高亮要交换的两个条形
                highlight_bars(t, data, j, j + 1, "red")

                # 交换数据
                data[j], data[j + 1] = data[j + 1], data[j]

                # 更新显示
                update_bars(t, data)
                turtle.update()
                time.sleep(0.3)  # 控制速度

    # 最终用绿色标记排序完成
    for i in range(len(data)):
        highlight_bars(t, data, i, i, "green")
        turtle.update()
        time.sleep(0.05)

    turtle.done()


# 测试代码
if __name__ == "__main__":
    # 生成随机数据
    random.seed(42)
    data = [random.randint(10, 50) for _ in range(20)]
    print("原始数据:", data)

    # 开始可视化
    visualize_sort(data.copy())  # 使用副本，避免修改原数据