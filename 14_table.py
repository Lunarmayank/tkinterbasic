from tkinter import *
root = Tk()
root.geometry("200x200")
root.resizable(0, 0)
x = IntVar()


def show():
    a = x.get()
    for i in range(1, 11):
        print(f"{a}x{i}={a*i}")
         


e1 = Entry(root, font=("Arial", 20), width="5", textvariable=x)
e1.pack()
b1 = Button(root, text="Click here", command=show)
b1.pack()
root.mainloop()
