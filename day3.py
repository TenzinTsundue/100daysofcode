#love calulator, TRUE LOVE
#count lower
one = input("Enter the first person name : ")
name_one = one.lower()
two = input("Enter the second person name : ")
name_two = two.lower()

first_digit = 0
second_digit = 0

name_one_true_count = name_one.count('t') + name_one.count('r') + name_one.count('u') + name_one.count('e')
name_two_true_count = name_two.count('t') + name_two.count('r') + name_two.count('u') + name_two.count('e')
first_digit = name_one_true_count  + name_two_true_count

name_one_love_count = name_one.count('l') + name_one.count('o') + name_one.count('v') + name_one.count('e')
name_two_love_count = name_two.count('l') + name_two.count('o') + name_two.count('v') + name_two.count('e')
second_digit = name_one_love_count  + name_two_love_count

print(f"the score is {first_digit}{second_digit}")