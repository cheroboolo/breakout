import turtle

position = [(-60, -280), (0, -280), (60, -280)]


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.x_move = 20
        self.y_move = 20
        print(self.segments)

    def create_paddle(self):
        for pos in position:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.shapesize(stretch_len=3, stretch_wid=1.5)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def move_right(self):
        for seg in self.segments:
            seg.goto(seg.xcor() + self.x_move, seg.ycor())

    def move_left(self):
        for seg in self.segments:
            seg.goto(seg.xcor() - self.x_move, seg.ycor())

