from tkinter import *

window = Tk()
window.title("Pounds to kilo Converter")
window.minsize(height=100, width=300)
window.config(pady=10, padx=10)

shown_number = 0


def calculate():
    number = float(user_input.get())
    new_number = round((number * 0.45359237), 2)
    calculated_number.config(text=f"{new_number}")


user_input = Entry(width=10)
user_number = user_input.get()
user_input.grid(column=1, row=0)

pounds_label = Label(text="pounds", font=("Arial", 10, "bold"))
pounds_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal_label.grid(column=0, row=1)

calculated_number = Label(text=f"{shown_number}", font=("Arial", 10, "bold"))
calculated_number.grid(column=1, row=1)

kg_label = Label(text="kg", font=("Arial", 10, "bold"))
kg_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



window.mainloop()
