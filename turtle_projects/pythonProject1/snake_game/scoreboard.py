from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 250)
        self.write(f"score = {self.counter}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):

        self.counter += 1
        self.clear()
        self.write(f"score = {self.counter}", align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
