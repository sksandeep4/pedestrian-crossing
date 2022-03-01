# import turtle
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allcars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rc = random.randint(1, 6)
        if rc == 1:
            new_car = Turtle()
            # new_car.lt(180)
            new_car.shape("car")

            new_car.shapesize(stretch_wid=2, stretch_len=3)
            new_car.penup()
            new_car.setheading(180)
            # new_car.lt(90)
            new_car.color(random.choice(COLORS))
            new_car.goto(-300, random.choice([random.randint(-40, 45),
                                             random.randint(-190, -105), random.randint(110, 195)]))
            self.allcars.append(new_car)

    def movecars(self):
        for car in self.allcars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increaselevel(self):
        self.carspeed += MOVE_INCREMENT
