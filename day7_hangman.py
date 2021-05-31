#Hangman game

from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')

import random

hangmanpic= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
 /|\  |
 / \  |
=========''']


#generate a random word
word_list = ["elephent", "baboon", "camel", "python", "dog", "cat", "tiger", "lion", "buffalo", "mouse", "hippo", "bird"]
selected_word = random.choice(word_list)
word_length = len(selected_word)

clear()

print(f"The word has {word_length} letters " + "_ "*word_length)

life = 7

list = []
for i in range(word_length):
    list.append("_")

while "_" in list:
    gussed_letter = input("Guess a letter: ").lower()
    list_stamp = list.copy()     
    new_list = list 
    for i in range(word_length):
        if gussed_letter == selected_word[i]:
            new_list[i] = gussed_letter

    if list_stamp == new_list:
        life-=1
        print(list_stamp)
        print(f"Now you have {life} life")
        if life == 0:
            clear()
            break
    else:
        print(new_list)
        list = new_list

    clear()

    print(" ".join(map(repr, list)))
    print(f"{life} life remainig")
    art_number = 7 - life
    print(f"{hangmanpic[art_number]}")
    

word = ""
for char in selected_word:
    word+=char


if "_" in list:
    print(" ".join(map(repr, list)))
    print(f"{life} life remainig")
    print(f"{hangmanpic[7]}")

    print("You run out of life, You lost")
    print(f"The word is {word}")
else:
    print(f"You Won, The word is {word}")