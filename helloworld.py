print ( 'hello world')
print ('***LOOP PRACTICE***')
# for intergers in range 
for i in range (2):
	print('A')
	print('B')

for i in range (2):
	print('A')
print('B')
print("                                                                                                                                                                                                                                                                                                            Too many single lines                                                                                                                                                                                                                                                             ")
name = "Bob"
age = 15
print (name)

print (age)
age += 1 
print (age)


"""
this will not execute
this is a simple python program that prints "hello world". That's all it does for now but soon it can do more

"""

print("fudgenutter")
print("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       MORE LOOPS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ")

numbers = [1, 2, 3]
for number in numbers: 
	print(number)

dog_name = "BINGO"

for char in dog_name:
	print (char)

for i in range(3):
	print(i)

print( "************************************************NAME PRACTICE*****************************************************")
# print how many characters or how many items in list: len(
name = "Jamie"
print (len(name))

names = ["Bob", "Jane", "James", "Alice"]
print (len(names))


# if statements
 
name = "Joe"

if len(name) > 3:
	print ( "Nice name")
	print (name)
else:
	print("That's a short name.")
#this adds all numbers 1+2+3+4... and displays the sum

n = 0

for i in range (1, 101):
	n+= i

print('The sum of the numbers 1 to 100 is ...')
print(n)




"""

Creating simple message box 


"""

from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def Hello():
	messagebox.showinfo("Say Hello", "Hello World")

B1= Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()
