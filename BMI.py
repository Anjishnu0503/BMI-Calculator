import tkinter as tk
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

root=Tk()
root.title("BMI Calculator By Anjishnu Bhowal")
root.geometry("470x550+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

def BMI():
    h=float(Height.get())
    w=float(Weight.get())
    
    m=h/100
    bmi=round(float(w/m**2),1)
    label1.config(text=bmi)
    
    if bmi<=18.5:
        label2.config(text="Underweight!")
        label3.config(text="You need to pull up weight \n to get a normal body")
        
    elif bmi>18.5 and bmi<=25:
        label2.config(text="Great!")
        label3.config(text="You are in the best Shape!")
        
    elif bmi>25 and bmi<=30:
        label2.config(text="OverWeight!")
        label3.config(text="Don't Worry \n Spinach's tastier than chicken")
        
    else:
        label2.config(text="Obese!")
        label3.config(text="Health at serious risk \n Meet Doctor ASAP!")   


image_icon = PhotoImage(file="C:\\Users\\anjis\\Desktop\\work\\COLLEGE\\Internship\\Oasis Infobyte\\BMI Calculator\\Images\\BMI icon.png")
root.iconphoto(False, image_icon)

top=PhotoImage(file = "C:\\Users\\anjis\\Desktop\\work\\COLLEGE\\Internship\\Oasis Infobyte\\BMI Calculator\\Images\\top.png")
top_image = Label(root, image=top, background = "#f0f1f5")
top_image.place(x=-10, y=-10)

Label(root, width=72, height=18, bg="lightgreen").pack(side=BOTTOM)

box=PhotoImage(file="C:\\Users\\anjis\\Desktop\\work\\COLLEGE\\Internship\\Oasis Infobyte\\BMI Calculator\\Images\\box.png")
Label(root, image=box).place(x=20, y=80)
Label(root, image=box).place(x=240, y=80)

scale=PhotoImage(file="C:\\Users\\anjis\\Desktop\\work\\COLLEGE\\Internship\\Oasis Infobyte\\BMI Calculator\\Images\\scale.png")
Label(root, image=scale, bg="lightgreen").place(x=20, y=290)

current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    
    size=int(float(get_current_value()))
    img=(Image.open("C:\\Users\\anjis\\Desktop\\work\\COLLEGE\\Internship\\Oasis Infobyte\\BMI Calculator\\Images\\man.png"))
    resized_image=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550-size)
    secondimage.image=photo2
    
style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=0, to=260, orient='horizontal', style="TScale", command=slider_changed,variable=current_value)
slider.place(x=80,y=220)

Height=StringVar()
Weight=StringVar()
height = Entry(root, textvariable = Height, width=5, font='arial 40', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())
style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale", command=slider_changed2,variable=current_value2)
slider2.place(x=300,y=220)


weight = Entry(root, textvariable = Weight, width=5, font='arial 40', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

secondimage = Label(root, bg="lightgreen")
secondimage.place(x=70, y=530)


Button(root,text="View Report", width=15,height=2,font='arial 10 bold',bg="#1f6e68",fg="white",command=BMI).place(x=300,y=300)

label1=Label(root,font='arial 60 bold', bg="lightgreen", fg="#fff")
label1.place(x=115,y=295)

label2=Label(root,font='arial 20 bold', bg="lightgreen", fg="#3b3a3a")
label2.place(x=260,y=380)

label3=Label(root,font='arial 10 bold', bg="lightgreen")
label3.place(x=250,y=420)


root.mainloop()
