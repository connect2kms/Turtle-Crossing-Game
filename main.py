import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
level = Scoreboard()
cars = CarManager()

screen.onkey(turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create Cards and move left
    cars.create_car()
    cars.move_cars()

    # Detect collision with Car
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            level.game_over()

    # Turtle reach top
    if turtle.is_at_finish_line():
        turtle.reset()
        level.up()
        cars.level_up()

screen.exitonclick()
