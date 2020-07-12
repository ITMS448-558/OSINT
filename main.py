from tkinter import *

root=Tk()
import tkinter as tk
    

def write_slogan():
    print("Tkinter is easy to use!")
frame = Frame(root)
frame.pack()

button = Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=LEFT)
slogan = Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=LEFT)

def twitterClick():
    myLabel=Label(root,text="Twitter button pressed")
    myLabel.pack()
def webClick():
    myLabel=Label(root,text="Web button pressed")
    myLabel.pack()

newLabel=Label(root,text="OSINT PROJECT")
newLabel.pack()
twitButton=Button(root,text="Twitter", command=twitterClick)
twitButton.pack()
webButton=Button(root,text="Grab web data", command=webClick)
webButton.pack()

root.mainloop()