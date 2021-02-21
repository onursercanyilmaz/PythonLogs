from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time
from snake import  Snake
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
score.write_score()
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect the collision between snake and food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.write_score()

    #Detect the collision between snake and the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game = False
        score.game_over()


    # Detect the collision between snake and the tail
    for segment in snake.seg[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            score.game_over()

"""
 for segment in snake.seg:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game = False
            score.game_over()

"""















screen.exitonclick()