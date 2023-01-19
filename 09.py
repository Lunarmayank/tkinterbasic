from tkinter import *
from tkinter import font
root = Tk()
root.geometry("500x500")


root.bind("<Enter>",lambda anything:root.configure(background="pink"))
root.bind("<Leave>",lambda anything:root.configure(background="blue"))

root.mainloop()


#lecture 17 abhi sir