from tkinter import *

class myfun:
    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()
        self.pbutton = Button(frame,text="click",command=self.clickr)
        self.pbutton.pack()

        self.qbutton = Button(frame,text="quit",command=frame.quit)
        self.qbutton.pack(side=LEFT)

    def clickr(self):
        print("clicked")
root= Tk()
o1 = myfun(root)
root.mainloop()