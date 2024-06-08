from turtle import *
import time


# screen=Screen()

# screen.title("My Snake Game")
# screen.setup(width=600,height=600)
# screen.bgcolor("black")


# starting_position=[(0,0),(-20,0),(-40,0)]

# segments=[]
# screen.tracer(0)

# for i in starting_position:
#     snake=Turtle("square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(i)
#     segments.append(snake)

# game_is_on=True

# def mov_left():
#     segments[0].left(90)

# def mov_right():
#     segments[0].right(90)

# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for segment in range(len(segments)-1,0,-1):
#         x_axis=segments[segment-1].xcor()
#         y_axis=segments[segment-1].ycor()
#         segments[segment].goto((x_axis,y_axis))
#     segments[0].forward(20)

# screen.listen()
# screen.onkey("a",mov_left)
# screen.onkey("d",mov_right)
# screen.exitonclick()

from snake_class import Snake

screen=Screen()

screen.title("My Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

game_on=True
snake=Snake()

screen.listen()

screen.onkey(snake.Up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.mov()
screen.exitonclick()
