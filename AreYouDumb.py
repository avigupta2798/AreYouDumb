from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry('300x300')

# Creating a Button
Label(root, 
		 text="Are You Dumb?",
         padx=75,
         pady=75,
		 font = "Helvetica 20 bold").pack()

btn = Button(root, text = 'No')
btn.pack()

 
# Defining method on click
def Clickedbtn(event):
    x = random.randint(50,250)
    y = random.randint(50,200)
    btn.place(x=x, y=y)

def onClick():
    MsgBox = messagebox.showinfo("You are Dumb!","Ha, I knew it!!")
    if MsgBox == 'ok':
       root.destroy()

# bind button
btn.bind("<Button-1>" ,Clickedbtn)
btn.pack()

btn1 = Button(root, text = 'Yes', command=onClick)
btn1.pack()

root.mainloop()