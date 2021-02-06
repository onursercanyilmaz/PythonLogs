from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("#EA4335")
"""

for i in range(15):
    timmy.forward(10)
    timmy.pencolor("white")
    timmy.forward(10)
    timmy.pencolor("black")
    #- - - - - - - - - -
    
  
for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
#- - - - - - - - - -
"""

import random
colours = ["blue", "red", "green", "yellow", "black", "DeepSkyBlue"]

k =0
flag = 2
for i in range(100):
    while k <= flag:
        timmy.fd(100)
        timmy.begin_poly()
        timmy.left(360/(i+3))
        k+=1
    flag+=1
    k = 0
    timmy.color(random.choice(colours))

"""
def draw_shape(num_sides):
    angle = 360 / num/sides
    for _ in range(num_sides):
    timmy.forward(100)
    timmy.right(angle)
    
for shape_side_n in range(3,11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)
"""


screen = Screen()
screen.exitonclick()