from tkinter import* 
from tkinter import messagebox

root = Tk()
root.geometry("270x270")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root, text="Scan For Virus", command=msg , width= 15, height=3)
button.place(x=80, y=160)

root.mainloop()