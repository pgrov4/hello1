print("Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.")

from tkinter import *
# import tkinter as tk
#
# master=tk.Tk()
# w=Label(master,text='My first label')
#
# button=tk.Button(master, text='exit',width=25,highlightbackground='#ccff00')
# button.grid(row=0)

# master.mainloop()

print("Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.")
import tkinter as tk
master=tk.Tk()
def playme():
    print("pressed button")

button=tk.Button(master, text='hello',width=25,highlightbackground='#ccff00',command=playme())
button.grid(row=0)
master.mainloop()
print("Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.")

import tkinter as Tk
from tkinter import *
import sys


root = Tk()

frame = Frame(root)
frame.pack()

text = StringVar()
text.set('old')
status = IntVar()


def change_label():
    if status.get() == 1:  # if clicked
        text.set('new')
    else:
        text.set('old')


button = Checkbutton(frame, text='Change Label', variable=status, fg='blue', command=change_label)
lb = Label(root, textvariable=text)
button.pack(side=RIGHT)
lb.pack()
redbutton = Checkbutton(frame, text='Exit', highlightbackground='red', fg='red', command=sys.exit)
redbutton.pack(side=RIGHT)

root.mainloop()

#4. Write a python program using tkinter interface to take input in GUI program and print it


import tkinter as tk
from tkinter import ttk

master = tk.Tk()
lbl = ttk.Label(master, text='enter the name').grid(row=0, column=0)


def click():
    print("Hi," + name.get())
    tk.Label(master, text=name.get()).grid(row=2, column=0)



name = tk.StringVar()
nameentered = ttk.Entry(master, textvariable=name).grid(row=1, column=0)

button = ttk.Button(master, text="submit", command=click).grid(row=1, column=1)
master.mainloop()
