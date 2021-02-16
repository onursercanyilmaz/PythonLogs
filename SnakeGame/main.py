from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

start_position = [(0,0),(-20,0),(-40,0)]
seg = []
for position in start_position:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    seg.append(segment)


game = True

while game:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(seg)-1,0, -1):
        new_x = seg[seg_num - 1].xcor()
        new_y = seg[seg_num - 1].ycor()
        seg[seg_num].goto(new_x,new_y)
    seg[0].forward(20)
    seg[0].left(90)









screen.exitonclick()