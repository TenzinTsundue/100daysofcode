from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.car_list = []
        self.manage_car()
        self.move_speed = 0.1


    def manage_car(self):
        for i in range(100):
            self.create_car()


    def create_car(self):
        new_car = Turtle() 
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(random.randrange(300,3000, 40), random.randrange(-230, 250, 30))
        new_car.color(random.choice(COLORS))
        self.car_list.append(new_car)


    def move(self):
        for i in range(len(self.car_list)):
            self.car_list[i].forward(MOVE_INCREMENT)

    def cars_reset(self):
        self.move_speed  *= 0.9
        for cars in self.car_list:
            cars.goto(random.randrange(300,3000, 20), random.randrange(-230, 250, 20))


