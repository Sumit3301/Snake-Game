#Writing snake game on python using turtle library

from turtle import Turtle,Screen
import turtle
screen=Screen() #initilizing screen
screen.setup(width=600,height=600)#defining screen size
screen.title("Snake Game")



#Creating snake's body
starting_pos=[(0,0),(-20,0),(-40,0)]

for position in starting_pos:
    new_segment=Turtle("square")
    new_segment.color("Black")
    new_segment.goto(position)




screen.exitonclick() #Screen will exit on clik on screen

