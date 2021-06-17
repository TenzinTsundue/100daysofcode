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
