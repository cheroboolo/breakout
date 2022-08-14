import turtle

c_pos = [(-360, 150), (-270, 150), (-180, 150), (-90, 150), (0, 150), (90, 150), (180, 150), (270, 150), (360, 150), (-360, 200), (-270, 200), (-180, 200), (-90, 200), (0, 200), (90, 200), (180, 200), (270, 200), (360, 200)]
w_pos = [(-360, 50), (-270, 50), (-180, 50), (-90, 50), (0, 50), (90, 50), (180, 50), (270, 50), (360, 50), (-360, 100), (-270, 100), (-180, 100), (-90, 100), (0, 100), (90, 100), (180, 100), (270, 100), (360, 100)]


class Wall:
    def __init__(self):
        self.color_wall = []
        self.white_wall = []
        self.white_position()
        self.color_position()
        print(self.color_wall)
        print(self.white_wall)

    def white_position(self):
        for data in w_pos:
            new_seg_w = turtle.Turtle()
            new_seg_w.shape("square")
            new_seg_w.shapesize(stretch_len=4, stretch_wid=2)
            new_seg_w.color("white")
            new_seg_w.penup()
            new_seg_w.goto(data)
            self.white_wall.append(new_seg_w)

    def color_position(self):
        for data in c_pos:
            new_seg_c = turtle.Turtle()
            new_seg_c.shape("square")
            new_seg_c.shapesize(stretch_len=4, stretch_wid=2)
            new_seg_c.color("blue")
            new_seg_c.penup()
            new_seg_c.goto(data)
            self.color_wall.append(new_seg_c)




