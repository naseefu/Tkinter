from tkinter import *
a = Tk()
l1 = Label(a,text="Username")
l2 = Label(a,text="Mobile number")
l3 = Label(a,text="Email")
l4 = Label(a,text="Age")
l5 = Label(a,text = "Password")
l6 = Label(a,text = "Confirm Password")

entry1 = Entry(a)
entry2 = Entry(a)
entry3 = Entry(a)
entry4 = Entry(a)
entry5 = Entry(a)
entry6 = Entry(a)

l1.grid(row=0,column=0)
entry1.grid(row=0,column=1)

l2.grid(row=1,column=0)
entry2.grid(row=1,column=1)

l3.grid(row=2,column=0)
entry3.grid(row=2,column=1)

l4.grid(row=3,column=0)
entry4.grid(row=3,column=1)

l5.grid(row=4,column=0)
entry5.grid(row=4,column=1)

l6.grid(row=5,column=0)
entry6.grid(row=5,column=1)

b1 = Button(a,text="Login")
b2 = Button(a,text="Cancel")

b1.grid(row=6,column=0)
b2.grid(row=6,column=1)

a.mainloop()
