from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gray")
        self.penup()
        self.goto(200, -300)
        self.x_move = 0
        self.y_move = 5
        self.move_speed = 0.03

    def move(self):

        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
