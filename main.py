import tkinter as tk
from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()



def twitterClick():
    myLabel = Label(root, text="Twitter button pressed")
    myLabel.pack()


def youtubeClick():
    myLabel = Label(root, text="Web button pressed")
    myLabel.pack()


def analyzeClick():
    myLabel = Label(root, text="Time to analyze the code")
    myLabel.pack()


newLabel = Label(root, text="OSINT PROJECT")
newLabel.pack()
twitButton = Button(root, text="Twitter", command=twitterClick)
twitButton.pack()
webButton = Button(root, text="Grab Youtube Data", command=youtubeClick)
webButton.pack()
analysisButton = Button(root, text="Analyze Data", command=analyzeClick)
analysisButton.pack()
button = Button(frame,text="QUIT",fg="red",command=quit)
button.pack()

root.mainloop()
