from turtle import Turtle

class Scorecard(Turtle):
    score = 0
    high_score ='0'

    with open("file.txt","r") as file:
        high_score=file.read()

    def __init__(self):
        super().__init__()
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_wid=1, stretch_len=2)  # Adjust these values for the desired size
        self.goto(0, 270)
        self.update_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
        self.score = 0

        with open("file.txt","w") as file:
            file.write(self.high_score)
        self.update_score()

    def update_score(self):
        self.clear()
        with open("file.txt","r") as file:
            self.high_score=file.read()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()
