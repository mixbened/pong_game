# Tut Source : https://www.youtube.com/watch?v=C6jJg9Zan7w

import turtle
import os

window = turtle.Screen()
window.title("Pong by Cuja")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Scoreboard
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Spieler A: 0  -  Spieler B: 0", align="center", font=('Courier', 24, 'normal'))

# Functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def close():
    turtle.bye()

# BONUS
def sound():
    os.system("afplay jump.wav&")

# Keyboard Binding

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
window.onkeypress(close, "Escape")

# Main Game Loop

while True:
    window.update()

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # BONUS
        sound()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # BONUS
        sound()

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Spieler A: " + str(score_a) + "  -  Spieler B: " + str(score_b) , align="center", font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Spieler A: " + str(score_a) + "  -  Spieler B: " + str(score_b) , align="center", font=('Courier', 24, 'normal'))

    # Paddle / Ball Collisions

    x_target_a = ball.xcor() < -340 and ball.xcor() > -350
    y_target_a = ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40

    x_target_b = ball.xcor() > 340 and ball.xcor() < 350
    y_target_b = ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40

    if x_target_a and y_target_a:
        # BONUS
        sound()
        ball.setx(-340)
        ball.dx *= -1

    if x_target_b and y_target_b:
        # BONUS
        sound()
        ball.setx(340)
        ball.dx *= -1


    # Paddle Restrictions

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)