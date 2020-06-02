#Simple Ping Pong bolte
import turtle
import random
import time


wn = turtle.Screen()
wn.title("PingPong by Wizard")
wn.bgcolor(random.choice(["Yellow", "Black" , "Navy"]))
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
 
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("White")
ball.penup()
ball.goto(-0,0)
ball.dx = 0.42
ball.dy = -0.42

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA:0  PlayerB:0", align="center", font=("Courier", 24, "normal"))

#Time
pen.write('Time:60s', align="center", font=("Courier", 24, "normal"))


#Functions
def paddle_a_up():
	y = paddle_a.ycor()
	y+= 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y-= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y+= 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y-= 20
	paddle_b.sety(y)

#Keyboard Binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Game LOOP
while True:
	wn.update() 

	#MoveTheBall
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border Checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("PlayerA:{}  Sonu:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("PlayerA:{}  Sonu:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

	
	#Paddle&Ball Collisions
	if (ball.xcor() > 340 and ball.xcor() > 350) and (ball.ycor() < paddle_b.ycor() + 40 ) and ball.ycor() > paddle_b.ycor() -40:
		ball.setx(340)
		ball.dx *= -1
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 ) and ball.ycor() > paddle_a.ycor() -40:
		ball.setx(-340)
		ball.dx *= -1