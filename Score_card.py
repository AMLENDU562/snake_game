from turtle import Turtle

class Scorecard(Turtle):
    score=0
    def __init__(self):
        super().__init__()
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.shapesize(20)
        self.goto((0,270))
        self.write(f"Score {self.score}",True,align="center",font=('Arial', 20, 'normal'))
    def game_over(self):
        self.goto((0,270))
        self.write(f"Score {self.score}",True,align="center",font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.clear()
        self.score=self.score+1
        self.goto((0,270))
        self.game_over()

    


