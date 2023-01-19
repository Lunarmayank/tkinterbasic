from tkinter import *
from typing import BinaryIO
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
b1=Button(root,text="click here",font=("Arial",20))
b1.bind("<Button>",lambda anything:root.configure(background="pink"))
b1.bind("<ButtonRelease>",lambda anything:root.configure(background="black"))
b1.pack()
root.mainloop()