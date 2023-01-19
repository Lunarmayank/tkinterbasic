from tkinter import *
root = Tk()
root.geometry("500x500")
un = Label(root, text="Enter Name", font=("Arial", 20))
un.grid(row=0, column=0,pady=25)

e1 = Entry(root, font=("Arial", 20))
e1.grid(row=0, column=1,pady=25)


l2 = Label(root, text="Password", font=("Arial", 20))
l2.grid(row=1, column=0,pady=25,sticky=W)

#e2 = Entry(root, font=("Arial", 20))
#e2.grid(row=1, column=1,pady=25)
# to hide password
e2 = Entry(root,show="*" ,font=("Arial", 20))
e2.grid(row=1, column=1,pady=25)


b1=Button(root,text="login",font=("Arial",20))

b1.grid(row=2,column=0,columnspan=2)



root.mainloop()
