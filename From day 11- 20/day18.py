import random
from turtle import Turtle, Screen
import turtle

tim = Turtle()

# tim.shape("turtle")
# tim.color("green")

"""
#make a square
for _ in range(4):
    tim.right(90)
    tim.forward(100)
"""

"""
# darw dotted line forward
for _ in range(20):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)
"""

"""
# draw a tri angel, then square till decagon.
color = ["deep sky blue", "medium aquamarine", "aquamarine", "silver", "spring green", "yellow", "coral",
         "dark salmon", "light pink", "orchid", "medium slate blue"]


def draw_shape(num_side):
    angle = 360/num_side
    for i in range(num_side):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(color))
    draw_shape(shape_side)

"""


# random walk

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

"""
direction = [0, 90, 180, 270]
tim.hideturtle()
tim.pensize(5)
tim.speed(10)


def random_mov():
    tim.setheading(random.choice(direction))
    tim.color(random_color())
    tim.forward(10)


while True:
    random_mov()
"""
"""
# spirograph
tim.speed(20)


def draw_spirograph(gap):
    for _ in range(360//gap):
        tim.color(random_color())
        tim.circle(80)
        tim.setheading(tim.heading()-gap)


draw_spirograph(5)
"""

tim.hideturtle()
tim.penup()
x = -200
y = -200
for _ in range(20):
    for _ in range(20):
        tim.setpos(x, y)
        tim.dot(10, random_color())
        x += 20
    y+=20
    x = -200

# million drawing spot painting
screen = Screen()
screen.setup(500, 500)
screen.exitonclick()
