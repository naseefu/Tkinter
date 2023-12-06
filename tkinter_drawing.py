from tkinter import *

a = Tk()

canvas = Canvas(a,width=100,height=200)
canvas.pack()
newline = canvas.create_line(0,0,8,90,fill="green")
newline1 = canvas.create_rectangle(0,0,90,90)
a.mainloop()