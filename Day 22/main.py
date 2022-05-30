from turtle import Screen
from paddles import Paddle
import time
from ball import Ball
import time 
import math 
from scoreboard import Scoreboard

myScreen = Screen ()
myScreen.setup(width= 800 , height=600)
myScreen.bgcolor("black")
myScreen.title("Pong")
myScreen.tracer(0)

scoreBoard = Scoreboard() 
# TODO 1: CENTRAL LINES 

rightPaddle = Paddle(350 , 0)

myScreen.listen()
myScreen.onkey(rightPaddle.up, "Up")
myScreen.onkey(rightPaddle.down,"Down")

leftPaddle = Paddle(-350 , 0)
myScreen.onkey(leftPaddle.up, "w")
myScreen.onkey(leftPaddle.down,"s")

ball = Ball()


game_on =True

y=1
gameSpeed = 0.1
while game_on:
    time.sleep(gameSpeed)
    myScreen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    elif ball.xcor() > 330 and ball.distance(rightPaddle) <  math.sqrt(20**2 + 25**2):
        ball.bounceX()
        gameSpeed *= 0.01
    elif ball.xcor() < -330 and ball.distance(leftPaddle) <  math.sqrt(20**2 + 25**2):
        ball.bounceX()
        gameSpeed *= 0.1
    elif ball.xcor() > 400:
        ball.restart()
        gameSpeed = 0.1
        scoreBoard.scoreRight += 1
        scoreBoard.clear()
        scoreBoard.printScore()
    elif ball.xcor() < -400:
        ball.restart()
        gameSpeed = 0.1
        scoreBoard.scoreLeft += 1
        scoreBoard.clear()
        scoreBoard.printScore()












myScreen.exitonclick()