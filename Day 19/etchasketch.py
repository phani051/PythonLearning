from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_anticlock():
    tim.lt(10)


def move_clock():
    tim.rt(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_anticlock, "a")
screen.onkey(move_clock, "d")
screen.onkey(clear, "c")

screen.listen()
screen.exitonclick()
