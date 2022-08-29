import numbers
from tkinter import *
import random
import tkinter

window = Tk()

def show_thing_1():
    frame_thing_1.pack()


menubar = Menu(window)
window.config(menu=menubar)


mainmenu = Menu(menubar)
mainmenu.add_command(label="Game 1", command=show_thing_1)         
mainmenu.add_separator()
mainmenu.add_command(label="Exit", command=window.quit)

menubar.add_cascade(label="Menu", menu=mainmenu)


frame_thing_1 = Frame(borderwidth=10)
label_1 = Label(frame_thing_1)
label_1.pack()


label = Label(window,font=('bold',400))
def dobbelsteen():
    nummer = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(nummer)}')
    label.pack()

window.minsize(600,600)
window.maxsize(700,700) 
window.title('DOBBELSTEEN')


heading = Label(window,text='DOBBELSTEEN',font=('bold',50),bg='red')
heading.pack(fill=X)

frame1 = Frame(master=window, height=80, bg="white")
frame1.pack(fill=tkinter.X)

frame2 = Frame(master=window, height=80, bg="blue")
frame2.pack(fill=tkinter.X)

button = Button(window,text='Gooi',font=('normal',25),bg='orange',command=lambda:dobbelsteen())
button.pack()

show_thing_1()

window.mainloop()

#deodojdoejodj