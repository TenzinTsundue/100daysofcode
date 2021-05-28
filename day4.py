print("rock paper scissors game")
print("0 for rock, 1 for paper ,2 pfr scissors")

import random

rock='''
 ---
| R |
| R  |
 ----
'''

paper='''
------
| P  |
| P  |
------
'''

scissor='''
 --    --
| S| /  /
 --
| S| \  \\
 --    --
'''
graphics = [rock, paper, scissor]
name = input("Enter your name: ")
your_selection = int(input("Choose your selection : "))
computer_selection = random.randint(0,2)

print(f"your selection is \n{graphics[your_selection]}\n")
print(f"Computer selection is\n{graphics[computer_selection]} ")

a = [0,1,2]
b = [0,1,2]
"""
2,0,c
0,2,p

0,1,c
1,2,c

1,0,p
2,1,p
"""
if your_selection == 2 and computer_selection == 0:
    print("Computer WIN")
elif your_selection == 0 and computer_selection == 2:
    print(f"Player {name} WIN")
elif your_selection < computer_selection:
    print("Computer WIN")
elif your_selection > computer_selection:
    print(f"Player {name} WIN")
else:
    print("DRAW")

#if your_selection == computer selection
#    print("DRAW")



 
