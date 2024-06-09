from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5,0.5)
        locate=(random.randint(-220,220),random.randint(-220,220))
        self.goto(locate)
    def refresh(self):
        x_axis=random.randint(-220,220)
        y_axis=random.randint(-220,220)
        self.goto((x_axis,y_axis))
    
    
        
