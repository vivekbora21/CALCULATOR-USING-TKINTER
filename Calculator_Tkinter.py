from tkinter import *

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0, str(result) + str(num))

def div():
    n1 = e.get()
    global math
    math = 'division'
    global i
    i = int(n1)
    e.delete(0, END)

def mul():
    n1 = e.get()
    global math
    math ='multiplication'
    global i
    i = int(n1)
    e.delete(0, END)

def sub():
    n1 = e.get()
    global math
    math = 'subtraction'
    global i
    i = int(n1)
    e.delete(0, END)

def add():
    n1 = e.get()
    global math
    math = 'addition'
    global i
    i = int(n1)
    e.delete(0, END)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0,i + int(n2))
    elif math =='subtraction':
        e.insert(0,i - int(n2))
    elif math =='multiplication':
        e.insert(0,i * int(n2)) 
    elif math =='division':
        e.insert(0,i / int(n2))  

def clear():
    e.delete(0, END)

window = Tk()
window.title("CALCULATOR")
window.geometry('300x250')

e = Entry(window , width = 20, borderwidth = 5, justify="right", font="Arial 18")
e.place(x = 10, y = 0)

b = Button(window , text = '1', width = 8 , command = lambda:click(1))
b.place(x = 10 , y = 60)

b = Button(window , text = '2', width = 8 , command = lambda:click(2))
b.place(x = 80 , y = 60)

b = Button(window , text = '3', width = 8 , command = lambda:click(3))
b.place(x = 150 , y = 60)

b = Button(window , text = '/', width = 8 , command = div)
b.place(x = 220 , y = 60)

b = Button(window , text = '4', width = 8 , command = lambda:click(4))
b.place(x = 10 , y = 100)

b = Button(window , text = '5', width = 8 , command = lambda:click(5))
b.place(x = 80 , y = 100)

b = Button(window , text = '6', width = 8 , command = lambda:click(6))
b.place(x = 150 , y = 100)

b = Button(window , text = '*', width = 8 , command = mul)
b.place(x = 220 , y = 100)

b = Button(window , text = '7', width = 8 , command = lambda:click(7))
b.place(x = 10 , y = 140)

b = Button(window , text = '8', width = 8 , command = lambda:click(8))
b.place(x = 80 , y = 140)

b = Button(window , text = '9', width = 8 , command = lambda:click(9))
b.place(x = 150 , y = 140)

b = Button(window , text = '-', width = 8 , command = sub)
b.place(x = 220 , y = 140)

b = Button(window , text = '0', width = 8 , command = lambda:click(0))
b.place(x = 80 , y = 180)

b = Button(window , text = 'clear', width = 8 , command = clear)
b.place(x = 10 , y = 180)

b = Button(window , text = '+', width = 8 , command = add)
b.place(x = 150 , y = 180)

b = Button(window , text = '=', width = 8 , command = equal)
b.place(x = 220 , y = 180)

mainloop()