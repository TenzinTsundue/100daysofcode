from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')

# clear()

ascii_art='''
___.   .__    .___ ___.   .__    .___                               
\_ |__ |__| __| _/ \_ |__ |__| __| _/    _________    _____   ____  
 | __ \|  |/ __ |   | __ \|  |/ __ |    / ___\__  \  /     \_/ __ \ 
 | \_\ \  / /_/ |   | \_\ \  / /_/ |   / /_/  > __ \|  Y Y  \  ___/ 
 |___  /__\____ |   |___  /__\____ |   \___  (____  /__|_|  /\___  >
     \/        \/       \/        \/  /_____/     \/      \/     \/
'''

list= []
def entry():
    dict = {}
    name = input("what is your name: ")
    bid = int(input("what's your bid: "))
    dict["name"] = name
    dict["bid"] = bid
    list.append(dict)

def winner():
    tester = 0
    for i in range(0, len(list)):
        if int(list[i]["bid"]) > tester:
            tester = i
        else:
            i = i
    print(f"The winner is {list[tester]['name']} with bid amout ${list[tester]['bid']}")

answer = True
clear()
print(ascii_art)
while answer == True:
    condition = input("Do you or other want to bid 'yes' or 'no': ").lower()
    if condition == "yes":
        clear()
        entry()
    elif condition == "no":
        clear()
        winner()
        answer = False

