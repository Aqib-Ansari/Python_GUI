from tkinter import *
from tkinter import font
from tkinter.ttk import *

from time import strftime

root =Tk()
root.title("digital clock")

def time():
    string1 = strftime('%H:%M:%S %p')
    Label.config(text=string1)
    Label.after(1000,time)

Label = Label(root, font=("Arial",80),foreground="black")
Label.pack(anchor='center')

time()

mainloop()