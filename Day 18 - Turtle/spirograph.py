import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


timmy.speed('fastest')
timmy.width(2)
ang = 0
while ang < 361:
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(ang)
    ang += 10

screen.exitonclick()
