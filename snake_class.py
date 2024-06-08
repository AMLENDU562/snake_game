from turtle import *
import time

class Snake:
    def mov():
        while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(segments)-1,0,-1):
        x_axis=segments[segment-1].xcor()
        y_axis=segments[segment-1].ycor()
        segments[segment].goto((x_axis,y_axis))
    segments[0].forward(20)
    screen.listen()
    screen.onkey(key="a",fun=mov_left)
    screen.onkey(key="d",fun=mov_right)