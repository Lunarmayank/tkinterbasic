from tkinter import *
root = Tk()
root.geometry("200x200")
root.resizable(0, 0)

x = IntVar() # use double for decimal  to calculate in points
y = IntVar()
z = IntVar()
def show():
    a = x.get()
    b = y.get()
    c = a+b
    z.set(c)

e1 = Entry(root, font=("Arial", 20),width="5", textvariable=x)
e1.pack()
e2 = Entry(root, font=("Arial", 20),width="5", textvariable=y)
e2.pack()
b1 = Button(root, text="Click here", command=show)
b1.pack()
e3 = Entry(root, font=("Arial", 20),width="5", textvariable=z)
e3.pack()
root.mainloop()
