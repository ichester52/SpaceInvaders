from turtle import Screen, Turtle
from defender import Defender
from shield import Shield
import random
from invader import Invader
import time
from bomb import Bomb

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Space Invaders")
screen.tracer(0)
bomb_list = []

defender = Defender()

starting_x = -380
starting_y = -150
distances = [30, 35, 40, 45, 50,]
shield_pixels = []

for i in range(5):
    for i in range(22):
        current_shield = Shield((starting_x, starting_y))
        starting_x += random.choice(distances)
        shield_pixels.append(current_shield)
    starting_x = -380
    starting_y -= 10

starting_x_invader = -175
starting_y_invader = 230
invaders = []

for i in range(7):
    for j in range(3):
        new_invader = Invader((starting_x_invader, starting_y_invader))
        invaders.append(new_invader)
        starting_y_invader -= 50

    starting_y_invader = 230
    starting_x_invader += 50

count = 0

game = True

while game:
    screen.listen()
    screen.onkeypress(defender.move_right, "Right")
    screen.onkeypress(defender.move_left, "Left")
    screen.onkey(fun=defender.fire_projectile, key="space")
    screen.update()

    if invaders[0].xcor() > 380 or invaders[-1].xcor() >380:
        for invader in invaders:
            invader.change_velocity()

    elif invaders[0].xcor() < -380 or invaders[-1].xcor() < -380:
        for invader in invaders:
            invader.change_velocity()

    for invader in invaders:
            invader.move()

    for bullet in defender.bullets:
        if bullet.ycor() > 300:
            defender.bullets.remove(bullet)
        else:
            for invader in invaders:
                if invader.distance(bullet) < 11:
                    defender.bullets.remove(bullet)
                    bullet.hideturtle()
                    invaders.remove(invader)
                    invader.hideturtle()
            bullet.move()
        for shield in shield_pixels:
            if bullet.distance(shield) < 8:
                defender.bullets.remove(bullet)
                bullet.hideturtle()
                shield_pixels.remove(shield)
                shield.hideturtle()


    number_drops = 1
    chance = random.randint(1,90)
    if chance == 20:
        bomber = random.choice(invaders).drop_bomb(bomb_list)

    if len(bomb_list) > 0:
        for bomb in bomb_list:
            for shield in shield_pixels:
                if bomb.distance(shield) < 8:
                    bomb_list.remove(bomb)
                    bomb.hideturtle()
                    shield_pixels.remove(shield)
                    shield.hideturtle()

                elif bomb.distance(defender) < 15:
                    screen.clear()
                    screen.bgcolor("black")
                    turtle = Turtle()
                    turtle.pencolor('green')
                    turtle.hideturtle()
                    turtle.goto(-50, 0)
                    turtle.write('You Loose')
                    game = False
                    break

            bomb.move()

    if len(invaders) == 0:
        screen.clear()
        screen.bgcolor("black")
        turtle = Turtle()
        turtle.pencolor('green')
        turtle.hideturtle()
        turtle.goto(-50, 0)
        turtle.write('You Win')
        game = False





screen.exitonclick()

