
from tkinter import *
from random import randint as rnd
from tkinter import messagebox

window = Tk()

window.geometry("400x550")
value=""
value2=""
result=""
com=0
action=""
def B2(b):
    global value
    global value2
    global fild
    if com!=0:
        if b=="-":
            if value2=="":
                value2="-"
        else:
            value2+=str(b)
    else:
        if b=="-":
            if value=="":
                value="-"
        else:
            value+=str(b)
    
    fild["text"]=str(value)+""+action+""+str(value2)
    print(value, value2)  
def B3():
    global value
    global value2
    if com==0:
        value= value[0:len(value)-1]
    else:
        value2= value2[0:len(value2)-1]

    fild["text"]=str(value)+""+action+""+str(value2)
def B4(e):
    global com
    global action
    if value!="":
        com=e
        if com==1:
            action="+"
        elif com==2:
            action="-"
        elif com==3:
            action="x"
        elif com==4:
            action=":"
        fild["text"]=str(value)+""+action+""+str(value2)
def B5():
    global com
    global value
    global action
    global result
    
    global value2
    if value!=""  and value2!="":
        
        if com==1:
            result=float(value)+float(value2)
        elif com==2:
            result=float(value)-float(value2)
        elif com==3:
            result=float(value)*float(value2)
        elif com==4:
            result=float(value)/float(value2)
        fild["text"]=result
        value=str(result)
        value2=""
        com=0
        action=""
def B6():
    global com
    global value
    global action
    global result
    global value2
    com=0
    value=""
    value2=""
    action=""
    result=""
    fild["text"]=""
def B7():
    global value
    if com==0:
        value=float(value)/100
        fild["text"]=str(value)+""+action+""+str(value2)
        

Q1=Button(window,text="1", command =lambda:B2(1))
Q2=Button(window,text="2", command =lambda:B2(2))
Q3=Button(window,text="3", command =lambda:B2(3))
Q4=Button(window,text="4", command =lambda:B2(4))
Q5=Button(window,text="5", command =lambda:B2(5))
Q6=Button(window,text="6", command =lambda:B2(6))
Q7=Button(window,text="7", command =lambda:B2(7))
Q8=Button(window,text="8", command =lambda:B2(8))
Q9=Button(window,text="9", command =lambda:B2(9))
Q0=Button(window,text="0", command =lambda:B2(0))
QComma=Button(window,text=",", command =lambda:B2("."))
QMin=Button(window,text="-/+", command =lambda:B2("-"))
QM=Button(window,text="⌫", command =B3)
QPl=Button(window,text="+", command =lambda:B4(1))
QMi=Button(window,text="-", command =lambda:B4(2))
QUm=Button(window,text="x", command =lambda:B4(3))
QDe=Button(window,text=":", command =lambda:B4(4))
QPro=Button(window,text="%", command =B7)
QAs=Button(window,text="Ac", command =B6)
QRe=Button(window,text="=", command =B5)
fild=Label(window,text="0")
tex=Label(window,text="Калькулятор")

tex.config(font=("Courier", 30))
fild.config(font=("Courier", 50))
QM.config(font=("Courier", 20))
QPl.config(font=("Courier", 20))
QMi.config(font=("Courier", 20))
QUm.config(font=("Courier", 20))
QDe.config(font=("Courier", 20))
QRe.config(font=("Courier", 20))
Q1.config(font=("Courier", 20))
Q2.config(font=("Courier", 20))
Q3.config(font=("Courier", 20))
Q4.config(font=("Courier", 20))
Q5.config(font=("Courier", 20))
Q6.config(font=("Courier", 20))
Q7.config(font=("Courier", 20))
Q8.config(font=("Courier", 20))
Q9.config(font=("Courier", 20))
Q0.config(font=("Courier", 20))
QComma.config(font=("Courier", 20))
QAs.config(font=("Courier", 20))
QPro.config(font=("Courier", 20))
QMin.config(font=("Courier", 20))


tex.place(x=0,y=0,width=400,height=50)
fild.place(x=0,y=50,width=400,height=150)
QM.place(x=100,y=175,width=100,height=75)
QPl.place(x=300,y=175,width=100,height=75)
QMi.place(x=300,y=250,width=100,height=75)
QUm.place(x=300,y=325,width=100,height=75)
QDe.place(x=300,y=400,width=100,height=75)
QRe.place(x=300,y=475,width=100,height=75)
Q1.place(x=0,y=250,width=100,height=75)
Q4.place(x=0,y=325,width=100,height=75)
Q7.place(x=0,y=400,width=100,height=75)
Q2.place(x=100,y=250,width=100,height=75)
Q5.place(x=100,y=325,width=100,height=75)
Q8.place(x=100,y=400,width=100,height=75)
Q3.place(x=200,y=250,width=100,height=75)
Q6.place(x=200,y=325,width=100,height=75)
Q9.place(x=200,y=400,width=100,height=75)
Q0.place(x=100,y=475,width=100,height=75)
QMin.place(x=0,y=475,width=100,height=75)
QComma.place(x=200,y=475,width=100,height=75)
QAs.place(x=0,y=175,width=100,height=75)
QPro.place(x=200,y=175,width=100,height=75)


window.mainloop()

