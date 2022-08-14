from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout Game")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
wall = Wall()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

count_lose = 0

game = True

while game:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    #collision with top y axis
    if ball.ycor() > 280:
        ball.bounce_y()

    #when player lose he have 5 guess
    if ball.ycor() < -350:
        count_lose += 1
        ball.bounce_y()
        ball.move_speed = 0.03

    #colision with x axis
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()


    #paddle have three segments for three directions(left,middle, right)
    if ball.distance(paddle.segments[0]) < 31 and ball.ycor() < -250:
        ball.x_move = -5
        ball.bounce_y()

    elif ball.distance(paddle.segments[1]) < 30 and ball.ycor() < -250:
        ball.x_move = 0
        ball.bounce_y()

    elif ball.distance(paddle.segments[2]) < 31 and ball.ycor() < -250:
        ball.x_move = 5
        ball.bounce_y()

    #collision with white wall
    for data in wall.white_wall:
        if ball.distance(data) < 41:
            ball.bounce_y()
            scoreboard.increase_score_w()
            data.goto(1000, 1000)

    #collision with color wall
    for data in wall.color_wall:
        if ball.distance(data) < 41:
            ball.move_speed *= 0.8
            ball.bounce_y()
            scoreboard.increase_score_c()
            data.goto(1000, 1000)

    if count_lose == 5:
        game = False
        scoreboard.game_over()
    elif scoreboard.score == 198:
        game = False
        scoreboard.win_game()


screen.exitonclick()

