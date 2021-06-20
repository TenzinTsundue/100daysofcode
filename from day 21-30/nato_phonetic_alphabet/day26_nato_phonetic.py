# file name: nato_phonetic_alphabet.txt

import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}

input_word = input("type your name to convert: ").upper()
input_list = list(input_word)

new_dict = {item:alpha_dict[item] for item in input_list}

print(new_dict)