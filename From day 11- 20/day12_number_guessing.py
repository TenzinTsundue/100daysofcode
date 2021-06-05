import random

#welcome note
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. type 'easy' or 'hard: ")

if difficulty == 'easy':
	chance = 10
elif difficulty =='hard':
	chance = 5
else:
	print("incorrent input, rerun code")

#select number form 1 to 100 and put in varible number
number = random.randint(1,100) 


for i in range(chance):
	guess = int(input("Make a guess: "))
	if guess > number:
		print("too high")
	elif guess < number:
		print("too low")
	else:
		print(f"you won, the number is {number}")
		break

if guess != number:
	print(f"you lost, the number is {number}")