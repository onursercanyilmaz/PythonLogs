import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()


    if player.ycor() >= 280:
        player.goto(0,-280)
        cars.level_up()
        score.increase_level()

#Collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()