from tkinter import *
import tkinter.messagebox


def calculate():
    income = int(entry1.get())
    unit = v.get()
    if unit == 0:
        if 0 < income < 20000:
            answer_label['text'] = 'You don\'t have any tax to pay for ${} income.'.format(income)
        elif 20000 <= income < 50000:
            result = income * 20 / 100
            answer_label['text'] = 'You need to pay ${} tax for ${} income based on %20 deduction.'.format(result,
                                                                                                           income)
        elif 50000 <= income < 100000:
            result = income * 30 / 100
            answer_label['text'] = 'You need to pay ${} tax for ${} income based on %30 deduction.'.format(result,
                                                                                                           income)
        elif income >= 100000:
            result = income * 40 / 100
            answer_label['text'] = 'You need to pay ${} tax for ${} income based on %40 deduction.'.format(result,
                                                                                                           income)

    elif unit == 1:
        if 0 < income < 20000:
            answer_label['text'] = 'You don\'t have any tax to pay for ${} income.'.format(income)
        elif 20000 <= income < 50000:
            result = income * 10 / 100
            answer_label['text'] = 'You need to pay ${} tax for ${} income based on %10 deduction.'.format(result,
                                                                                                           income)
        elif 50000 <= income < 100000:
            result = income * 20 / 100
            answer_label['text'] = 'You need to pay ${} tax for ${} income based on %20 deduction.'.format(result,
                                                                                                           income)
        elif income >= 100000:
            result = income * 30 / 100
            answer_label['text'] = 'You need to pay ${} tax for ${} income based on %30 deduction.'.format(result,
                                                                                                           income)


def about():
    tkinter.messagebox.showinfo("About", "This is income tax calculator app\nMade by Njteh Keledjian")


root = Tk()
root.geometry("425x125")

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)

menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Exit", command=quit)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=about)

label1 = Label(root, text="Enter your annual income:")
entry1 = Entry(root)

label1.grid(row=0, column=0, padx=(75, 0))
entry1.grid(row=0, column=1, padx=(0, 75))

v = IntVar()
seniorCheck = Checkbutton(root, text="I'm Senior (64+)", variable=v)
seniorCheck.grid(row=1, column=0, padx=(100, 0))

calc_button = Button(text='Calculate', command=calculate)
calc_button.grid(row=2, column=0, columnspan=4)

answer_frame = LabelFrame(text='Result', height=100)
answer_frame.grid(row=10, column=0, columnspan=4, sticky='nesw')

answer_label = Label(answer_frame, text='')
answer_label.grid(row=0, column=0)

root.mainloop()
