#Writing snake game on python using turtle library

from turtle import Turtle,Screen
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
    for seg in segments:
        seg.forward(20)
        screen.update()
    time.sleep(1)    


screen.exitonclick() #Screen will exit on clik on screen

