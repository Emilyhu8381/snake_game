from turtle import Turtle, Screen

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write(f"Score:{self.score}", align='center', font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}", align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(x=0,y=0)
        print(self.write("GAME OVER", align='center', font=('Courier', 20, 'normal')))


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
