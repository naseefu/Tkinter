from tkinter import *

a = Tk()
def fun1():
    print("undo clicked")
mymenu = Menu(a)
a.config(menu=mymenu)
submenu = Menu(mymenu)


mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="save")
submenu.add_command(label="New")
submenu.add_command(label="save as")
submenu.add_command(label="New menu")
submenu.add_separator()
submenu.add_command(label="History")
submenu.add_command(label="settings")


newmenu = Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu)
newmenu.add_command(label = "Undo",command=fun1)

toolbar = Frame(a,bg="pink")
toolbar.pack(fill=X,side=TOP)
b1 = Button(toolbar,text="Login").pack(side=LEFT,padx=2,pady=2)
b2 = Button(toolbar,text="PASSWORD").pack(side=LEFT,padx=2,pady=2)
stat = Label(a,text = "this is me",bd=1,relief=SUNKEN,anchor=W).pack(side=BOTTOM,fill=X)



a.mainloop()