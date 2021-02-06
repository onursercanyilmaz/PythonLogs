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


def draw_circle():
        timmy.pensize(2)
        timmy.left(25)
        timmy.circle(100)
        timmy.speed("fastest")


for walk in range(200):
     timmy.color(random_color())
     draw_circle()


"""
stops when reach the first circle
def draw_s(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
draw_s(5)
"""
screen = Screen()
screen.exitonclick()