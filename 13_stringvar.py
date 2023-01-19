from tkinter import *
root = Tk()
root.geometry("500x500")
root.resizable(0, 0)

x=StringVar()

def show():
    s=x.get()
    print(s)
    s=x.set("")

root.title()   
e1=Entry(root,font=("Arial",20),textvariable=x)
e1.pack()
b1=Button(root,text="Click here",command=show)
b1.pack()
root.mainloop()
