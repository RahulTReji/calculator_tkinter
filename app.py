from tkinter import *

root = Tk()
root.title("Rahul's Calculator")


def button_click(temp_num):
    cur_num = calc_bar.get()
    calc_bar.delete(0, END)
    calc_bar.insert(0, str(cur_num) + str(temp_num))


def clear():
    calc_bar.delete(0, END)


def add_button():
    first_number = calc_bar.get()
    global f_num
    f_num = int(first_number)
    global operation
    operation = 'add'
    calc_bar.delete(0, END)


def subtract_button():
    first_number = calc_bar.get()
    global f_num
    f_num = int(first_number)
    global operation
    operation = 'subtract'
    calc_bar.delete(0, END)


def multiply_button():
    first_number = calc_bar.get()
    global f_num
    f_num = int(first_number)
    global operation
    operation = 'multiply'
    calc_bar.delete(0, END)


def divide_button():
    first_number = calc_bar.get()
    global f_num
    f_num = int(first_number)
    global operation
    operation = 'divide'
    calc_bar.delete(0, END)


def equal_button():
    if operation == 'add':
        second_number = calc_bar.get()
        calc_bar.delete(0, END)
        calc_bar.insert(0, f_num + int(second_number))
    if operation == 'subtract':
        second_number = calc_bar.get()
        calc_bar.delete(0, END)
        calc_bar.insert(0, f_num - int(second_number))
    if operation == 'multiply':
        second_number = calc_bar.get()
        calc_bar.delete(0, END)
        calc_bar.insert(0, f_num * int(second_number))
    if operation == 'divide':
        second_number = calc_bar.get()
        calc_bar.delete(0, END)
        calc_bar.insert(0, f_num / int(second_number))


calc_bar = Entry(width=38)
button1 = Button(text=1, padx=25, pady=25, borderwidth=5, command=lambda: button_click(1))
button2 = Button(text=2, padx=25, pady=25, borderwidth=5, command=lambda: button_click(2))
button3 = Button(text=3, padx=25, pady=25, borderwidth=5, command=lambda: button_click(3))
button4 = Button(text=4, padx=25, pady=25, borderwidth=5, command=lambda: button_click(4))
button5 = Button(text=5, padx=25, pady=25, borderwidth=5, command=lambda: button_click(5))
button6 = Button(text=6, padx=25, pady=25, borderwidth=5, command=lambda: button_click(6))
button7 = Button(text=7, padx=25, pady=25, borderwidth=5, command=lambda: button_click(7))
button8 = Button(text=8, padx=25, pady=25, borderwidth=5, command=lambda: button_click(8))
button9 = Button(text=9, padx=25, pady=25, borderwidth=5, command=lambda: button_click(9))
button0 = Button(text=0, padx=25, pady=25, borderwidth=5, command=lambda: button_click(0))
plus = Button(text='+', padx=29, pady=25, fg='black', command=add_button)
equal = Button(text='=', padx=25, pady=25, fg='black', command=equal_button)
clear = Button(text='A/C', padx=25, pady=95, fg='black', command=clear)
divide = Button(text='/', padx=31, pady=25, command=divide_button)
multiply = Button(text='x', padx=29, pady=25, command=multiply_button)
subtract = Button(text='-', padx=30, pady=25, command=subtract_button)
exit_button = Button(text='Exit', command=root.quit, padx=58, pady=25, fg='red', bg='#f432a6')

# packing into the grid system happens here:

calc_bar.grid(row=0, column=0, columnspan=5)
button1.grid(row=3, column=0, )
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
equal.grid(row=4, column=1)
clear.grid(row=1, column=3, rowspan=3)
plus.grid(row=1, column=4)
divide.grid(row=4, column=4)
multiply.grid(row=3, column=4)
subtract.grid(row=2, column=4)
exit_button.grid(row=4, column=2, columnspan=2)
root.mainloop()
