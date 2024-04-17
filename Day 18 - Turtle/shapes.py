from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
colors = ["blue", "lime green", "navajo white", "purple", "plum", "medium turquoise"]

i = 4
while i < 11:
    timmy.color(random.choice(colors))
    for _ in range(i):
        timmy.forward(100)
        timmy.right(360 / i)
    i += 1

# timmy.color("red")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# timmy.color("blue")
# for _ in range(5):
#     timmy.forward(100)
#     timmy.right(72)
# timmy.color("green")
# for _ in range(6):
#     timmy.forward(100)
#     timmy.right(60)
#
# timmy.color("pink")
# for _ in range(8):
#     timmy.forward(100)
#     timmy.right(45)
#
# timmy.color("yellow")
# for _ in range(9):
#     timmy.forward(100)
#     timmy.right(40)
#
# timmy.color("orange")
# for _ in range(10):
#     timmy.forward(100)
#     timmy.right(36)


screen = Screen()
screen.exitonclick()
