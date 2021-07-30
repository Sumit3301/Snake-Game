from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        self.score=0
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("red")
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        xrand=random.randint(-288,288)
        yrand=random.randint(-288,288)
        self.goto(xrand,yrand)
    
    def score_increment(self):
        self.score=self.score+1

        


