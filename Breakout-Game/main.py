from turtle import Screen
import time
from ball import Ball
from bricks import Bricks, all_t
from paddle import Paddle
from scoreboard import Scoreboard

##########
game_on = True

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Breakout")
##########
paddle = Paddle((0, -260))
ball = Ball()
scoreboard = Scoreboard()
bricks = Bricks()
##########
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
##########
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    
    if ball.ycor() > 280:
        ball.bounce_y()


    if ball.distance(paddle) < 80 and ball.ycor() < -250:
        ball.bounce_y()

    
    for t in all_t:
        if ball.distance(t) < 35:
            ball.bounce_y()
            scoreboard.add_point()
            all_t.remove(t)
            t.goto(500, 500)

            if len(all_t) == 0:
                game_on = False
                scoreboard.game_over()


##########
screen.exitonclick()