from turtle import *
import time
from snake_class import Snake
from Food_Allocate import Food 
from Score_card import Scorecard

screen = Screen()
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

game_on = True
snake = Snake()
food = Food()
score = Scorecard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        snake.extend()
        score.increase_score()
        food.refresh()

    if (
        snake.head.xcor() > 280
        or snake.head.ycor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() < -280
    ):
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

    # Exit game loop when player closes the window
    if screen.window_width() == 0 or screen.window_height() == 0:
        game_on = False

screen.exitonclick()
