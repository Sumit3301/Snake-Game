STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
from turtle import Turtle
class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
    

    def create_snake():
        for position in STARTING_POSITIONS:
            new_segment=Turtle("square")
            new_segment.color("Black")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        
#Animations of snake
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DIST)
    

        


    