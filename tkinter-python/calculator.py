from tkinter import *

root = Tk()
root.title("Ethan's Calculator")
root.iconbitmap('images\calculator.ico')

e = Entry(root, borderwidth=5, width=41)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

	

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)



button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="#ff4d4d")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="#00ccff")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="#00cc00")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="#ff3399")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="#cc00ff")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="#996633")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="#ffff00")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="#fff")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="#4d4dff")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="#ff0000")
button_add = Button(root, text="+", padx=40, pady=20, command=button_add, bg='#00ffbf')
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal, bg='#00ffbf')
button_clear = Button(root, text="Clear", padx=125, pady=20, command=button_clear, bg='#ff8000')

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract, bg='#00ffbf')
button_multiply = Button(root, text="×", padx=40, pady=20, command=button_multiply, bg='#00ffbf')
button_divide = Button(root, text="÷", padx=40, pady=20, command=button_divide, bg='#00ffbf')

# Put the Buttons on the screen

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=1)
button_clear.grid(row=1, column=0, columnspan=3)
button_add.grid(row=4, column=3)
button_equal.grid(row=5, column=3)

button_subtract.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=3, column=3)


root.mainloop()