from tkinter import *
from typing import BinaryIO
root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
b1 = Button(root, text="click here", font=("Arial", 20))
x = 1


def show(anything_we_can_pass):
    global x
    x = x+1
    if(x % 2 == 0):
        root.configure(background="pink")
    else:
        root.configure(background="black")


b1.bind("<Motion>", show)

b1.pack()
root.mainloop()

# focus in focus out 
# https://www.youtube.com/watch?v=wmuQgw7xvWE&list=PLsTEvedQ53ULTIWjjpCfkBYavGjxQrc-p&index=28