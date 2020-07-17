from tkinter import *
import tweets

def twitterClick(query):
    print("Twitter Pressed")
    tweets.get_tweets(query)
    query_text = query['query']
    myLabel = Label(text=f"Twitter info saved to {query_text}_twitter_output.csv")
    myLabel.grid()

def youtubeClick(root):
    myLabel = Label(root, text="Web button pressed")
    myLabel.grid()


def analyzeClick(root):
    myLabel = Label(root, text="Time to analyze the code")
    myLabel.grid()

