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

import twitter.twitter_analysis as twitter_analysis
import twitter.tweets as tweets
from tkinter import messagebox
import os
from chicago.plots import *
import youtube.youtube as you
import youtube.analyze as anal
import chicago.chicago as chicago
import subprocess

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

<<<<<<< HEAD
def raiseChicago(frame):
    print("Bring Chicago to front")
    frame.lift()

=======
>>>>>>> 359e935b24b99f84494c44b68d3a645bb07167c9
def raiseAnalyze(frame):
    print("Bring Analyze to front")
    frame.lift()

def checkExit():
    print("Run exit script")
    if (messagebox.askokcancel(title="OSINT", message="Are you want to exit, OK or Cancel") == 1) :
        os._exit(1)

def run_twitter(query):
<<<<<<< HEAD
    print("Twitter Pressed")
    tweets.get_tweets(query)
=======
    twitterClick(query)
>>>>>>> 359e935b24b99f84494c44b68d3a645bb07167c9
    openNewWindow(query['query'])

def run_youtube(youtube_query,youtube_count):
    you.run_youtube_click(youtube_query,int(youtube_count))
<<<<<<< HEAD
    openYoutubeAnalyze(youtube_query)

def run_chicago(query):
    print(query['analysis'])
    chicago.pullData(query)
    analysis(query['analysis'])

def analysis(selection):
    print(selection)
    if selection==0:barh()
    if selection==1:weekRange()
    if selection==2:monthRange()
    if selection==3:caughtPlot()
=======

def twitterClick(query):
    print("Twitter Pressed")
    tweets.get_tweets(query)
    query_text = query['query']
    #myLabel = Label(text=f"Twitter info saved to {query_text}_twitter_output.csv")
    #myLabel.grid()
>>>>>>> 359e935b24b99f84494c44b68d3a645bb07167c9

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
<<<<<<< HEAD

def openYoutubeAnalyze(qs):
    newWindow = tk.Toplevel()
    newWindow.title(qs)
    newWindow.geometry("250x250")

    results = anal.analyze(qs)
    text = tk.Text(newWindow)
    for each in results:
        text.insert(tk.END, str(each[1]))
        text.insert(tk.END, "\t")
        text.insert(tk.END, str(each[0]))
        text.insert(tk.END, "\n")
        text.grid()
=======
>>>>>>> 359e935b24b99f84494c44b68d3a645bb07167c9
