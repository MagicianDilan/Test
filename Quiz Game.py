'''
This will be a quiz game who has been tought for childrens at elementary school.
-Desktop program with tkinter frame
-Using two dictionaries. One for questions and other for the answers.
-The principal menu has 3 options: Play a game,  exit
-each game will have 20 questions from a vaul of 200, topics are gonna be sciense, art, spanish, geography.
'''
from tkinter import *
from tkinter import messagebox

def how_to():
    def back():
        how_to_play.destroy()
    how_to_play = Tk()
    button5 = Button(how_to_play,text="Back", command=back)
    button5.pack( side = TOP and LEFT)
    title2 = Label(how_to_play, text=" Then repeat the same until you finish all questions (20). Finally see your result and share it with your friends!", font=("Times New Romans", 15))
    title2.pack(side = BOTTOM)
    title1 = Label(how_to_play, text="\tHow to play.\nFirst you need to click 'Play button' and choose the\n anwser you think is correct.", font=("Times New Romans", 15))
    title1.pack(side = BOTTOM)

main = Tk()
main.geometry("300x200")
main.title("Quiz Game")
title = Label(text = "How much do you know?", font = ("Times New Romans", 15))
title.pack()
button1 = Button(text ="Play", command = lambda: print("Hello")).pack()
button2 = Button(text ="How to play?", command = how_to).pack()
button3 = Button(text ="Exit", command = main.destroy).pack()
mainloop()