import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    if player.ycor() > 280:
        player.reset()
        car.speed_up()
        scoreboard.incr_score()

    # Detect collision with Cars

    for i in car.all_cars:
        if i.distance(player) < 25:
            game_is_on = False

screen.exitonclick()
