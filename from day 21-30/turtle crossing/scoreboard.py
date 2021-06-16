from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f"Score: {self.score}", align="center", font= FONT)

    def player_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align= "center", font= ("Courier", 25, "bold"))

