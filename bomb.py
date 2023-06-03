from turtle import Turtle

class Bomb(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('arrow')
        self.penup()
        self.color('red')
        self.shapesize(0.5)
        self.goto(position)
        self.right(90)
        self.velocity = -1

    def move(self):
        self.goto(self.xcor(), self.ycor() + self.velocity)