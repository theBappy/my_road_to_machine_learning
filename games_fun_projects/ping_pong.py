import turtle as t
import os


player_a_score = 0
player_b_score = 0


window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color('white')
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)


right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0, 0)
ball_dx = 0.2
ball_dy = 0.2

pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "Player A: 0 Player B: 0",
    align="center",
    font=("Arial", 24, "normal")
)

def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

while True:
    window.update()

    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)


    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

        if ball.ycor() < -290:
            ball.sety(290)
            ball_dy *= -1
        
        if ball.ycor() > 390:
            ball.goto(0, 0)
            ball_dx *= -1
            player_a_score += 1
            pen.clear()
            pen.write(
                "Player A : {}  Player B: {}".format(
                    player_a_score, player_b_score
                ),
                align="center",
                font=("Arial", 24, "normal"),
            )
        
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball_dx *= -1
            player_b_score += 1
            pen.clear()
            pen.write(
            "Player A: {}                    Player B: {} ".format(
                player_a_score, player_b_score
            ),
            align="center",
            font=("Arial", 24, "normal"),
            )

        if (
            (ball.xcor() > 340)
            and (ball.xcor() < 350)
            and (
                ball.ycor() < right_paddle.ycor() + 50
                and ball.ycor() > right_paddle.ycor() - 50
            )
        ):
            ball.setx(340)
            ball_dx *= -2

        if(
            (ball.xcor() < -340)
            and (ball.xcor() > -340)
            and (
                ball.ycor() < left_paddle.ycor() + 50
                and ball.ycor() > left_paddle.ycor() -50
            )
        ):
            ball.setx(-340)
            ball_dx *= -1
