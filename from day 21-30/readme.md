> 14 June 2021 | day 21

Inheritance 

```python
class Fish(Animal):
	def __init__(self):
		super().__inti__()

```

```python
class Animal:

	def __init__(self):
		self.num_eye = 4

	def breath(self):
		print('Inhale, Exhale...')

class Fish(Animal):

	def __init__(self):
		super().__init__()			#all initilization of Animal class run under Fish class

	def breath(self):
		super().breath()			#breath meathod of Animal is added
		print('Under the water')	#behavior added on top of breath method form the Animal class

	def swim(self):				#Fish class own method
		print('Swimming')

```

**COMPLETED SNAKE GAME**<br>
<img src="https://user-images.githubusercontent.com/40035716/121854394-b92efd00-cd0f-11eb-838b-8e2592ba7dd1.PNG" width="250">

> 15 June 2021 | Day 22

Pong game <br>
<img src="https://user-images.githubusercontent.com/40035716/122014797-252b6700-cddd-11eb-92fb-d6213b894fa8.PNG" width="250">

> 16 June 2021 | Day 23

Turtle crossing game <br>
<img src="https://user-images.githubusercontent.com/40035716/122172645-954df180-ce9e-11eb-960d-172221ffd56e.PNG" width="250">

> 17 June 2021 | day 24

File

```python
file = open('file.txt')
contents = file.read()
print(contents)
file.close()
```
file read
```python
with open('file.txt') as file:
	contents = file.read()
	print(contents)
```
file write
```python
with open('day24.txt', mode="w") as file:   # w for write mode
	file.write("New text")
```
file append
```python
with open('day24.txt', mode="a") as file:   # a for append mode
	file.write("\nNew line")
```

directory 
```python
with open('./Input/Names/invited_names.txt') as file:
    name = file.read()
    name_list = name.split("\n")

for name in name_list:
    with open(f'./Output/ReadyToSend/{name}.txt', mode='w') as file:
        file.write(f'Dear {name},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nTenzin')
```

> 18 June 2021 | Day 25

```pyhton
with open('weather_data.csv') as file:
    data = file.readlines()
    print(data)
```

```python
import csv

with open('weather_data.csv') as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        if row[1] != 'temp':
	    temperature.append(row[1])
     print(temperature)
```

```python
import pandas as pd 

data = pd.read_csv('weather_data.csv')

print(data[data.temp == data.temp.max()])
```

```python
import pandas as pd

data = pd.read_csv('Central_Park_Squirrel_Data.csv')

unique_breed = data['Primary Fur Color'].unique()
unique_breed = unique_breed[1:]

gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

unique_count = [gray_count, cinnamon_count, black_count]

df = pd.DataFrame(list(zip(unique_breed, unique_count)), columns = ['Color', 'Count'])

print(df)
```
Created the US guess state learning game <br>
<img src="https://user-images.githubusercontent.com/40035716/122550510-60ce6700-d051-11eb-8751-de486fbc211f.PNG" width="400">

The code is at this [link](https://github.com/TenzinTsundue/100daysofcode/tree/main/from%20day%2021-30/US%20State%20guessing%20game)

>  19 June 2021 | Day 26

List and dictionary comprehension

Goal: Nato phonetic alphabet

```
numbers = [1, 2, 3]

# new_list = []
# for n in numbers:
# 	add_1 = n + 1
# 	new_list.append(add_1)

new_list = [n + 1 for n in numbers]  # list comprehension syntex
```

```
name = "tenzin"
new_lsit = [ letter for letter in name]   # we can also do string comprehension
```

```
range_list = [item * 2 for item in range(1, 5)]  # we can loop through range too
```

conditional list comprehension
```
new_list = [new_item for item in lsit if test]   # list comprehension with condition 

# example
names = ['Alex', 'Beth', 'Ten', 'Tensang', 'Macqueen', 'Freddie', 'Dave']

short_names = [name for name in names if len(name) < 5]
```


