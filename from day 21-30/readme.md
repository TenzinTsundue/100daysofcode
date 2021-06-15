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


