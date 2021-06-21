from tkinter import *

window = Tk()
window.title("mile to km converter")
window.minsize(width=250, height=50)
window.config(padx=5, pady=5)

lable_1 = Label(text="is equal to")
lable_1.grid(row="1", column="0")

lable_2 = Label(text="Miles")
lable_2.grid(row="0", column="2")

lable_3 = Label(text="0")
lable_3.grid(row="1", column="1")

lable_4 = Label(text="Km")
lable_4.grid(row="1", column="2")


def calculate():
	solution = round(float(entry.get()) * 1.689)
	lable_3.config(text= solution)


button = Button(text="Calculate", command=calculate)
button.grid(row="2", column="1")

entry = Entry(width=20)
entry.grid(row="0", column="1")

window.mainloop()
