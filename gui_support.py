#! /usr/bin/env python
import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import twitter_analysis
from tkinter import messagebox
import os
import tweets
import youtube.youtube as you

#line 223 Needs to be added for analyze
app_title= ""
youtube_count=0
youtube_query=""
twitter_end_date=""
twitter_location=""
twitter_max_tweets=""
twitter_start_date=""
twitter_radius=""
twitter_query=""

def pull():
    print("Hello")

def set_Tk_var():
    print("Define all global variables for root")
    app_title="OSINT PROJECT"
    
def init(root, top):
    print("Start the engines on something I suppose")
    
def raiseTwitter(frame):
    print("Bring Twitter to front")
    frame.lift()

def raiseYoutube(frame):
    print("Bring Youtube to front")
    frame.lift()

def raiseAnalyze(frame):
    print("Bring Analyze to front")
    frame.lift()

def checkExit():
    print("Run exit script")
    if (messagebox.askokcancel(title="OSINT", message="Are you want to exit, OK or Cancel") == 1) :
        os._exit(1)

def run_twitter(query):
    twitterClick(query)
    openNewWindow(query['query'])

def run_youtube(youtube_query,youtube_count):
    you.run_youtube_click(youtube_query,int(youtube_count))

def twitterClick(query):
    print("Twitter Pressed")
    tweets.get_tweets(query)
    query_text = query['query']
    #myLabel = Label(text=f"Twitter info saved to {query_text}_twitter_output.csv")
    #myLabel.grid()

def openNewWindow(search_term):
    newWindow = tk.Toplevel()
    newWindow.title(search_term)
    newWindow.geometry("250x250")

    results = twitter_analysis.analyze_tweets(search_term)
    text = tk.Text(newWindow)
    text.insert(tk.END, str(results[0]))
    text.insert(tk.END, "\n")
    text.insert(tk.END, str(results[1]))
    text.grid()
