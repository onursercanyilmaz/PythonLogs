from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
MOVE_DIST = 20
class Snake:
    start_position = [(0, 0), (-20, 0), (-40, 0)]
    seg = []
    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]

    def create_snake(self):
        for position in self.start_position:
            self.add_segment(position)


    def add_segment(self,position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.seg.append(segment)

    def extend(self):
        #add a new segment to snake
        self.add_segment(self.seg[-1].position())


    def move(self):
        for seg_num in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[seg_num - 1].xcor()
            new_y = self.seg[seg_num - 1].ycor()
            self.seg[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)
#snake can not go opposite way
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)