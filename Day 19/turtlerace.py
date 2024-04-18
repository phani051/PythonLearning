from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? ").lower()

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-100)

all_turtles = []
ycor = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=ycor)
    ycor += 40
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtel = turtle.pencolor()
            if winning_turtel == user_bet:
                print(f"You have won, winner is {winning_turtel}")
            else:
                print(f"You have lost, winner is {winning_turtel}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
