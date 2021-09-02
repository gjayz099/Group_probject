              #MEMBER
        #Dangcalan, Gerald Glen
        #Canada, Mark Paul
        #Lucenio, Rubyn Jane
        #Nalasa, Nikki
        #Sotalbo, Siara Vina
        #Aurigue, Shiela Marie S.

#IMPORT------------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from numpy import random
import time
import datetime
import os


#VIRABLE_0------------------------------------------------------------------------------------
subtop=""
def submit():
    if str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='11111':
        subtop="SET 1, SET 2, SET 3, SET 4, AND SET 5"
        TOTAL_Price=8480
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='11110':
        subtop="SET 1, SET 2, SET 3 AND SET 4"
        TOTAL_Price=6500
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='10111':
        subtop="SET 1, SET 3, SET 4 AND SET 5"
        TOTAL_Price=6560
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='11011':
        subtop="SET 1, SET 2, SET 4 AND SET 5"
        TOTAL_Price=6580
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='01111':
        subtop="SET 2, SET 3, SET 4, AND SET 5"
        TOTAL_Price=7280
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='11011':
        subtop="SET 1, SET 2, SET 3, AND SET 5"
        TOTAL_Price=7000
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='11100':
        subtop="SET 1, SET 2, AND SET 3"
        TOTAL_Price=5020
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='10110':
        subtop="SET 1, SET 3, AND SET 4"
        TOTAL_Price=4580
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='10011':
        subtop="SET 1, SET 4, AND SET 5"
        TOTAL_Price=4660
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='11001':
        subtop="SET 1, SET 2, AND SET 5"
        TOTAL_Price=5100
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='10101':
        subtop="SET 1, SET 3, AND SET 5"
        TOTAL_Price=5080
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='11010':
        subtop="SET 1, SET 2, AND SET 4"
        TOTAL_Price=4600
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='01110':
        subtop="SET 2, SET 3, AND SET 4"
        TOTAL_Price=5300
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='01011':
        subtop="SET 2, SET 4, AND SET 5"
        TOTAL_Price=5380
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='11000':
        subtop="SET 1, AND SET 2"   
        TOTAL_Price=3120
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='10100':
        subtop="SET 1, AND SET 3"
        TOTAL_Price=3100
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='10010':
        subtop="SET 1, AND SET 4"
        TOTAL_Price=2680
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='10001':
        subtop="SET 1, AND SET 5"
        TOTAL_Price=3180
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='01100':
        subtop="SET 2, AND SET 3"
        TOTAL_Price=3820
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='01010':
        subtop="SET 2, AND SET 4"
        TOTAL_Price=3400
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='01001':
        subtop="SET 2, AND SET 5"
        TOTAL_Price=3900
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='00110':
        subtop="SET 3, AND SET 4"
        TOTAL_Price=3380
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='00101':
        subtop="SET 3, AND SET 5"
        TOTAL_Price=3880
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='00011':
        subtop="SET 4, AND SET 5"
        TOTAL_Price=3460
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='00111':
        subtop="SET 3, SET 4, AND SET 5"
        TOTAL_Price=5360
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='10000':
        subtop="SET 1"
        TOTAL_Price=1200
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='01000':
        subtop="SET 2"
        TOTAL_Price=1920
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='00100':
        subtop="SET 3"
        TOTAL_Price=1900
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='00010':
        subtop="SET 4"
        TOTAL_Price=1480
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='00001':
        subtop="SET 5"
        TOTAL_Price=1980
    elif str(Set1.get())+str(Set2.get())+str(Set3.get())+str(Set4.get())+str(Set5.get()) =='00000':
        subtop="SORRY YOU HAVE NO ORDER\U0001F923"
        TOTAL_Price=0
#RES#------------------------------------------------------------------------------------
    res=messagebox.askquestion("YOUR ORDER","\nORDER FOR: "+entnme.get()+"\n__________________________\nYOUR PHONE NUMBER IS: "+entphn.get()+"\n__________________________\nYOUR EMAIL-ID IS: "+enteml.get()+"\n__________________________\nTHIS IS ORDERED: "+subtop+"\n__________________________\nTHIS IS YOUR TOTAL BILL:  \u20B1"+str(TOTAL_Price)+ "\n__________________________\nDATE AND TIME: "+str(datenow)+" | "+str(current_time)+"\n__________________________\nPAYMENT METHOD: "+MofPayment.get()+"\n__________________________\nORDER NUMBER: "+str(No_Order)+"\n__________________________\n(YES OR NO) TO CONFIRM YOU ORDER")
    if res=='yes':
        save_bill()
        message = messagebox.askokcancel("LUKE's KITCHEN", "THANK U USE PROGRAM")
        if message > 0:
            kit.destroy()
            return

