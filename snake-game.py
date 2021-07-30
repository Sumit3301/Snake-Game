#Writing snake game on python using turtle library

from snake import Snake
from turtle import Turtle,Screen,goto
import time
import turtle
from food import Food
screen=Screen() #initilizing screen
screen.setup(width=600,height=600)#defining screen size
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


#Creating snake's body

game_is_on=True

#Animations of snake
while game_is_on:
    score=0
    screen.update()
    time.sleep(0.1)
    snake.move()
    if(snake.header.distance(food))<15:
        food.new_location()
        food.score_increment()


    
print(score)
screen.exitonclick() #Screen will exit on clik on screen


