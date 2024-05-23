import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

net = Turtle("turtle")
net.hideturtle()
net.speed("fastest")
net.penup()
net.color("white")
net.goto(0, 310)
net.setheading(270)
net.width(5)
for _ in range(30):
    net.forward(10)
    net.penup()
    net.forward(10)
    net.pendown()

# paddle = Turtle()
# paddle.penup()
# paddle.goto(350, 0)
# paddle.color("white")
# paddle.shape("square")
# paddle.shapesize(3,.8)

r_paddel = Paddle((350, 0))
l_paddel = Paddle((-350, 0))

screen.listen()
screen.onkeypress(l_paddel.move_up, "w")
screen.onkeypress(l_paddel.move_down, "s")
screen.onkeypress(r_paddel.move_up, "Up")
screen.onkeypress(r_paddel.move_down, "Down")

ball = Ball()
scoreboard = Scoreboard()

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collission
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collission with paddel
    if ball.xcor() > 325 and ball.distance(r_paddel) < 50 or ball.xcor() < -325 and ball.distance(l_paddel) < 50:
        ball.bounce_x()

    # Detect ball going beyond paddle

    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
