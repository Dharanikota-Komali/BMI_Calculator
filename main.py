from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import mysql.connector


root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")





def BMI():
    height=float(Height.get())
    weight=float(Weight.get())

    #convert height into meter

    if height<=7.00:
        m=height*0.3048
        print("height in meters = ",m)
        
        #bmi=round(float(weight/m**2),2)
        #label1.config(text=bmi)
        #print("bmi = ",bmi)
    
    else:
        m=height/100
        print("height in meters = ",m)
        
    bmi = round(float(weight/m**2),2)
    
    label1.config(text=bmi)
    print("bmi = ",bmi)



    if bmi<=18.5:
        label2.config(text="Underweight")
        label3.config(text="you have lower weight \n then normal body!")

    elif bmi>18.5 and bmi<=25:
        label2.config(text="Normal!")
        label3.config(text="It Indicates that you are healthy!")

    elif bmi>25 and bmi<=30:
        label2.config(text="Overweight!")
        label3.config(text="It Indicates that a person is \n slightly overweight! \n A Doctor may advise to lose some \n weight for health reasons!")

    else:
        label2.config(text="Obes!")
        label3.config(text="Health may be risk, if they do not \n lose weight!")
    #creating database connection
    cnx = mysql.connector.connect(
        host='localhost',
        user='komali',
        password='Dharanikota@99',
        database='bmi'
    )

    cursor = cnx.cursor()
 

    create_table_query = """
    CREATE TABLE IF NOT EXISTS bmi_data1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        height FLOAT,
        weight FLOAT,
        bmi FLOAT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(create_table_query)

    insert_data_query = """ INSERT INTO bmi_data1 (height, weight, bmi) VALUES (%s, %s, %s)"""
 
    data = (height, weight, bmi)
    cursor.execute(insert_data_query, data)

    # Commit the changes to the database
    cnx.commit()

    cursor.close()
    cnx.close()

     

#icon
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

#top
top=PhotoImage(file="Images/top.png")
top_image=Label(root,image=top,background="#f0f1f5")
top_image.place(x=-10,y=-10)

#bottom box
Label(root,width=72,height=18,bg="lightgreen").pack(side=BOTTOM)

#two boxes
box=PhotoImage(file="Images/box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)

#scale
scale=PhotoImage(file="Images/scale.png")
Label(root,image=scale,bg="lightgreen").place(x=20,y=310)



############Slider1################
current_value=tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size=int(float(get_current_value()))
    img=(Image.open("Images/man.png"))
    resized_image=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70,y=550-size)
    secondimage.image=photo2

#command to change background color of scale
style=ttk.Style()
style.configure("TScale",background="White")


slider=ttk.Scale(root,from_=0, to=220,orient='horizontal',
                 command=slider_changed,variable=current_value)
slider.place(x=80,y=250)

###################################





#############Slider2################

current_value2=tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

#command to change background color of scale
style2=ttk.Style()
style2.configure("TScale",background="White")


slider2=ttk.Scale(root,from_=0, to=200,orient='horizontal',
                 command=slider_changed2,variable=current_value2)
slider2.place(x=300,y=250)

###################################





#Entry box
Height=StringVar()
Weight=StringVar()
height=Entry(root,textvariable=Height,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)  #to align text in center
height.place(x=35,y=160)
Height.set(get_current_value())



weight=Entry(root,textvariable=Weight,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)  #to align text in center
weight.place(x=255,y=160)
Weight.set(get_current_value())




#man image
secondimage=Label(root,bg="lightgreen")
secondimage.place(x=70,y=530)


Button(root,text="view Report",width=15,height=2,font="arial 10 bold", bg="#1f6e68",fg="white",command=BMI).place(x=280,y=340)

label1=Label(root,font="arial 15 bold", bg="lightgreen",fg="#fff")
label1.place(x=205,y=430)

label2=Label(root,font="arial 20 bold", bg="lightgreen",fg="#3b3a3a")
label2.place(x=270,y=430)


label3=Label(root,font="arial 10 ", bg="lightgreen",fg="black")
label3.place(x=250,y=500)

label4=Label(text="BMI = ", font="arial 15 bold",bg="lightgreen", fg="#fff")
label4.place(x=130, y=430)

label5=Label(text="height", font="arial 15 bold",bg="#f0f1f5", fg="black")
label5.place(x=100, y=70)

label6=Label(text="weight", font="arial 15 bold",bg="#f0f1f5", fg="black")
label6.place(x=320, y=70)


root.mainloop()
