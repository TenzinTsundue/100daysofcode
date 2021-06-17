# snake game with python turtle module

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time
 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake
game_is_on = True 
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

	#detect collision with food
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		score.increase_score()

	#detecting collision with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		score.reset()
		snake.reset()
		# game_is_on = False
		# score.game_over()

	#detect collision with tail
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
			score.reset()
			snake.reset()
			# game_is_on = False
			# score.game_over()

	with open("high_score.txt", mode = "w") as file:
		file.write(f"{score.high_score}")


screen.exitonclick()
	



	