print("Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.")
print("Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.")
import tkinter as tk
from tkinter import *
def onselect(event):
    w=event.widget
    print(w)
    #label(root,dict[event])
    idx=int(w.curselection()[0])
    value=w.get(idx)
    print(idx)
    print(dict[value])

def return_e1(en):
    content = e1.get()
    mylist.insert(END,content)
    print(content)

root=tk.Tk()
scrollbar=Scrollbar(root)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
#l1=['priyanka','poonam','shweta','vaishali']
dict = {'priyanka': 9899695557, 'poonam': 9811769810, 'shweta': '1234567890','vaishali':9876543210}
mylist = Listbox(root,name='mylist', yscrollcommand = scrollbar.set )


for key in dict:
   mylist.insert(END, key)
e1 = Entry(root)
e1.bind('<Return>',return_e1)
e1.pack()



mylist.bind('<<ListboxSelect>>',onselect)
mylist.pack( side = RIGHT, fill = BOTH )
scrollbar.config( command = mylist.yview )



mainloop()

