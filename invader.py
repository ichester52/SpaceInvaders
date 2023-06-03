from turtle import Turtle
from bomb import Bomb

class Invader(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('red')
        self.shapesize(1)
        self.goto(position)
        self.right(90)
        self.velocity = 0.7

    def move(self):
        self.goto(self.xcor() + self.velocity, self.ycor())

    def change_velocity(self):
        self.velocity = self.velocity * -1

    def drop_bomb(self, bomb_list):
        bomb = Bomb((self.xcor(), self.ycor()))
        bomb_list.append(bomb)
        bomb.move()