#INSTALL A WINDOWS AND ICON--------------------------------------------------------------
kit=Tk()
kit.geometry("360x640+0+0")
kit.title("ONLINE ORDERING SYSTEM")
kit.iconbitmap("icon.ico")
kit.configure(background="pink")

#EXIT-----------------------------------------------------------------------------------
def Exit():
    qExit = messagebox.askyesno("MAC'S KITCHEN", "Do you what to exit the system")
    if qExit > 0:
        kit.destroy()
        return

#PICTURE-------------------------------------------------------------------------------
my_img = ImageTk.PhotoImage(Image.open("MACS.jpg"))
my_label = Label(image=my_img,bg="white",padx=10,pady=10)
my_label.grid(column=0,row=0)

#LABELS FRAME--------------------------------------------------------------------------
name=Label(kit,font=("arial",10,"bold"),text="LUKE's KITCHEN",bg="white",padx=10,pady=10)
f1=LabelFrame(kit,font=("arial",10,"bold"),text="CUSTOMER DETAILS", bg="white",bd=6,padx=20)
nme=Label(f1,font=("arial",10,"bold"),text="NAME:",relief=SUNKEN,width=15)
phn=Label(f1,font=("arial",10,"bold"),text="PHONE:",relief=SUNKEN,width=15)
eml=Label(f1,font=("arial",10,"bold"),text="EMAIL:",relief=SUNKEN,width=15)
mPayment=Label(f1,font=("arial",10,"bold"),text="Method of Payment",fg="black")
MofPayment=ttk.Combobox(f1,font=("arial",8,))
MofPayment["value"]=("CASH","GCASH","PAYPAL")

