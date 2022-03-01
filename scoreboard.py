from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def writescore(self):
        self.write(f"Score = {self.level}", align="center", font=FONT)

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-200, 250)
        self.writescore()

    def increaselevel(self):
        self.clear()
        self.level += 1
        self.writescore()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

