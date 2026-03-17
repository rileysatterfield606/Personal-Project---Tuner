import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *


window = tk.Tk()
text = tk.Label(window, text="Hello World")
label = tk.Label(
    text= "poopie",
    foreground="white",
    background="black",
    width=20,
    height=10
    )
button = tk.Button(
    text= "pls click me",
    width= 20,
    height= 5,
    bg= "blue",
    fg= "white"
)
text.pack()
label.pack()
button.pack()
window.mainloop() # This is essential

