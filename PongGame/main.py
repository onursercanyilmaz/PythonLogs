from turtle import Turtle, Screen
from pong import Pong
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG")
screen.tracer(0)


left_pos = (-375, 0)
right_pos = (375, 0)

l_pong = Pong((left_pos))
r_pong = Pong((right_pos))

ball = Ball()
score = Scoreboard()




screen.listen()
screen.onkey(r_pong.up, "Up")
screen.onkey(r_pong.down, "Down")

screen.onkey(l_pong.up, "w")
screen.onkey(l_pong.down, "s")




game = True
while game:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Detect the collision with ball, top and bottom.
    #code
    #if something:
        #ball.turn_way()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pong) < 50 and ball.xcor() > 340 or ball.distance(l_pong) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 400 :
        ball.ball_reset()
        score.l_point()

    if ball.xcor() < -400:
        ball.ball_reset()
        score.r_point()




screen.exitonclick()