from tkinter import *
root =Tk()
root.geometry("400x400")
root.resizable(0,0)
# root is window's object
# width mein ek samay pe kitne character show hone wale hai uski jahag lega
un=Entry(root,font=("Arial",16),fg="white",width=10,bg="black")
un.pack()
root.mainloop()

