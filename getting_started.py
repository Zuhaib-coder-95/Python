from tkinter import *
from datetime import date

window = Tk()
window.title("Getting started with Widgets")
window.geometry('400x300')

label = Label(text="Hey There!", fg="white", bg="#072f5f", height=1, width=300)

name_label = Label(text="Full name", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()

    global message 
    message = "Welcome to the application! \n Today's Date is: "
    greet = "Hello "+ name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)


btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')

label.pack()
name_label.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()