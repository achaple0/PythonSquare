from turtle import Turtle, Screen

DELTA = 3
MINIMUM = DELTA * 2
CURSOR_SIZE = 20

num_squares = 100

screen = Screen()
turtle = Turtle("square", visible=False)
turtle.fillcolor("white")

for size in range(((num_squares - 1) * DELTA) + MINIMUM, MINIMUM - 1, -DELTA):
    turtle.goto(turtle.xcor() + DELTA/2, turtle.ycor() - DELTA/2)
    turtle.shapesize(size / CURSOR_SIZE)
    turtle.stamp()

screen.exitonclick()

