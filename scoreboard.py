from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.white_score = 0
        self.color_score = 0
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(200, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.score = self.white_score + self.color_score
        self.write(f"Score: {self.score}", font=("Arial", 24, "normal"))

    def increase_score_w(self):
        self.white_score += 4
        self.update_scoreboard()

    def increase_score_c(self):
        self.color_score += 7
        self.update_scoreboard()

    def game_over(self):
        self.goto(-280, -150)
        self.write(f"GAME OVER, final score is: {self.score} ", font=("Arial", 36, "normal"))

    def win_game(self):
        self.goto(-280, -150)
        self.write(f"YOU ARE AWESOME, BRAVO", font=("Arial", 36, "normal"))
