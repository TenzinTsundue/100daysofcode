# Password manager
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# -------------------PASSWORD GENERATOR---------------------- #

def generate_password():
	password_entry.delete(0, END)

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	nr_letters = random.randint(8, 10)
	nr_symbols = random.randint(2, 4)
	nr_numbers = random.randint(2, 4)

	password_letters = [random.choice(letters) for item in range(nr_letters)]
	password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
	password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

	password_list = password_letters + password_symbols +password_numbers
	random.shuffle(password_list)

	password = "".join(password_list)
	pyperclip.copy(password)
	password_entry.insert(0, password)

# ----------------------SAVE PASSWORD------------------------ #
def add_password():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()

	if website == "" or email == "" or password == "":
		messagebox.showerror(title="Oops", message="Please don't leave any field empty")
	else:	
		is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save.")

		if is_ok:
			with open('data.txt', mode="a") as file:
				file.write(f"{website} | {email} | {password}\n")
				website_entry.delete(0, END)
				email_entry.delete(0, END)
				password_entry.delete(0, END)


# ------------------------UI SETUP--------------------------- #

window = Tk()
# window.minsize(width=400, height=500)
window.title("Password Manager")
window.config(padx=20, pady=60)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="password.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

title_label = Label(text="MyPass", font=("Courier", 30, "bold"), fg="#1338be")
title_label.grid(row=1, column=1)

website_label = Label(text="Website:")
website_label.grid(row=2, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=2, column=1, columnspan=2, sticky="WE")
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=3, column=1, columnspan=2, sticky="WE")
email_entry.insert(0, "tensun0@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=4, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=2)

add_button = Button(text="Add", command=add_password)
add_button.grid(row=5, column=1, columnspan=2, sticky="WE")



window.mainloop()