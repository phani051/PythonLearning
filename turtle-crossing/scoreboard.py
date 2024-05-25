from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def incr_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        pass

