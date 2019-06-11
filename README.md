## Summary

This is Project is meant to demonstrate an example of a simple game development with Python.

### Requirements

* We will use the PyPi Package Turtle to create visuals and let them move
* If you want to make a sound when the ball is hit, you have to download a sound file (wav or mp3)

#### Step 1

* create a window with Turtle
* name your game
* set the color and size of the window
* run main loop to keep window open

<details>
<summary>Solution</summary>

<p>

```
import turtle

window = turtle.Screen()
window.title("Pong by Cuja")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

while True:
    window.update()

```

</p>
</details>

#### Step 2

* create paddles
* create the ball

<details>
<summary>Solution</summary>

<p>

```
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
```

</p>
</details>

#### Step 3

* let paddles move with function
* run function on keystroke

<details>
<summary>Solution</summary>

<p>

```
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

# Keyboard Binding

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

```

</p>
</details>

#### Step 4

* let the ball move over the screen
* the ball should move in x and y directions
* restrict the paddles from going off the screen

<details>
<summary>Solution</summary>

<p>

```
# directions
ball.dx = -2
ball.dy = -2

# in main loop let ball move constantly
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Paddle Restrictions

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

```

</p>
</details>

#### Step 5

* keep the ball in the window the whole time
* let the ball bounce off in the other direction on top and bottom
+ left and right of the window let the ball go back to the middle and start from there in the other direction

<details>
<summary>Solution</summary>

<p>

```
    # Border Checking (inside of the main loop)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

```

</p>
</details>

#### Step 6

* let the ball bounce off the paddles 

<details>
<summary>Solution</summary>

<p>

```
    # Paddle / Ball Collisions (inside the main loop)

    x_target_a = ball.xcor() < -340 and ball.xcor() > -350
    y_target_a = ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40

    x_target_b = ball.xcor() > 340 and ball.xcor() < 350
    y_target_b = ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40

    if x_target_a and y_target_a:
        ball.setx(-340)
        ball.dx *= -1

    if x_target_b and y_target_b:
        ball.setx(340)
        ball.dx *= -1

```

</p>
</details>

#### Step 7

* keep score by writing a scoreboard to the top
* update the scoreboard after every ball that moves past the paddles

<details>
<summary>Solution</summary>

<p>

```
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Spieler A: 0  -  Spieler B: 0", align="center", font=('Courier', 24, 'normal'))

# part of the border checking
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

```

</p>
</details>

The Complete Solution can be found in the pong.py file.