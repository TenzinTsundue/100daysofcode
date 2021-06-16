import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title('turtle crossing')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car.move_speed)
    screen.update() 

    car.move()

    # checking collision
    for cars in car.car_list:
        if player.distance(cars) < 20:
            score.game_over()
            game_is_on = False

    # detect reacing the top
    if player.ycor() > 280:
        player.reset_position()
        score.player_score()
        car.cars_reset()
        # game_is_on = False

screen.exitonclick()


    