from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")

with open("high_score.txt", mode = "r") as file:
	contents = int(file.read())


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.high_score = contents
		self.color("white") 
		self.penup()
		self.goto(0, 270)
		self.hideturtle()
		self.scoreboard_update()


	def scoreboard_update(self):
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGNMENT, font= FONT)

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score 
		self.score = 0
		self.scoreboard_update()


	def game_over(self):
		self.goto(0, 0) 
		self.write(f'GAME OVER', align= ALIGNMENT, font= FONT)

		
	def increase_score(self):
		self.score += 1
		self.scoreboard_update()









