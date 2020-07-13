from tkinter import *
import tweets

def twitterClick(tweet_query):
    print("Twitter Pressed")
    tweets.get_tweets(tweet_query)
    myLabel = Label(text="Twitter info saved to twitter_output.csv")
    myLabel.grid()

def youtubeClick(root):
    myLabel = Label(root, text="Web button pressed")
    myLabel.grid()


def analyzeClick(root):
    myLabel = Label(root, text="Time to analyze the code")
    myLabel.grid()

