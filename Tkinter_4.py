from tkinter import *

a = Tk()

def fun():
    print("click here")
b1 = Button(a,text="OK!",command=fun)
b1.pack()

a.mainloop()