#Writing snake game on python using turtle library

from snake import Snake
from turtle import Turtle,Screen,goto
import time
import turtle
screen=Screen() #initilizing screen
screen.setup(width=600,height=600)#defining screen size
screen.title("Snake Game")
screen.tracer(0)

snake=Snake

#Creating snake's body

game_is_on=True
#Animations of snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    
    

screen.exitonclick() #Screen will exit on clik on screen

