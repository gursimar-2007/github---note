import turtle
import time
import random
# screen
screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("Sky Blue")
screen.setup(width=800, height=600)

# bird
bird = turtle.Turtle()
bird.shape("circle")
bird.color("yellow")
bird.penup()
bird.dy = 0

top_pipe = turtle.Turtle()
top_pipe.shape("square")  
top_pipe.color("green")
top_pipe.shapesize(stretch_wid=10, stretch_len=2)  
top_pipe.penup()
top_pipe.goto(400,300)
# bottom pipe
bottom_pipe = turtle.Turtle()
bottom_pipe.shape("square")  
bottom_pipe.color("green")
bottom_pipe.shapesize(stretch_wid=20, stretch_len=2)  
bottom_pipe.penup()
bottom_pipe.goto(400,-300)
def jump():
    bird.dy = 5

screen.listen()
screen.onkeypress(jump, "space")

while True:
    bird.dy -= 0.2
    bird.sety(bird.ycor() + bird.dy)
    top_pipe.setx(top_pipe.xcor() - 10)
    gap=random.randint(-100,100)
    bottom_pipe.setx(bottom_pipe.xcor() - 10)
    if top_pipe.xcor()< -400:
        top_pipe.goto(400,gap + 200)
    if bottom_pipe.xcor()< -400:
        bottom_pipe.goto(400,gap -200)
    screen.update()
    time.sleep(0.02)