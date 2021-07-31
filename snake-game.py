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
score=0
#Animations of snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if(snake.header.distance(food))<15:
        
        food.new_location()
        snake.add_segment()

    if(snake.header.xcor()>280 or snake.header.xcor()<-280 or snake.header.ycor()>280 or snake.header.ycor()<-280):
        game_is_on=False
    for segment in snake.segments:
        if segment==snake.header:
            pass
        elif snake.header.distance(segment)<15:
            game_is_on=False

    

screen.exitonclick() #Screen will exit on clik on screen


