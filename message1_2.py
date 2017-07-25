#!/usr/bin/python3.4

from tkinter import *

from tkinter import messagebox

top = Tk()
def Hello():
	messagebox.showinfo("Say Hello", "Hello World")

	
top.geometry("400x400")


B1= Button(top, text = "Say Hello", command = "hello")
B1.place(x = 50,y = 50)

top.mainloop() 