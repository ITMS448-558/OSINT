import tkinter as tk
from funcs import *

root = Tk()
root.geometry("400x300")
frame = Frame(root)
frame.pack()

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
