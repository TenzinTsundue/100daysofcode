# 100daysofcode
Here is the 100 days code challenge. #python #100daysofcode

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
- math.ceil(x): round up and its integer too
- math.comb(n, k)
- math.copysigh(x, y): return value of x but sign of y
- math.fabs(x): return absolute value of x
- math.factorial(x)
- math.floor(x): show integer value or round down
- math.fmod(x,y)
- math.frexp(x)
- math.fsum(iterable)
- math.gcd(*integers)
- math.isclose(a,b,*,rel_tol=1e-09,abs_tol=0.0)
- math.isfinite(x) : return True if x is neither an infinity nor a NaN
- math.isinf(x)
- math.isnan(x)
- math.isqrt(n)
- math.1cm(*integers)
- math.1dexp(x, i)
- math.modf(x)
- math.nextafter(x, y)
- math.perm(n, k=None)
- math.prod(iterable, *, start=1)
- math.remainder(x, y)
- math.trunc(x)
- math.ulp(x)
- math.exp(x): retuen e raised to the power of x
- math.expm1(x)
- math.log(x[,base]): return the natural logarithm of x to the base e
- math.log1p(x)
- math.lag2(x)
- math.log10(x)
- math.pow(x, y)
- math.sqrt(x): return the square root of x
- math.acos(x): return arc cosine of x in radians
- math.asin(x)
- math.atan(x)
- math.atan2(y, x)
- math.cos(x): return the cosine of x radians
- math.dist(p, q)
- math.pypot("coordinates)
- math.sin(x)
- math.tan(x)
- math.degrees(x): convert angle x from radians to degrees
- math.radians(x): convert angle x from degrees to radians
- math.acosh(x)
- math.cosh(x)
- math.erf(x): return error function at x
- math.erfc(x)
- math.gamma(x)
- math.lgamma(x)
#constants
- math.pi: 3.141592...
- math.e: 2.71828...
- math.tau: 6.283185...
- math.inf: floating point poistive infinity
- math.nan: floating point not a number(NaN) value

> 2 June 2021 | Day 9

Dictionaries and Nesting

project: Secret Auction (Highest bid will win, without knowing each other bidding)

key and value
{key : value}

>>> dict = {"a": "apple",
... "b": "ball",
... "c": "cat"}
>>> dict["c"]
'cat'
>>> dict["d"] = "dog"
>>> dict
{'a': 'apple', 'b': 'ball', 'c': 'cat', 'd': 'dog'}

```
import pprint 
pp = pprint.PrettyPrinter(indent=1)

student_score = {
	"Harry": 81,
	"Ron": 78,
	"Hermione": 99,
	"Draco": 74,
	"Neville": 62
}

student_grading = {}

for i in student_score:
	if student_score[i] > 90:
		student_grading[i]= "Outstanding"
	elif student_score[i] > 80:
		student_grading[i]= "Exceeds Expectation"
	elif student_score[i] > 70:
		student_grading[i]= "Acceptable"
	else:
		student_grading[i]= "Fail"

pp.pprint(student_grading)
```

Nesting a List in a Dictionary
```
travel_log = {
"France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visit: 7},
"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visit:2"}
}
```

Nesting a dict in a list
```
travel_log = [
{
 "country": "France",
 "cities_visited": ["Paris", "Lille", "Dijon"], 
 "total_visit": 7
},
{
 "country": "Germany",
 "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
 "total_visit": 2
}
]
```

```
travel_log = [
{
 "country": "France",
 "visits": 7,
 "cities": ["Paris", "Lille", "Dijon"]
},
{
 "country": "Germany",
 "visits": 2,
 "cities": ["Berlin", "Hamburg", "Stuttgart"]
}
]

def add_new_country(country, visits, cities):
	new_country = {}
	new_country["country"] = country
	new_country["visits"] = visits
	new_country["cities"] = cities
	travel_log.append(new_country)


add_new_country("Russia", 3, ["Moscow", "Saint Petersberg", "Sattrigas"])
print(travel_log)
```

> 6 june 2021 | Day 10 🥳

function with output
return

docstring: description for a function (documenting your function) 
```
def my_function():
    """Description on the my_function and 
    its also callded docstring"""
    #do this
```

print vs return

while loop, flag and recursion





