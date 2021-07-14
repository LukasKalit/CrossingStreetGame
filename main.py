import time
from turtle import Screen
import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
level = 1
score_i = 2

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
scoreboard = Scoreboard()
scoreboard.score(level)

player = Player()
cars = CarManager()

screen.onkey(fun=player.run_turtle, key="w")

# main loop
game_is_on = True
while game_is_on:
    if level == score_i:
        scoreboard.score(level)
        score_i += 1

    for c in car_manager.cars_moving:
        if player.distance(c) < 23:
            scoreboard.game_over_print(level)
            game_is_on = False

    cars.start_game(level=level)
    level = player.win_level(level)
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
