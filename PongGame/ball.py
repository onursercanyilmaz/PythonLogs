from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("blue")



    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor() +self.y_move
        self.goto(new_x,new_y)


    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *=0.8
    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.1

