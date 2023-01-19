from tkinter import *
from tkinter import font
root = Tk()
root.geometry("500x500")


def show():
    print("pranjal pagaria")


b1 = Button(root, text="click here", font=("Arial", 20), command=show)
b1.pack()
root.mainloop()
