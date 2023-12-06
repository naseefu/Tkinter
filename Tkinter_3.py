from tkinter import *
a = Tk()

label1 = Label(a,text="Hai",fg="red",bg="blue")
label1.pack(fill=X)

label2 = Label(a,text = "Hello",fg="blue",bg="red")
label2.pack(side=LEFT,fill=Y)



a.mainloop()