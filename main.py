# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("時計")

def gettime():
    time_string = strftime("%H時%M分%S秒")
    label.config(text=time_string)
    label.after(1000, gettime)

label = Label(root, font=("Arial Black", 80), background="white", foreground="lightgreen")
label.pack(fill="both",expand=1)

gettime()

mainloop()