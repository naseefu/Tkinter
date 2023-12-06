from tkinter import *

a = Tk()

class student:
    def __init__(self,root):
        frame = Frame(root)
        frame.pack()
        self.p1 = Button(frame,text="click here!",command=self.clicked)
        self.p1.pack()
        self.p2 = Button(frame,text="Click to cancel",command=self.cancelled)
        self.p2.pack()
        self.p3 = Button(frame,text="Click to exit",command = frame.quit)
        self.p3.pack()

    def clicked(self):
        print("Clicked")
    def cancelled(self):
        print("cancelled")
b = student(a)
a.mainloop()