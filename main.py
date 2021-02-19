from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

# creation of screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong 🧚")
screen.tracer(0)

# creation of score board
score_board = ScoreBoard()

# creation of 2 paddles
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-360, 0))

# creation of ball
ball = Ball()

# link user key actions with paddle movements:
screen.listen()
screen.onkey(paddle_r.go_up, 'Up')
screen.onkey(paddle_r.go_down, 'Down')

screen.onkey(paddle_l.go_up, 's')
screen.onkey(paddle_l.go_down, 'w')

speed = 0.1
game_on = True
while game_on:
    ball.move()

    # Detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect ball collision with walls, reset ball position, reset speed
    if ball.xcor() > 380:
        time.sleep(0.5)
        score_board.l_point()
        ball.reset_position()
        speed = 0.1

    if ball.xcor() < -390:
        time.sleep(0.5)
        score_board.r_point()
        ball.reset_position()
        speed = 0.1

    # Detect collision with paddles, increase speed
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        speed -= 0.005

    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed -= 0.005

    screen.update()
    time.sleep(speed)

screen.exitonclick()
