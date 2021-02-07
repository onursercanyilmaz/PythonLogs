from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def d():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def a():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def w():
    tim.forward(10)

def s():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(a,"a")
screen.onkey(s,"s")
screen.onkey(d,"d")
screen.onkey(w,"w")

screen.onkey(clear,"c")
screen.listen()
screen.exitonclick()