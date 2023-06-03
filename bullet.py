from turtle import Turtle

class Bullet(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('arrow')
        self.shapesize(0.5)
        self.penup()
        self.color('green')
        self.goto(position)
        self.left(90)
        self.yvelocity = 1.6

    def move(self):
        self.goto(self.xcor(), self.ycor() + self.yvelocity)

    def check_boundry(self):
        if self.ycor() > 300:
            self.hideturtle()

