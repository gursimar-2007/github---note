import turtle
import time
import random
import os  


script_dir = os.path.dirname(os.path.abspath(__file__))
# Build the correct path: G:\gs\c programming\FSV_C\FSV_C\bird.gif
gif_path = os.path.join(script_dir, "bird.gif")

# screen
screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("Sky Blue")
screen.setup(width=800, height=600)

# Register the custom GIF shape using the full absolute path
screen.register_shape(gif_path)

# bird
bird = turtle.Turtle()
bird.shape(gif_path)  # Set the bird to use the full GIF path
bird.penup()
bird.dy = 0

# top pipe
top_pipe = turtle.Turtle()
top_pipe.shape("square")  
top_pipe.color("green")
top_pipe.shapesize(stretch_wid=15, stretch_len=3)
top_pipe.penup()
top_pipe.goto(400, 300)

# bottom pipe
bottom_pipe = turtle.Turtle()
bottom_pipe.shape("square")  
bottom_pipe.color("green")
bottom_pipe.shapesize(stretch_wid=15, stretch_len=3)  
bottom_pipe.penup()
bottom_pipe.goto(400, -300)

def jump():
    bird.dy = 6  

score=0
screen.listen()
screen.onkeypress(jump, "space") 
run=True
while run:
    # Gravity and physics
    bird.dy -= 0.25
    bird.sety(bird.ycor() + bird.dy)

    # Move pipes left
    top_pipe.setx(top_pipe.xcor() - 4)
    bottom_pipe.setx(bottom_pipe.xcor() - 4)

    # Reset pipes
    if top_pipe.xcor() < -400:
        gap_y = random.randint(-100, 100)
        top_pipe.goto(400, gap_y + 250)
        bottom_pipe.goto(400, gap_y - 250)

    # Collision detection
    if (bird.xcor() + 20 > top_pipe.xcor() - 30 and 
        bird.xcor() - 20 < top_pipe.xcor() + 30 and 
        bird.ycor() + 20 > top_pipe.ycor() - 150):
        run = False

    if (bird.xcor() + 20 > bottom_pipe.xcor() - 30 and 
        bird.xcor() - 20 < bottom_pipe.xcor() + 30 and 
        bird.ycor() - 20 < bottom_pipe.ycor() + 150):
        run = False

    # Scoring
    score += 1
    print(score)

    # Boundary check
    if bird.ycor() > 300 or bird.ycor() < -300:
        run = False

    screen.update()
    time.sleep(0.01)