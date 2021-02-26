COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE



    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            c = Turtle("square")
            c.penup()
            c.shapesize(1,2)
            c.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            c.goto(300,random_y)
            self.all_cars.append(c)


    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT










