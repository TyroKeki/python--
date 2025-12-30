import turtle

class PhysicsTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.velocity = [0, 0]
        self.gravity = -0.1

    def update(self):
        """简化的物理更新"""
        x, y = self.pos()
        self.velocity[1] += self.gravity  # 重力
        self.goto(x + self.velocity[0], y + self.velocity[1])

        # 边界碰撞
        if y < -300:
            self.sety(-300)
            self.velocity[1] = -self.velocity[1] * 0.8  # 能量损失


# 创建弹跳球模拟
ball = PhysicsTurtle()
ball.shape("circle")
ball.penup()

while True:
    ball.update()