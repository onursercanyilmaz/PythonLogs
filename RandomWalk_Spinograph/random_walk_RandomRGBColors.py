from turtle import Turtle, Screen
import  turtle as t
timmy = Turtle()
timmy.shape("turtle")
timmy.color("#EA4335")
t.colormode(255)
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb = (r, g, b)

    # tuple is immutable
    return random_rgb


def random_walk():
        timmy.pensize(15)
        timmy.forward(25)
        timmy.setheading(random.choice(ways))
        timmy.speed("fastest")

ways = [0,90,180,270]



for walk in range(200):
    timmy.color(random_color())
    random_walk()


screen = Screen()
screen.exitonclick()