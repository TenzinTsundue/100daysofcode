# Turtle race and bet

from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width = 600 , height = 400)
bet_turtle = my_screen.textinput("Turtal race", "type the color you want to bet on: ")
# tim = Turtle(shape="turtle")

game_on = True
color = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
turtle = []
# speed_range = range(0,10)

for i in range(6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.penup()
	new_turtle.color(color[i])
	new_turtle.goto(-200, -150 + i * 40 + 40 )
	new_turtle.speed(2)
	turtle.append(new_turtle)

while game_on:
	for i in range(6):
		turtle[i].forward(random.randint(0, 10))
		if turtle[i].xcor() > 280:
			game_on = False
			winning_color = turtle[i].pencolor()
			if winning_color == bet_turtle:
				my_screen.title(f"You've won! The {winning_color} turtle is the winner!")
				# print()
			else:
				my_screen.title(f"You've lost! The {winning_color} turtle is the winner!")
				# print()
			break



my_screen.exitonclick()