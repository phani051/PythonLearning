from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scorecount = 0
        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.scorecount}", align=ALLIGNMENT, font=FONT)
    # def update_scoreboard(self):
    #     self.write(f"Score : {self.scorecount}", align="center", font=("Arial", 10, "normal"))

    def increase_score(self):
        self.scorecount += 1
        self.clear()
        self.write(f"Score : {self.scorecount}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align=ALLIGNMENT, font=FONT)



