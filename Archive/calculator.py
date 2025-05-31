import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title('Simple Calculator')
window.geometry("190x235")
window.config(background='black')

input_field = tk.Entry(borderwidth=5, width=18)
input_field.grid(row=0, column=0, columnspan=3)

def click_num(n):
    curr = input_field.get()
    input_field.delete(0, tk.END)
    new_val = curr + str(n)
    input_field.insert(0, new_val)

def clear():
    input_field.delete(0, tk.END)

length = 10
hight = 10

buttons = list(range(10))
for i in range(10):
    num = 9 - i
    row = (i // 3) + 1
    column = i % 3

    button = tk.Button(window, 
                       text=f'{num}', 
                       padx=length, 
                       pady=hight, 
                       command=lambda n=num: click_num(n),
                       font="Helvetica 16 bold")
    
    button.grid(row=row, column=column)
    buttons[-num] = button

clear_button = tk.Button(window,
                         text='c',
                         padx=length,
                         pady=hight,
                         command=clear,
                         font="Helvetica 16 bold")

clear_button.grid(row=4, column=1)

tk.mainloop()