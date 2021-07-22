#Writing snake game on python using turtle library

from turtle import Turtle,Screen,goto,xcor,ycor
import time
import turtle
screen=Screen() #initilizing screen
screen.setup(width=600,height=600)#defining screen size
screen.title("Snake Game")
screen.tracer(0)


#Creating snake's body
starting_pos=[(0,0),(-20,0),(-40,0)]
segments=[]
for position in starting_pos:
    new_segment=Turtle("square")
    new_segment.color("Black")
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on=True
#Animations of snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments)-1,0,-1):
        new_x=segments[seg-1].xcor()
        new_y=segments[seg-1].ycor()
        segments[seg]=goto(new_x,new_y)
    segments[0].forward(10)



screen.exitonclick() #Screen will exit on clik on screen

