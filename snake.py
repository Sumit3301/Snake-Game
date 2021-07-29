STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
from turtle import Turtle
class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.header=self.segments[0]
    
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment=Turtle("square")
            new_segment.color("Black")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.header.forward(MOVE_DIST)

    def up(self):
        self.header.setheading(90)

    def down(self):
        self.header.setheading(270)

    def left(self):
        self.header.setheading(180)

    def right(self):
        self.header.setheading(0)

        

        


    