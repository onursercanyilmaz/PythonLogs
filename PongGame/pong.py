from turtle import Turtle
UP = 90
DOWN = 270
class Pong(Turtle):

    def __init__(self,pong_side):
        super().__init__()
        self.create_pong(pong_side)




    def create_pong(self,position):
        self.shape("square")
        self.penup()
        self.goto(position)
        self.color("white")
        self.shapesize(5, 1)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)






