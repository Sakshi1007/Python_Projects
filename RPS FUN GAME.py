from tkinter import *
import random
root=Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title("RPS FUN GAME")
root.config(bg='seashell3')
Label(root,text='Rock,Paper,Scissors',font='arial 20 bold',bg='seashell2').pack()
user_take=StringVar()
Label(root,text="Choose any one: Rock,Paper,Scissors",font="arial 15 bold",bg="seashell2").place(x=20,y=70)
Entry(root,font="arial 15 bold",textvariable=user_take, bg="antiquewhite2").place(x=90,y=130)
comp_pick=random.randint(1,3)
if comp_pick==1:
    comp_pick='Rock'
elif comp_pick==2:
    comp_pick='Paper'
else:
    comp_pick='Scissors'
Result=StringVar()

def play():
    user_pick=user_take.get()
    if user_pick == comp_pick:
        Result.set('Tie, You Both Selected the same')
    elif user_pick == 'Rock' and comp_pick =='Paper':
         Result.set("You Loose, Computer selected the Paper")
    elif user_pick == 'Rock' and comp_pick == 'Scissors':
         Result.get("YOu Won! Computer selected the Scissors")
    elif user_pick == 'Paper' and comp_pick == 'Rock':
         Result.set("You Won, Computer selected the Rock")
    elif user_pick == 'Paper' and comp_pick=='Scissors':
         Result.set("You loose, Computer selected the Scissors")
    elif user_pick == 'Scissors' and comp_pick == 'Rock':
         Result.set("You Loose!, Computer Picked the Rock")
    elif user_pick == 'Scissors' and comp_pick == 'Paper':
         Result.set("You Won, Computer selected the Paper")
    else:
         Result.get('Invalid Selection, Choose one of - Rock, Paper, Scissors')
def reset():
    Result.set("")
    user_take.set("")

def exit():
    root.destroy()

Entry(root,font= "arial 15 bold", textvariable= Result, bg= 'antiquewhite2', width=50,).place(x=25, y=250)
Button(root, font="arial 15 bold", text="Play",padx=5, bg="seashell4",command=play).place(x=150, y=190)
Button(root, font="arial 15 bold", text="RESET",padx=5, bg="seashell4",command=reset).place(x=70, y=310)
Button(root, font="arial 15 bold", text="EXIT",padx=5, bg="seashell4",command=exit).place(x=230, y=310)
              
root.mainloop()
