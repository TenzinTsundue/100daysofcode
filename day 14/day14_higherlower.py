#higher lower game
#instagram follower comparasion

import os
import random 
import ascii, game_data

def clear():
	_ = os.system('cls')

def compare(a, b):
	if game_data.data[a]['follower_count'] >= game_data.data[b]['follower_count']:
		return a
	else:
		return b

clear()
print(ascii.logo)   # show the ascii art on a clear screen

game = True
count = 0
a = random.randint(0,len(game_data.data))
while game == True:
	b = random.randint(0,len(game_data.data))
	print(f"Compare A : {game_data.data[a]['name']}, {game_data.data[a]['description']} from {game_data.data[a]['country']} \n {ascii.vs} \nagainst B : {game_data.data[b]['name']}, {game_data.data[b]['description']} from {game_data.data[b]['country']}")
	answer = input("who has more followers? 'A' or 'B': ")
	if answer == 'A' and compare(a,b) == a or answer == 'B' and compare(a,b) == b:
		clear()
		print(ascii.logo)
		# print("You WON")
		a = b
		count = count + 1
	else:
		clear()
		print(ascii.logo)
		print(f"Your score is {count}")
		game = False


