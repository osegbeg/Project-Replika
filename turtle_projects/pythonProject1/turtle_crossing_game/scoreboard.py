from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-250,250)

    def current_score(self):
        self.write(f"Level: {self.score}", False, "left", font=FONT)

    def increment_score(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.clear()
        self.goto(-100, 0)
        self.write(f"Your Score is: {self.score}", False, "left", font=FONT)
        self.goto(-100, 150)
        self.write("GAME OVER", False, "left", font=FONT)


