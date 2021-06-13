## Day 11 -20

> 4 June 2021 | day 11

Started with a small capston projet(Black jack)<br>
You can check the code here named **day11_blackjack.py**<br>
The code itself is pretty simple, since i modified many rules like Ace is just 1 instead of not 1 and 11 at the smae time and even full deck will reamain same after dealing.<br>
I will come back to this project with with all rule intact later and I am even thinking about creating GUI for Black jack later, using tkinter or pygame. We will see and i will always keep this updated.<br>

> 6 June 2021 | Day 12

Namespace: Local and Global scope

Local scope: within a funciton
```
player_health = 10    #global variable

def drink_potion():
    global life_count     #explicit declare global varible life_count
    life_count = 3      #global cariable																			
    potion_strength = 2      #local variable
    print(player_health)     #will print 10

drink_potion()
print(potion_stringth)  #will show error
print(life_count)	#will print 3
```

python constants and global scope: declare global varible in uppercase as a sign for not to modify it.
```
PI = 3.14159
URL = "https://www.codewithtenzin.com"
INSTAGRAM_HANDLE = "@tentsun12"
``` 

> 6 June 2021 | Day 13 

Debugging couple of codes, took less then half and hour

> 7 June 2021 | Day 14

Just made a simple python version of higher and lower game (instagram follower)

> 8 June 2021 | Day 15

Create a virtual coffee machine where you put which coffee you want and add coin, check the resources and give you coffee if all criteria are met.a

> 9 June 2021 | Day 16

#object oriented programming

#How to OOP
#class(blueprint) has attributes(data) and  methods(functionality)
#object is modeled from a class

```
class CarBlueprint():    # declearing class
	pass

car = CarBlueprint()  # creating object
```

#import turtle
#timmy = turtle.Turtle()
```
from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(200)

my_screen = Screen()
# print(my_screen.canvheight)
my_screen.exitonclick()
```
> 11 June 2021 | Day 17

```python
# quiz project using class and OOP

# Class is a blueprint to create objects

class User:			# class name is PascalCase
	def __init__(self, user_id, user_name): 	 # initialize or consturctor, special function 
	    self.user_id = user_id
	    self.user_name = user_name
	    self.follower = 0
	    self.following = 0

	def follow(self, user):
		user.follower += 1
		self.following += 1 

	def show(self):
		return f'user name: {self.user_name}, follower: {self.follower}, following: {self.following}'


user_1 = User(1, "tentsun12")
user_2 = User(2, "choedon7777")

user_1.follow(user_2)

print(user_1.show())
print(user_2.show())
```

> 12 June 2021 | day 19

Turtle package study
Create draw with turtle and turtle race game.

