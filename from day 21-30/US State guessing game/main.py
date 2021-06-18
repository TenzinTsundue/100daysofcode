from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("US State Guessing Game")
screen.bgpic('blank_states_img.gif')

data = pd.read_csv('50_states.csv')

state_corrected = []
state_to_learn = []

while len(state_corrected) < 50:
	state_input = screen.textinput(f"{len(state_corrected)}/50 US State Guessing Game",
		                           "Type any name of state: ").title()
	if state_input == 'Exit':
		break

	if state_input in data['state'].unique():
		t = Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data.state == state_input]
		t.setpos((int(state_data.x), int(state_data.y)))
		t.write(state_input, align= "center", font= ("Arial", 8, "normal"))
		if state_input not in state_corrected:
			state_corrected.append(state_input)

screen.exitonclick()

# state to learn
all_states = data.state
for state in all_states:
	if state not in state_corrected:
	    state_to_learn.append(state) 

df = pd.DataFrame(state_to_learn, columns =['State'])
df.to_csv('list_to_learn.csv')