from turtle import *


starting_position=[(0,0),(-20,0),(-40,0)]

class Snake:
    
    def __init__(self):
        self.segments=[]
        self.create_snake()    




    def create_snake(self):
        for i in starting_position:
            snake=Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(i)
            self.segments.append(snake)


    


        
    
    


    
    def mov(self):
        for segment in range(len(self.segments)-1,0,-1):
            x_axis=self.segments[segment-1].xcor()
            y_axis=self.segments[segment-1].ycor()
            self.segments[segment].goto((x_axis,y_axis))
        self.segments[0].forward(20)
    

            
