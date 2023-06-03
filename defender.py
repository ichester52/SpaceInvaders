from turtle import Turtle
from bullet import Bullet
import time

class Defender(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('green')
        self.goto(0, -250)
        self.left(90)
        self.bullets = []
        self.last_shot_time = time.time()
        self.shot_cooldown = 1.0

    def move_right(self):
        if self.xcor() > 380:
            pass
        else:
            self.goto(self.xcor() + 8, -250)



    def move_left(self):
        if self.xcor() < -380:
            pass
        else:
            self.goto(self.xcor() - 8, -250)

    def fire_projectile(self):
        if time.time() - self.last_shot_time >= self.shot_cooldown:
            bullet = Bullet((self.xcor(), self.ycor()))
            bullet.move()
            self.bullets.append(bullet)
            self.last_shot_time = time.time()
