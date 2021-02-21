from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)


    def write_score(self):
        self.clear()
        self.write(f"Score = {self.score}", move=False, align="center", font=("Arial", 15, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER!", align="center", font=("Arial", 25, "bold"))







