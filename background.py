from turtle import Turtle


class Background:
    def __init__(self):
        pass

    def drawroads(self):
        road1 = Turtle("road1")
        road2 = Turtle("road2")
        road3 = Turtle("road3")
        road1.color("grey")
        road2.color("grey")
        road3.color("grey")

    def drawwhites(self):
        for m in range(0,3):
            for n in range(0, 5):
                i = Turtle("white")
                i.setheading(90)
                i.color("white")
                i.penup()
                i.goto(((-250+(n*110)), -200 + (m*150)))
