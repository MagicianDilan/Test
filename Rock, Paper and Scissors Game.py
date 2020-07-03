from tkinter import *
from random import *
from PIL import Image, ImageTk

main = Tk()
main.geometry("640x300")
main.title("Rock, paper and Scissors Game")
main.configure(bg = "grey65")
title1 = Label(text = "Choose your weapon!", bg = "grey65",font = ("Comic Sans MC",20))
title1.place(x = 18, y = 35)

a = 0 #Aux, to save the person choice

imagen_rock = ImageTk.PhotoImage(Image.open(r"rock.jpg").resize((150, 150)))
imagen_paper = ImageTk.PhotoImage(Image.open(r"paper.jpg").resize((150, 150)))
imagen_scissors = ImageTk.PhotoImage(Image.open(r"scissors.jpg").resize((150, 150)))

def put_rock():
    titulo_rock = Label(image=imagen_rock)
    titulo_rock.place(x=50, y=130)
    global a
    a = 1
def put_paper():
    titulo = Label(image=imagen_paper)
    titulo.place(x=50, y=130)
    global a
    a = 2
def put_scissors():
    titulo = Label(image=imagen_scissors)
    titulo.place(x=50, y=130)
    global a
    a = 3
def put_image_compu(b):
    if (b ==1):
        titulo_rock = Label(image=imagen_rock)
        titulo_rock.place(x=415, y=130)
    elif (b==2):
        titulo = Label(image=imagen_paper)
        titulo.place(x=415, y=130)
    elif (b==3):
        titulo = Label(image=imagen_scissors)
        titulo.place(x=415, y=130)
def put_ready(a):
    b = randint(1,3)
    put_image_compu(b)
    title3 = Label(text="Computer selection", bg="grey65", font=("Comic Sans MC", 20))
    title3.place(x=370, y=70)
    if (b==1 and a==1):
        title2 = Label(text="Tie *_*", bg="grey65", fg = "white", font=("Comic Sans MC", 18), width = 10)
        title2.place(x=230, y=210)
    elif  (b==1 and a == 2):
        title2 = Label(text="You Won!:)", bg="grey65", fg="green", font=("Comic Sans MC", 18))
        title2.place(x=250, y=210)
    elif (b == 1 and a == 3):
        title2 = Label(text="You loose:(", bg="grey65", fg="red", font=("Comic Sans MC", 18))
        title2.place(x=250, y=210)
    elif (b == 2 and a == 1):
        title2 = Label(text="You loose:(", bg="grey65", fg="red", font=("Comic Sans MC", 18))
        title2.place(x=250, y=210)
    elif (b == 2 and a == 2):
        title2 = Label(text="Tie *_*", bg="grey65", fg="white", font=("Comic Sans MC", 18), width = 10)
        title2.place(x=230, y=210)
    elif (b == 2 and a == 3):
        title2 = Label(text="You Won!:)", bg="grey65", fg="green", font=("Comic Sans MC", 18))
        title2.place(x=250, y=210)
    elif (b == 3 and a == 1):
        title2 = Label(text="You Won!:)", bg="grey65", fg="green", font=("Comic Sans MC", 18))
        title2.place(x=250, y=210)
    elif (b == 3 and a == 2):
        title2 = Label(text="You loose:(", bg="grey65", fg="red", font=("Comic Sans MC", 18))
        title2.place(x=250, y=210)
    elif (b == 3 and a == 3):
        title2 = Label(text="Tie *_*", bg="grey65", fg="white", font=("Comic Sans MC", 18),  width = 10)
        title2.place(x=230, y=210)

boton_rock = Button(text = "Rock", command = put_rock , width = 8).place(x = 20, y = 80)
boton_paper = Button(text = "Paper", command = put_paper, width = 8).place(x = 95, y = 80)
boton_scissors = Button(text = "Scissors", command = put_scissors, width = 8).place(x = 170, y = 80)
boton_ready = Button(text = "Ready!", command = lambda: put_ready(a), width = 8).place(x = 280, y = 180)

mainloop()