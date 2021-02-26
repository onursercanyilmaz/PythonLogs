FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280,250)
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def increase_level(self):
        self.clear()
        self.level +=1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER! ", align="center",font=FONT)







