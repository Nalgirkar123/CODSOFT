import tkinter as tk
from tkinter import *

myframe=tk.Tk()
myframe.geometry("210x270")
myframe.title('calculator')

input=Entry(myframe,width=22,borderwidth=3,relief=RIDGE)
input.grid(padx=15,pady=10,row=0,sticky="w")

def b9():
    input.insert("end","9")
def b8():
    input.insert("end","8")
def b7():
    input.insert("end","7")
def b6():
    input.insert("end","6")
def b5():
    input.insert("end","5")
def b4():
    input.insert("end","4")
def b3():
    input.insert("end","3")
def b2():
    input.insert("end","2")
def b1():
    input.insert("end","1")
def b0():
    input.insert("end","0")
def b00():
    input.insert("end","00") 
def bdot():
    input.insert("end",".")
def plus():
    input.insert("end","+")
def Minus():
    input.insert("end","-")
def mul():
    input.insert("end","*")
def div():
    input.insert("end","/")
def mod():
    input.insert("end","%")
def result():
    if input.get()=="":
        input.insert("end","error")
    elif input.get()[0]=="0":
        input.delete(0,"end")
        input.insert("end","error")
    else:
        res=input.get()
        res=str(eval(res))
        input.insert("end","=")
        input.insert("end",res)
        
def clear():
    input.delete(0,"end")

clear=Button(myframe,text='clr',width='4',fg='white',bg='purple',command=clear,relief=RIDGE)
clear.grid(row=0,padx=165,sticky="w")

b9=Button(myframe,text="9",width=4,height=2,borderwidth=3,command=b9,relief=RIDGE)
b9.grid(row=1,padx=15,sticky="w")

b8=Button(myframe,text="8",width=4,height=2,borderwidth=3,command=b8,relief=RIDGE)
b8.grid(row=1,padx=65,sticky="w")

b7=Button(myframe,text="7",width=4,height=2,borderwidth=3,command=b7,relief=RIDGE)
b7.grid(row=1,padx=115,sticky="w")

plus=Button(myframe,text="+",width=4,height=2,borderwidth=3,command=plus,relief=RIDGE)
plus.grid(row=1,padx=165,sticky="w")

b6=Button(myframe,text="6",width=4,height=2,borderwidth=3,command=b6,relief=RIDGE)
b6.grid(row=2,padx=15,sticky="w")

b5=Button(myframe,text="5",width=4,height=2,borderwidth=3,command=b5,relief=RIDGE)
b5.grid(row=2,padx=65,sticky="w")

b4=Button(myframe,text="4",width=4,height=2,borderwidth=3,command=b4,relief=RIDGE)
b4.grid(row=2,padx=115,sticky="w")

Minus=Button(myframe,text="-",width=4,height=2,borderwidth=3,command=Minus,relief=RIDGE)
Minus.grid(row=2,padx=165,sticky="w")

b3=Button(myframe,text="3",width=4,height=2,borderwidth=3,command=b3,relief=RIDGE)
b3.grid(row=3,padx=15,sticky="w")

b2=Button(myframe,text="2",width=4,height=2,borderwidth=3,command=b2,relief=RIDGE)
b2.grid(row=3,padx=65,sticky="w")

b1=Button(myframe,text="1",width=4,height=2,borderwidth=3,command=b1,relief=RIDGE)
b1.grid(row=3,padx=115,sticky="w")

multiply=Button(myframe,text="x",width=4,height=2,borderwidth=3,command=mul,relief=RIDGE)
multiply.grid(row=3,padx=165,sticky="w")

b0=Button(myframe,text="0",width=4,height=2,borderwidth=3,command=b0,relief=RIDGE)
b0.grid(row=4,padx=15,sticky="w")

b00=Button(myframe,text="00",width=4,height=2,borderwidth=3,command=b00,relief=RIDGE)
b00.grid(row=4,padx=65,sticky="w")

bdot=Button(myframe,text=".",width=4,height=2,borderwidth=3,command=bdot,relief=RIDGE)
bdot.grid(row=4,padx=115,sticky="w")

divide=Button(myframe,text="/",width=4,height=2,borderwidth=3,command=div,relief=RIDGE)
divide.grid(row=4,padx=165,sticky="w")

result=Button(myframe,text="=",width=15,fg='white',bg='purple',height=2,borderwidth=3,command=result,relief=RIDGE)
result.grid(row=6,padx=30,pady=7,sticky="w")

mod=Button(myframe,text="%",width=4,height=2,borderwidth=3,command=mod,relief=RIDGE)
mod.grid(row=6,padx=165,sticky="w")

myframe.mainloop()

