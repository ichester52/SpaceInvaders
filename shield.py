from turtle import Turtle

class Shield(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(0.75)
        self.penup()
        self.color('green')
        self.goto(position)
        self.left(90)
