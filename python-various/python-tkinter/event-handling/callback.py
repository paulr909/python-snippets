#!/usr/bin/python3

from tkinter import *
from tkinter import ttk


def callback(number):
    print(number)


root = Tk()

ttk.Button(root, text="Click Me 1", command=lambda: callback(1)).pack()
ttk.Button(root, text="Click Me 2", command=lambda: callback(2)).pack()
ttk.Button(root, text="Click Me 3", command=lambda: callback(3)).pack()

root.mainloop()