#Order No-------------------------------------------------------------------------------
No_Order=random.choice(10,size=(6))
#Virable_1-------------------------------------------------------------------------------
date=datetime.datetime.now()
datenow=date.strftime("%x")
entnme=Entry(f1,width=30)
entphn=Entry(f1,width=30)
enteml=Entry(f1,width=30)
Set1=IntVar()
Set2=IntVar()
Set3=IntVar()
Set4=IntVar()
Set5=IntVar()
#FRAME------------------------------------------------------------------------------------
f2=Label(kit,font=("arial",15,"bold"),bg="snow4",text="WHAT KIND OF ORDER?")
f3=Frame(kit,bg="lavender",bd=6)
f4=Frame(kit,bg="lavender",bd=6)
f5=Frame(kit,bg="lavender",bd=6)
#SET1 MENU---------------------------------------------------------------------------------
FSet1=Frame(f3,width=175,height=150,bg="white",bd=4,relief="raise")
FSet1.pack(side=LEFT)
Set1Btm=Checkbutton(FSet1,font=("arial",8,"bold"),text="SET-1: 6-8  pax \u20B1:1200",variable=Set1,bg="LightCyan3",bd=5,cursor="dotbox",relief=RAISED)
Set1Btm.grid(column=0,row=1)
Name1=Label(FSet1,text="2 pcs Steamend Potato",bg="white")
Name1.grid(column=0,row=2)
Name1=Label(FSet1,text="1 large Chicken Bam-e",bg="white")
Name1.grid(column=0,row=3)
Name1=Label(FSet1,text="Whole Chicken BBQ",bg="white")
Name1.grid(column=0,row=4)
Name1=Label(FSet1,text="30 pcs Lumpia Shanghai",bg="white")
Name1.grid(column=0,row=5)
#SET2 MENU----------------------------------------------------------------------------------
FSet2=Frame(f3,width=175,height=150,bg="white",bd=4,relief="raise")
FSet2.pack(side=RIGHT)
Set3Btm=Checkbutton(FSet2,font=("arial",8,"bold"),text="SET-2: 8-10 pax \u20B1:1920",variable=Set2,bg="LightCyan3",bd=5,cursor="dotbox",relief=RAISED)
Set3Btm.grid(column=0,row=1)
Name1=Label(FSet2,text="2 pcs Sweet & Sour Pompano",bg="white")
Name1.grid(column=0,row=2)
Name1=Label(FSet2,text="1 large Chicken Bam-e",bg="white")
Name1.grid(column=0,row=3)
Name1=Label(FSet2,text="2 pcs Tuna Panga",bg="white")
Name1.grid(column=0,row=4)
Name1=Label(FSet2,text="1 kl Hone Garlic Chicker",bg="white")
Name1.grid(column=0,row=5)
#SET3 MENU----------------------------------------------------------------------------------
FSet3=Frame(f4,width=175,height=150,bg="white",bd=4,relief="raise")
FSet3.pack(side=LEFT)
Set3Btm=Checkbutton(FSet3,font=("arial",8,"bold"),text="SET-3: 8-10 pax \u20B1:1900",variable=Set3,bg="LightCyan3",bd=5,cursor="dotbox",relief=RAISED)
Set3Btm.grid(column=0,row=1)
Name1=Label(FSet3,text="2 pcs Steamend Potato",bg="white")
Name1.grid(column=0,row=2)
Name1=Label(FSet3,text="1 large Chicken Bam-e",bg="white")
Name1.grid(column=0,row=3)
Name1=Label(FSet3,text="2 pcs Tuna/Malasugue Belly",bg="white")
Name1.grid(column=0,row=4)
Name1=Label(FSet3,text="1 kl Shrimp Gambas",bg="white")
Name1.grid(column=0,row=5)
#SET4 MENU-----------------------------------------------------------------------------------
FSet4=Frame(f4,width=175,height=150,bg="white",bd=4,relief="raise")
FSet4.pack(side=RIGHT)
Set4Btm=Checkbutton(FSet4,font=("arial",8,"bold"),text="SET-4: 8-10 pax \u20B1:1480",variable=Set4,bg="LightCyan3",bd=5,cursor="dotbox",relief=RAISED)
Set4Btm.grid(column=0,row=1)
Name1=Label(FSet4,text="1 Large Chicken Bam-e",bg="white")
Name1.grid(column=0,row=2)
Name2=Label(FSet4,text="30 pcs Lumpia Shanghai",bg="white")
Name2.grid(column=0,row=3)
Name3=Label(FSet4,text="1 kl Shrimp Gambas",bg="white")
Name3.grid(column=0,row=4)
Name4=Label(FSet4,text="1 kl Grilled Pork Belly",bg="white")
Name4.grid(column=0,row=5)
#SET5 MENU-----------------------------------------------------------------------------------
FSet5=Frame(f5,width=175,height=150,bg="white",bd=4,relief="raise")
FSet5.pack(side=LEFT)
Set3Btm=Checkbutton(FSet5,font=("arial",8,"bold"),text="SET-5: 8-10 pax \u20B1:1980",variable=Set5,bg="LightCyan3",bd=5,cursor="dotbox",relief=RAISED)
Set3Btm.grid(column=0,row=1)
Name1=Label(FSet5,text="2 pcs Sweet & Sour Pompano",bg="white")
Name1.grid(column=0,row=2)
Name1=Label(FSet5,text="2 pcs Tuna/Malasugue Belly",bg="white")
Name1.grid(column=0,row=3)
Name1=Label(FSet5,text="1 Whole Chicken BBQ",bg="white")
Name1.grid(column=0,row=4)
Name1=Label(FSet5,text="1 kl Grilled",bg="white")
Name1.grid(column=0,row=5)
#SET6 EXIT AND SUBMIT------------------------------------------------------------------------
FSet5=Frame(f5,width=175,height=150,bg="white",bd=4,relief="raise")
FSet5.pack(side=RIGHT)
current_time=time.strftime("%I:%M:%p")
time=Label(FSet5, text=current_time,font=("arial",10,"bold"),relief=SUNKEN,fg="black",bg="white")
time.grid(row=0,column=0)
btnSbt=Button(FSet5,text="SUBMIT",font=("arial",10,"bold"),bg="ivory3",width=8,command=submit)
btnSbt.grid(row=1,column=0)
btnExt=Button(FSet5,text="EXIT",font=("arial",10,"bold"),bg="red4",width=8,command=Exit)
btnExt.grid(row=2,column=0)
#NAME----------------------------------------------------------------------------------------
nme.grid(column=0,row=5)
entnme.grid(column=1,row=5)
#PHONE---------------------------------------------------------------------------------------
phn.grid(column=0,row=7)
entphn.grid(column=1,row=7)
#EMAIL---------------------------------------------------------------------------------------
eml.grid(column=0,row=9)
enteml.grid(column=1,row=9)
#PAYMENT------------------------------------------------------------------------------------
mPayment.grid(column=0,row=11)
MofPayment.grid(column=1,row=11)
#FRAME MENU----------------------------------------------------------------------------------
f1.grid(column=0,row=1)
f2.grid(column=0,row=2)
f3.grid(column=0,row=3)
f4.grid(column=0,row=4)
f4.grid(column=0,row=5)
f5.grid(column=0,row=6)
name.grid(column=0,row=7)

kit.mainloop()