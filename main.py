from turtle import *
import random
import time


screen=Screen()

screen.title("My Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")


starting_position=[(0,0),(-20,0),(-40,0)]

segments=[]
screen.tracer(0)

for i in starting_position:
    snake=Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(i)
    segments.append(snake)

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment in segments:
        segment.forward(20)
screen.exitonclick()



