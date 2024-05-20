import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# paddle = Turtle()
# paddle.penup()
# paddle.goto(350, 0)
# paddle.color("white")
# paddle.shape("square")
# paddle.shapesize(3,.8)

r_paddel = Paddle((350, 0))
l_paddel = Paddle((-350, 0))

screen.listen()
screen.onkey(l_paddel.move_up, "w")
screen.onkey(l_paddel.move_down, "s")
screen.onkey(r_paddel.move_up, "Up")
screen.onkey(r_paddel.move_down, "Down")

ball= Ball()

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()
