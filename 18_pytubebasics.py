from tkinter import *
from pytube import YouTube
root =Tk() 
root.geometry("600x700")
root.title("YouTube Video Downloader by Pranjal Pagaria")
root.config(bg="red")
logo=PhotoImage(file="picture.png")
Label(root,text="Video Downloader",font=("Arial  30 bold"),bg="black",fg="white").pack(padx=5,pady=50)
root.iconphoto(False,logo)
strvar=StringVar()
Label(root,text="Please paste your link here : ",font=("Arial 25  bold")).place(x=70,y=110)
Entry_link=Entry(root,width=50,font=25,textvariable=strvar).place(x=37,y=200)


root.mainloop()

