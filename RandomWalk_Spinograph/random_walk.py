from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("#EA4335")

import random

colours = ["#285078", "#9B2335", "#DFCFBE", "#7FCDCD", "#C3447A", "DeepSkyBlue", "#009B77","#660000","#ff99ff"]
my_color_tuple = (0,1,2,3,4,5,6,7,8,9)
#tuple is immutable
ways = [0,90,180,270]



def random_walk():
        timmy.pensize(15)
        timmy.forward(25)
        timmy.setheading(random.choice(ways))
        timmy.speed("fastest")


for walk in range(200):
    timmy.color(random.choice(colours))
    random_walk()


screen = Screen()
screen.exitonclick()