## Day 11 -20

> 4 June 2021 | day 11

Started with a small capston projet(Black jack)<br>
You can check the code here named **day11_blackjack.py**<br>
The code itself is pretty simple, since i modified many rules like Ace is just 1 instead of not 1 and 11 at the smae time and even full deck will reamain same after dealing.<br>
I will come back to this project with with all rule intact later and I am even thinking about creating GUI for Black jack later, using tkinter or pygame. We will see and i will always keep this updated.<br>

> 6 June 2021 | Day 12

Namespace: Local and Global scope

Local scope: within a funciton
```
player_health = 10    #global variable

def drink_potion():
    global life_count     #explicit declare global varible life_count
    life_count = 3      #global cariable																			
    potion_strength = 2      #local variable
    print(player_health)     #will print 10

drink_potion()
print(potion_stringth)  #will show error
print(life_count)	#will print 3
```

python constants and global scope: declare global varible in uppercase as a sign for not to modify it.
```
PI = 3.14159
URL = "https://www.codewithtenzin.com"
INSTAGRAM_HANDLE = "@tentsun12"
``` 

> 6 June 2021 | Day 13 

Debugging couple of codes, took less then half and hour

> 7 June 2021 | Day 14

Just made a simple python version of higher and lower game (instagram follower)

> 8 June 2021 | Day 15

Create a virtual coffee machine where you put which coffee you want and add coin, check the resources and give you coffee if all criteria are met.a

