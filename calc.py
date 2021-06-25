from tkinter import *
exp=""

def press(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)
def equalpress():
        try:
            global exp
            total=str(eval(exp))
            equation.set(total)
            exp=" "
        except:
            equation.set("error")
            exp=""

def clear():
    global exp
    exp=""
    equation.set("")

root=Tk()
root.geometry("500x400")
root.title("BLANKOlator")
root.configure(bg="olive")
heading=Label(root,text="IFast_Calc",font=('times new roman',15,'bold'),bg="white",fg="black")
heading.place(x=180,y=10)
footing=Label(root,text="GUI MODULE",font=('times new roman',15,'bold'),bg="white",fg="black")
footing.place(x=180,y=360)
equation=StringVar()
txt=Entry(root,state='readonly',font=('Kristen ITC Regular',25,'bold'),textvariable=equation)
txt.grid(row=6,column=3,pady=50,padx=70,sticky="w")
txt_frame=Frame(txt,bd=10,bg="crimson")
txt_frame.place(x=2,y=2,width=500)
seven=Button(text="7",width=10,height=2,command=lambda:press(7))
seven.place(x=80,y=110)
eight=Button(text="8",width=10,height=2,command=lambda:press(8))
eight.place(x=170,y=110)
nine=Button(text="9",width=10,height=2,command=lambda:press(9))
nine.place(x=260,y=110)
CE=Button(text="CE",width=10,height=2,command=clear)
CE.place(x=345,y=110)
four=Button(text="4",width=10,height=2,command=lambda:press(4))
four.place(x=80,y=160)
five=Button(text="5",width=10,height=2,command=lambda:press(5))
five.place(x=170,y=160)
six=Button(text="6",width=10,height=2,command=lambda:press(6))
six.place(x=260,y=160)
zero=Button(text="0",width=10,height=2,command=lambda:press(0))
zero.place(x=345,y=160)
add=Button(text="+",width=10,height=2,command=lambda:press('+'))
add.place(x=345,y=210)
one=Button(text="1",width=10,height=2,command=lambda:press(1))
one.place(x=80,y=210)
two=Button(text="2",width=10,height=2,command=lambda:press(2))
two.place(x=170,y=210)
three=Button(text="3",width=10,height=2,command=lambda:press(3))
three.place(x=260,y=210)
div=Button(text="/",width=10,height=2,command=lambda:press('/'))
div.place(x=80,y=260)
multiply=Button(text="*",width=10,height=2,command=lambda:press('*'))
multiply.place(x=170,y=260)
sub=Button(text="-",width=10,height=2,command=lambda:press('-'))
sub.place(x=260,y=260)
equal=Button(text="=",width=10,height=2,command=equalpress)
equal.place(x=345,y=260)

root.mainloop()
