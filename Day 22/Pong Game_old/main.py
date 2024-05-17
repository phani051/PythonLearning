from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

# net = Turtle("turtle")
# net.hideturtle()
# net.speed("fastest")
# net.penup()
# net.color("white")
# net.goto(0, 310)
# net.setheading(270)
# net.width(5)
# for _ in range(30):
#     net.forward(10)
#     net.penup()
#     net.forward(10)
#     net.pendown()

# Paddles creation and movement

PADDLE_POSITION = [(350, 0), (-350, 0)]

r_paddle = Paddle(PADDLE_POSITION[0])
l_paddle = Paddle(PADDLE_POSITION[1])

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# Ball

ball = Ball()

# Game logic

game_is_on = True

while game_is_on:
    time.sleep(0.2)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print('bangg')
        ball.bounce_x()

screen.listen()

screen.exitonclick()
