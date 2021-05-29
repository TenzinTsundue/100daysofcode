#Password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter_length = int(input("How many letters would you like in your password? "))
symbol_length = int(input("How many symbols would you like? "))
number_length = int(input("How many number would you like? "))

word = []

for i in range(symbol_length):
    word.append(random.choice(symbols))

for i in range(number_length):
    word.append(random.choice(numbers))

for i in range(letter_length - symbol_length - number_length):
    word.append(random.choice(letters))

random.shuffle(word)

a = ""
print(f"Here is your password {a.join(word)}")

password = ""
for char in word:
    password += char
print(password)