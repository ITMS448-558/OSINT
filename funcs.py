from tkinter import *
import tweets

def twitterClick():
    print("Twitter Pressed")
    tweets.get_tweets()
    myLabel = Label(text="Twitter info saved to twitter_output.csv")
    myLabel.pack()


def youtubeClick(root):
    myLabel = Label(root, text="Web button pressed")
    myLabel.pack()


def analyzeClick(root):
    myLabel = Label(root, text="Time to analyze the code")
    myLabel.pack()

