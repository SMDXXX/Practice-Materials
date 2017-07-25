Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def Hello():
        messagebox.showinfo("Say Hello", "Hello World")

B1= Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()
