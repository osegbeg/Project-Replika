from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.life = 3
        self.penup()
        self.hideturtle()
        self.score_position()
        self.life_position()


    def score_position(self):
        self.goto(-250, 250)
        # self.write(f"{self.score}/50", move=False, align='left', font=('Courier', 18, 'normal'))

    def life_position(self):
        self.goto(-150, 250)
        # self.write(f"{self.life}❤", move=False, align='left', font=('Courier', 18, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}/50", move=False, align='left', font=('Courier', 18, 'normal'))

    def update_life(self):
        self.life -= 1
        self.clear()
        self.write(f"{self.life}", move=False, align='left', font=('Courier', 18, 'normal'))