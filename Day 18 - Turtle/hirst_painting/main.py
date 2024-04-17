import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
# timmy.pensize(100)

timmy.up()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.down()
timmy.hideturtle()

color_list = [(211, 154, 98), (53, 107, 131), (177, 78, 33), (198, 142, 35),
              (116, 155, 171), (124, 79, 98)]


def move_forward():
    for i in range(0, 10):
        timmy.dot(10, random.choice(color_list))
        timmy.up()
        timmy.forward(25)
        timmy.down()
        timmy.dot(10, random.choice(color_list))


def turn_left():
    timmy.up()
    timmy.setheading(90)
    timmy.forward(25)
    timmy.setheading(180)


def turn_right():
    timmy.up()
    timmy.setheading(90)
    timmy.forward(25)
    timmy.setheading(0)


for _ in range(0, 5):
    move_forward()
    turn_left()
    move_forward()
    turn_right()

screen = Screen()
screen.exitonclick()
