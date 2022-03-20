import time
from turtle import Screen
from turtle import Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from background import Background

CAR = ((0, -3), (0, -5), (-3, -5), (-3, -3),
       (-3.5, -3), (-3.5, -2.5), (-3, -2.5), (-3, 2.5),
       (-3.5, 2.5), (-3, 2.5), (-3, 3), (-3, 5),
       (0, 5), (0, 3), (3, 3), (3, -3))
PLAYER1 = ((6, 12), (6, 18), (10, 18), (10, 12),
           (14, 12), (14, 10), (10, 10), (10, 2),
           (6, 2), (6, 10), (2, 10), (2, 12))
WHITE = ((0, 60), (60, 60), (60, 40), (0, 40))
screen = Screen()
screen.register_shape("white", WHITE)
screen.register_shape("bg", ((0, -300), (300, -300), (300, 300), (0, 300)))
screen.register_shape("road1", ((-100, 300), (-200, 300), (-200, -300), (-100, -300)))
screen.register_shape("road2", ((-50, 300), (50, 300), (50, -300), (-50, -300)))
screen.register_shape("road3", ((200, 300), (100, 300), (100, -300), (200, -300)))
screen.register_shape("car", CAR)
screen.register_shape("player", PLAYER1)

screen.setup(width=600, height=600)
screen.tracer(0)
bg = Background()

player = Player()
score = Scoreboard()
car = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.movecars()

    screen.listen()
    screen.onkeypress(player.move, "Up")

    if player.ycor() > 280:
        player.reset()
        car.increaselevel()
        score.increaselevel()

    for cars in car.allcars:
        if cars.distance(player) < 20:
            score.gameover()
            game_is_on = False
screen.exitonclick()
