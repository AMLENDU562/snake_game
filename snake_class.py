from turtle import *

starting_position=[(0,0),(-20,0),(-40,0)]

class Snake:
    
    def __init__(self):
        self.segments=[]
        self.create_snake()    
        self.head=self.segments[0]

    def create_snake(self):
        for i in starting_position:
            snake=Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(i)
            self.segments.append(snake)
    
    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move segments out of the screen
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def add_segment(self, position):
        snake=Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def game_over(self):
        return self.segments[-1].distance(self.head) < 15
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_axis = self.segments[segment - 1].xcor()
            y_axis = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_axis, y_axis)
        self.head.forward(20)