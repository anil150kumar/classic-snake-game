import turtle
from turtle import Turtle


class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.setposition(0, 270)

        self.color("white")
        self.penup()
        self.score_board()

    def count_score(self):
        self.score += 1
        self.clear()
        self.score_board()

    def score_board(self):
        self.write(f"Score: {self.score}", False, align="center", font="Arial")

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False, align="center", font="Arial")
