#Blackjack
#Simple Blackjack project where Ace act as only 1 and 
#while cards are withdrawn, it is not removed from the deck


import random

from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')

ascii_art = '''
 __        __                      __                 _____                      __       
/  |      /  |                    /  |               /     |                    /  |      
$$ |____  $$ |  ______    _______ $$ |   __          $$$$$ |  ______    _______ $$ |   __ 
$$      \ $$ | /      \  /       |$$ |  /  |            $$ | /      \  /       |$$ |  /  |
$$$$$$$  |$$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/        __   $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/ 
$$ |  $$ |$$ | /    $$ |$$ |      $$   $$<        /  |  $$ | /    $$ |$$ |      $$   $$<  
$$ |__$$ |$$ |/$$$$$$$ |$$ \_____ $$$$$$  \       $$ \__$$ |/$$$$$$$ |$$ \_____ $$$$$$  \ 
$$    $$/ $$ |$$    $$ |$$       |$$ | $$  |      $$    $$/ $$    $$ |$$       |$$ | $$  |
$$$$$$$/  $$/  $$$$$$$/  $$$$$$$/ $$/   $$/        $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/                                                                                           
'''

card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# deal the card form card list
def deal(list):
	list.append(random.choice(card))

#sum the total card in the list
def card_total(list):
	total = 0
	for i in range(0, len(list)):
		item = list[i]
		item = item + total
		total = item
	return total

#check who is the winner
def winner_check(your_card, computer_card):
	your_total = card_total(your_card)
	computer_total = card_total(computer_card)
	if 21 - your_total < 21 - computer_total:
		print("You win")
	elif 21 - your_total > 21 - computer_total:
		print("Computer won")
	else:
		print("its a DRAW")

#promt, do you want to play game of blackjack? type 'y' or 'n': 
condition = input("Do you want to play game of blackjack? type 'y' or 'n': ")
your_card = []
computer_card =[]

if condition == 'y':
	clear()
	print(ascii_art)
	deal(your_card)
	deal(computer_card)
	deal(your_card)

	print(f"Your card: {your_card}")
	print(f"Computer card: {computer_card}")

	deal_again = True
	while deal_again == True:		#condition to check the player want to deal card again
		deal_condition = input("type 'y' to get another card, type 'y' to pass: n: ")
		if deal_condition == 'y':		#if player want to deal
			deal(your_card)
			print(f"Your card: {your_card}")
			print(f"Computer card: {computer_card}")
			if card_total(your_card) > 21:		#if total amount of player card is greater then 21, player lose
				print("You lost")
				deal_again = False
		elif deal_condition == 'n':		#if player want no deal
			deal(computer_card)
			print(f"computer card: {computer_card}")
			while card_total(computer_card) < 17:
				deal(computer_card)
				print(f"Computer card: {computer_card}")
			if card_total(computer_card) > 21:
				print("player wins")
				break
			winner_check(your_card, computer_card)
			deal_again = False
		else:
			deal_again = True

else:
	print("Come back when you want to play blackjack")
 



 


