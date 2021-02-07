from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(600,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "yellow", "green", "blue", "purple","orange"]
all_turtles = []
"""
def create_Turtle(x,y,color):
    name = Turtle("turtle")
    c = random.choice(color)
    name.color(c)
    color.remove(c)
    name.penup()
    name.goto(x,y)

create_Turtle(-250,-120,colors)
create_Turtle(-250,-70,colors)
create_Turtle(-250,-20,colors)
create_Turtle(-250,30,colors)
create_Turtle(-250,80,colors)
create_Turtle(-250,130,colors)
"""

y_positions = [-120,-70,-20,30,80,130]

for turtle_index in range(0,6):
    tim = Turtle("turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-250,y_positions[turtle_index])
    all_turtles.append(tim)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:


    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} turtle is winner!")
            else:
                print(f"You lost! {winning_color} turtle is winner!")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()