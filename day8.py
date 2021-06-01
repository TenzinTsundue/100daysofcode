#simple function
"""
def greet():
	print("Hello ")
	print("How do you do?")
	print("Isn't the weather nice today")

greet(tenzin)
"""

#function that allows for input

"""
def greet_with_name(name):    #name is parameter
	print(f"Hello {name}")
	print(f"How do you do {name}?")

greet_with_name("Tenzin")     #Tenzin is argument
"""

#function with more then 1 input
"""
def greet_with(name, location):     #is a positional arguments
	print(f"Hello {name}")
	print(f"what is it like in {location}")

greet_with("Tenzin", "London")
"""

#keyword argument
"""
def my_funciton(a, b, c):
	#Do this wiht a, b and c

my_funciton(b= 12, a=3, c=11)    #keyword argument, where swith in position of aregument doesn't matter
"""

# code challanege for Area calc 
"""
import math

def my_function(test_h, test_w):
	can_required = math.ceil(test_h*test_w/5)
	print(f"you need {can_required} amount of paint")

test_h = int(input("Enter the height: "))
test_w = int(input("Enter the width: "))
coverage = 5

my_function(test_h, test_w)
"""

#prime number checker
"""
import math

def prime_checker(number):
	#number 1, 2, 3, 5, 7 are prime
	if number == 1 or number == 2 or number == 3 or number == 5 or number == 7:
	    print(f"{number} is a prime") 
	#perfect square not a prime
	elif math.sqrt(number).is_integer():
		print(f"{number} is not a prime")
	#divisible by 2, 3, 5, 7 not a prime
	elif number%2==0 or number%3==0 or number%5==0 or number%7==0:
	    print(f"{number} is not a prime") 
	#else prime
	else:
		print(f"{number} is a prime")

n = int(input("Enter number to check is a prime number: "))

prime_checker(number = n)
"""

# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#message = input("Type your message: ").lower()
#shift = int("Enter shift number")

def incode(message):
	for i in range(len(message)):
		item = message[i]
		if item not in alphabet:
			print(item, end="")
		else: 
			encoded_letter_position = alphabet.index(item) + shift
			if encoded_letter_position > 25:
				new_encoded_letter_position = encoded_letter_position%25 - 1
			else:
				new_encoded_letter_position = encoded_letter_position
			encode_letter = alphabet[new_encoded_letter_position]
			print(encode_letter, end="")

def decode(message):
	for i in range(len(message)):
		item = message[i] 
		if item not in alphabet:
			print(item, end="")
		else:
			encoded_letter_position = alphabet.index(item) - shift%25
			encode_letter = alphabet[encoded_letter_position]
			print(encode_letter, end="")

should_continue = True
while should_continue:
	direction = input("type 'incode' to incrypt and type 'decode' to decrypt: ")

	#encode
	if direction == 'incode':
		#input the message
		message = input("Type your message: ").lower()
		#type shift number
		shift = int(input("Enter shift number: "))
		#show encoded result
		print("The encoded message is ",end="")
		incode(message)

	elif direction == 'decode':
		#type your encoded message
		message = input("Type your incoded message: ").lower()
		#type your shift number
		shift = int(input("Enter shift number: "))
		#show the decoded message
		print("The decoded message is ",end="")
		decode(message)
	else:
		print("Wrong direction, rewrite direction")
		should_continue = False

	result = input("\nType 'yes' if you want to go again. Otherwise type 'no' : ")
	if result == 'yes':
		should_continue = True
	else:
		should_continue = False


