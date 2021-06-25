from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time= datetime.datetime.now()
        now= current_time.strftime("%H:%M:%S")
        date= current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if current_time == set_alarm_timer:
            print("Time to Wake Up")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer= f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock= Tk()
clock.title("Kuch Bhoole Toh Ni")
clock.geometry("400x300")
time_format= Label(clock,text="Enter in 24 hr. format!",fg="blue",bg="white", font=("Arial",15,"bold")).place(x=100,y=120)
addTime=Label(clock,text="Hour       Min      Sec   ", fg="white", bg="brown",font=60).place(x=250)
setYourAlarm=Label(clock,text= "Farmayiye, Kab Utha Du", fg="green", relief="solid",font=("helevetica",12,"bold")).place(x=0,y=29)

#variable that we use
hour,min,sec=StringVar(),StringVar(),StringVar()

#time requires to set our alarm
houTime=Entry(clock,textvariable=hour,bg="red",width=16).place(x=250,y=30)
minTime=Entry(clock,textvariable=min,bg="red",width=16).place(x=300,y=30)
secTime=Entry(clock,textvariable=sec,bg="red",width=16).place(x=350,y=30)

submit=Button(clock,text="Set Alarm", fg="orange",width=10,command=actual_time).place(x=150,y=80)
clock.mainloop()
