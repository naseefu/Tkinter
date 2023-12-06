from tkinter import *

a = Tk()
mymenu = Menu(a)
a.config(menu=mymenu)

s1 = Menu(mymenu)
s2 = Menu(mymenu)
s3 = Menu(mymenu)
s4 = Menu(mymenu)
s5 = Menu(mymenu)


def pro():
    print("project created")
def new():
    print("new file created")
def scr():
    print("new scratch file created")
def ope():
    print("file opened")
def sav():
    print("Saved")
def rec():
    print("recents projects")


mymenu.add_cascade(label="File",menu=s1)
s1.add_command(label="New project",command=pro)
s1.add_command(label="New",command=new)
s1.add_separator()
s1.add_command(label="New Scratch file",command=scr)
s1.add_command(label="Open",command=ope)
s1.add_separator()
s1.add_command(label="Save AS",command=sav)
s1.add_command(label="Recent Projects",command=rec)
s1.add_separator()
s1.add_command(label="Quit",command=s1.quit)


def und():
    print("Undo the words")
def cu():
    print("words cut")
def cop():
    print("words copied")
def past():
    print("file pasted")
def dele():
    print("file deleted")
def fin():
    print("file found")


mymenu.add_cascade(label="Edit",menu=s2)
s2.add_command(label="Undo Typing",command=und)
s2.add_command(label="Cut",command=cu)
s2.add_separator()
s2.add_command(label="Copy",command=cop)
s2.add_command(label="Paste",command=past)
s2.add_separator()
s2.add_command(label="Delete",command=dele)
s2.add_command(label="Find",command=fin)



def too():
    print("tool windows")
def app():
    print("appearence")
def qui():
    print("quick definiton")
def par():
    print("Info of parameters")
def ty():
    print("Type info")
def con():
    print("context info")

mymenu.add_cascade(label="View",menu=s3)
s3.add_command(label="Tool Windows",command=too)
s3.add_command(label="Appearence",command=app)
s3.add_separator()
s3.add_command(label="Quick Definition",command=qui)
s3.add_command(label="Parameter info",command=par)
s3.add_separator()
s3.add_command(label="Type info",command=ty)
s3.add_command(label="Context info",command=con)



def bac():
    print("Go Back")
def cl():
    print("class")
def fii():
    print("Files")
def lin():
    print("Lines")
def urll():
    print("Url mapping")
def sele():
    print("Select in")



mymenu.add_cascade(label="Navigate",menu=s4)
s4.add_command(label="Back",command=bac)
s4.add_command(label="Class",command=cl)
s4.add_separator()
s4.add_command(label="File",command=fii)
s4.add_command(label="Line:Column",command=lin)
s4.add_separator()
s4.add_command(label="URL:Mapping",command=urll)
s4.add_command(label="Select In",command=sele)



def gen():
    print("generated")
def cd():
    print("Code completed")
def ins():
    print("code Inspected")
def clea():
    print("code cleanup")
def analy():
    print("code analyzed")
def fold():
    print("Folding")



mymenu.add_cascade(label="Code",menu=s5)
s5.add_command(label="Generate",command=gen)
s5.add_command(label="Code Complete",command=cd)
s5.add_separator()
s5.add_command(label="Inspect Code",command=ins)
s5.add_command(label="Code Cleanup",command=clea)
s5.add_separator()
s5.add_command(label="Analyze Code",command=analy)
s5.add_command(label="Folding",command=fold)



a.mainloop()