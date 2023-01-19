from tkinter import *
from tkinter import font
root = Tk()
root.geometry("500x500")


def show():
    root.configure(background="red")

def show1():
    root.configure(background="blue")



b1 = Button(root, text=" RED", font=("Arial", 20), command=show)
#b1.confige(background="colour")
b1.pack()

b2 = Button(root, text="BLUE", font=("Arial", 20), command=show1)
#b1.confige(background="colour")
b2.pack()
root.mainloop()
#bind method  https://www.youtube.com/watch?v=1kKXjAcckTc&list=PLsTEvedQ53ULTIWjjpCfkBYavGjxQrc-p&index=14