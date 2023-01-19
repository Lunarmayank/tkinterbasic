from tkinter import *
from tkinter import font
root = Tk()
root.geometry("500x500")




show2 = lambda anything:root.configure(background="blue")
b1 = Button(root, text="click here", font=("Arial", 20),background="green")
b1.bind("<Enter>",lambda anything:root.configure(background="pink"))
b1.bind("<Leave>",show2)
b1.pack()
root.mainloop()


#lecture 17 abhi sir