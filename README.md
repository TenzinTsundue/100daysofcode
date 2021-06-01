# 100daysofcode
Here is the 100 day code challenge. #python #100daysofcode

> 24 May 2021

Just started with the plan to start 100 days coding challange <br>
*Language* : *Python*

> 25 May 2021 | Day 1

/ is used for escape character in python<br>
\` -> Single quote<br>
\\ -> Backslash<br>
\n -> New line<br>
\r -> Carriage return<br>
\t -> Tab<br>
\b -> Backspace<br>
\f -> Form feed<br>
\ooo -> Octal value<br>
\xhh -> Hex value<br>

String concatenation using +<br><br>
Indentation : Spaces at the beginning of a code. use 4-space indents and no hard tab characters<br>

Errors types in Python
- AssertionError
- AttributeError
- EOFError
- FloatinPointError
- GeneratorExit
- ImportError
- IndexError
- KeyError
- KeyboardInterrupt
- MemoryError
- NameError
- NotImplementedError
- OSError
- OverflowError
- ReferenceError
- RuntimeError
- StopIteration
- SyntaxError
- IndentaionError
- TabError
- SystemError
- SystemExit
- TypeError
- UnboundLocalError
- UnicodeError
- UnicodeEncodeError
- UnicodeDecodeError
- UnicodeTranslateError
- ValueError
- ZeroDivisionError

thonny app for debugging step by step
```
print("hello" + input("What is your name" ))
```
- comment best practice #comment (shortcut)
```
#singel line comment

"""
Multiple line
comments
looks like this
"""
```
```
print(len(input("what is your name: ")))
```

swap place shortcut<br>
a,b=b,a

> 26 May 2021 | Day 2

Python keywords list<br>
False await else import pass None break except in raise <br>
True class finally is return and continue for lambda try <br>
as def from nonlocal while asset del global not with async <br>
elif if or yield<br>

Data types<br>
integers | float | complex number | string | boolean <br>
```
#string
subsript: bracket notation
a="apple"
a[1]
'p'
#integer
123_456 is same as 123456
#float
3124.25
#boolean
True and False
#complex number
2+4j
```

Can't concatenate str with int<br>
so need type casting<br>
a=12<br>
str(a) #now a is a string <br>
ascii() bin() bool() chr() complex() float() hex() int() oct() ord() repr() str() type()<br>

Mathematical operation<br>
() > ** > *=/ > -=+<br>

functions in python<br>
len<br>
round(1.223, 2)<br>
```
type(4/2)
<class 'float'>
type(4//2)  #integer division operator
<class 'int'>

a=12
a+=2
>>a
14

#f string
name = "tenzin"
print(f"your name is {name}")

format function
"{:.2f}".format(123.3434)
123.34
```
> 26 May 2021 | Day 3
```
Condition 
if condition:
    do this
elif condition:
    do this
else:
    do this

Relational Operators
> < >= <= == !=

logical Operators
and
or 
not
```
> 27 May 2021 | Day 4

Random Module<br>
today final project: Rock paper scissors<br>
```
import random
rand_int = random.randint(1,10) #random int between 1 to 10 with 10 inclusive
rand_float = random.random()   #between 0-1 with 1 exclusive
```
```
#my_module.py
pi = 3.14
#main.py
import my_module.py
circle = pi * r * 2
```

list[] - data structure<br>
fruits = [item1, item2]<br>
list methods<br>
- index()
- append()
- extend()
- insert()
- remove()
- count()
- pop()
- reverse()
- sort()
- copy()
- clear()
>len(fruits)<br><br>
>random.choice(fruits)<br>

Nested list<br><br>
Grocery = [[fruits],[vegetables]]<br>
<br>
**Unlike function, methods are called on an object. Becasue of method is called on an object, it can access the data with it
Unlike method which can alter the ocjects state, python function doesn't do this and normally operates on it.**
<br>
indexing nested list<br>
```
a = [[1,2],[3,4]]
a[1,0]
>3
```
Random methods<br>
- seed()
- getstate()
- setstate()
- getrandbits()
- randrange()
- randint()
- choice()
- choices()
- shuffle()
- sample()
- random()
- uniform()
- triangular()
- betavariate()
- expovariate()
- gammavariate()
- gauss()
- lognornvariate()
- normalvariate()
- vonmisesvariate()
- paretovariate()
- weibullvariate()

> 29 May 2021 | Day 5

today project: password generator
```
loops
for loop
for item in list_of_items:
    print(item)

range(10)
>>range(0,10)
range(1,11)  #1,2,...,10

range(1, 100, 2)
```

> 30 May 2021 | Day 6
```
function
def my_function():	#define function
    #Do this
    #then this
my_functin()		#calling function
 
Code blocks(indentation) 
four space

while loops #loop till condition is met
while condition:
    #do this
```
List of inbuilt python function
-
-
-

> 31 May 2021 | Day 7

create hangeman in python

> 1 June 2021 | Day 8

#Ceasar cipher 

Functions and input

def my_function():
    #do this
    #then do this

my_function()

#math module
