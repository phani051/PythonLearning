from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scorecount = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())

        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.scorecount} High Score = {self.highscore}", align=ALLIGNMENT, font=FONT)
    # def update_scoreboard(self):
    #     self.write(f"Score : {self.scorecount}", align="center", font=("Arial", 10, "normal"))

    def increase_score(self):
        self.scorecount += 1
        self.clear()
        self.write(f"Score : {self.scorecount} High Score = {self.highscore}", align=ALLIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER!", align=ALLIGNMENT, font=FONT)

    def reset_game(self):
        if self.scorecount > self.highscore:
            self.highscore = self.scorecount
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.scorecount = 0
        self.clear()
        self.write(f"Score : {self.scorecount} High Score = {self.highscore}", align=ALLIGNMENT, font=FONT)




