# turtle drawing borad

from turtle import Turtle, Screen

tim = Turtle()

def forward():
	tim.forward(10)

def backward():
	tim.forward(-10)

def turn_right():
	tim.right(10)

def turn_left():
	tim.left(10)

def clean():
	tim.clear()
	tim.penup()
	tim.home()
	tim.pendown()

my_screen = Screen()
my_screen.onkeypress(forward, key = "w")
my_screen.onkeypress(backward, key = "s")
my_screen.onkeypress(turn_right, key = "d")
my_screen.onkeypress(turn_left, key = "a")
my_screen.onkeypress(clean, key = "c")

my_screen.listen()
my_screen.exitonclick()