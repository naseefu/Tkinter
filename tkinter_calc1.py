from tkinter import *
import ast
a = Tk()
a.title("Calculator")
display = Entry(a)
display.grid(row=1,columnspan=6,sticky=W+E)

#get user input and place in the textfield
i = 0
def get_variable(num):
    global i
    display.insert(i,num)
    i+=1
def clearall():
    display.delete(0,END)
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clearall()
        display.insert(0,new_string)
    else:
        clearall()
        display.insert(0,"Error")
def get_operations(opr):
    global i
    length = len(opr)
    display.insert(i,opr)
    i+=length
def calculate():
    entire_string = display.get()
    try:
        a = ast.expr(entire_string).compile()
        result = eval(a)
        clearall()
        display.insert(0,result)
    except:
        clearall()
        display.insert(0,"Error")

#adding button to the calculator


Button(a,text ="1",command=lambda :get_variable(1)).grid(row=2,column=0)
Button(a,text ="2",command=lambda :get_variable(2)).grid(row=2,column=1)
Button(a,text ="3",command=lambda :get_variable(3)).grid(row=2,column=2)
Button(a,text ="4",command=lambda :get_variable(4)).grid(row=3,column=0)
Button(a,text ="5",command=lambda :get_variable(5)).grid(row=3,column=1)
Button(a,text ="6",command=lambda :get_variable(6)).grid(row=3,column=2)
Button(a,text ="7",command=lambda :get_variable(7)).grid(row=4,column=0)
Button(a,text ="8",command=lambda :get_variable(8)).grid(row=4,column=1)
Button(a,text ="9",command=lambda :get_variable(9)).grid(row=4,column=2)
Button(a,text ="0",command=lambda :get_variable(0)).grid(row=5,column=0)
Button(a,text ="AC",command=lambda :clearall()).grid(row=5,column=1)
Button(a,text ="=",command=lambda :calculate()).grid(row=5,column=2)
Button(a,text ="+",command=lambda :get_operations('+')).grid(row=2,column=3)
Button(a,text ="-",command=lambda :get_operations('-')).grid(row=3,column=3)
Button(a,text ="*",command=lambda :get_operations('*')).grid(row=4,column=3)
Button(a,text ="/",command=lambda :get_operations('/')).grid(row=5,column=3)
Button(a,text ="pi",command=lambda :get_operations('*3.14')).grid(row=2,column=4)
Button(a,text ="%",command=lambda :get_operations('%')).grid(row=3,column=4)
Button(a,text ="(",command=lambda :get_operations('(')).grid(row=4,column=4)
Button(a,text =")",command=lambda :get_operations(')')).grid(row=5,column=4)
Button(a,text ="exp",command=lambda :get_operations('**')).grid(row=2,column=5)
Button(a,text ="x!").grid(row=3,column=5)
Button(a,text ="^2",command=lambda :get_operations('**2')).grid(row=4,column=5)
Button(a,text="Undo",command=lambda :undo()).grid(row=5,column=5)

a.mainloop()