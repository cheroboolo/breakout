# Breakout game with Turtle, Python

    * You can try out the gameplay here:

        [Breakout game example](https://elgoog.im/breakout/)
    
    * This game is OOP version, where I split parts for simple code(ball.py, wall.py, paddle.py, scoreboard.py)
    * main.py connects all classes and objects

### Requirements

##### Time Module:

[Time docs](https://docs.python.org/3/library/time.html)

##### Turtle Module
[Turtle docs](https://docs.python.org/3/library/turtle.html)

### Usage

* scoreboard counts collision with white square as 4 points, 
  or collision with blue square as 7 points and update scoreboard on top.
* wall class create objects on screen and positioning.
* After ball passes the paddle, ball will automatically will bounce back and you'll lose one try.
* you have 5 guesses to try throw all squares. When you hit square, your ball speed will increase, 
  then you need to move paddle faster.
* if you hit all squares there is winning message and games stop, look for your points.
    
    
### Ideas for future improvements

##### This script as any other have always space for improvements.
    
* precise ball pixel cordinates,
* another color row with different score point for calculation final score,
* with scoreboard, track more info, as number of repeat, count time of play(what is the fastest play vs slowest,
* save score to text and open with every new start.
* more levels, for additional segments.

![Example GUI](https://github.com/cheroboolo/breakout/blob/master/breakout-img.jpg?raw=true "Title")