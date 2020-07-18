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
import multiprocessing as mp
import threading as th
import os.path
import gui_support
import twitter_analysis
from funcs import *
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    gui_support.set_Tk_var()
    top = main (root)
    gui_support.init(root, top)
    root.mainloop()
    
w = None
def create_main(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_main(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    gui_support.set_Tk_var()
    top = main (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_main():
    global w
    w.destroy()
    w = None
 
class main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("500x300+547+229")
        top.minsize(1, 1)
        top.maxsize(1345, 668)
        top.resizable(1, 1)
        top.title("OSINT Project")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.4)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.Twitter = tk.Frame(top)
        self.Twitter.place(relx=0.4, rely=0.0, relheight=1.0, relwidth=0.6)
        self.Twitter.configure(relief='groove')
        self.Twitter.configure(borderwidth="2")
        self.Twitter.configure(relief="groove")

        self.Label1 = tk.Label(self.Twitter)
        self.Label1.place(relx=0.067, rely=0.1, height=21, width=100)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(text='''Search Term:''')

        self.Label1_1 = tk.Label(self.Twitter)
        self.Label1_1.place(relx=0.067, rely=0.417, height=21, width=100)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(text='''Location:''')

        self.Label1_2 = tk.Label(self.Twitter)
        self.Label1_2.place(relx=0.067, rely=0.233, height=21, width=100)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(anchor='w')
        self.Label1_2.configure(text='''Start Date:''')

        self.Label2 = tk.Label(self.Twitter)
        self.Label2.place(relx=0.067, rely=0.5, height=21, width=100)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(text='''Radius:''')

        self.Label1_3 = tk.Label(self.Twitter)
        self.Label1_3.place(relx=0.067, rely=0.617, height=21, width=100)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(anchor='w')
        self.Label1_3.configure(text='''Max Tweets:''')

        self.Label1_2 = tk.Label(self.Twitter)
        self.Label1_2.place(relx=0.067, rely=0.3, height=21, width=100)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(anchor='w')
        self.Label1_2.configure(text='''End:''')

        self.collectTweets = tk.Button(self.Twitter)
        self.collectTweets.place(relx=0.067, rely=0.75, height=31, width=260)
        self.collectTweets.configure(activebackground="#f9f9f9")
        self.collectTweets.configure(background="#0fba0f")
        self.collectTweets.configure(command=th.Thread(target=self.run_twee).start())
        self.collectTweets.configure(padx="1")
        self.collectTweets.configure(pady="3")
        self.collectTweets.configure(text='''Collect''')

        self.twitter_query = tk.Entry(self.Twitter)
        self.twitter_query.place(relx=0.4, rely=0.1,height=23, relwidth=0.5)
        self.twitter_query.configure(background="white")
        self.twitter_query.configure(font="TkFixedFont")
        self.twitter_query.configure(selectbackground="blue")
        self.twitter_query.configure(selectforeground="white")
        self.twitter_query.configure(textvariable=gui_support.twitter_query)

        self.twitter_end_date = tk.Entry(self.Twitter)
        self.twitter_end_date.place(relx=0.4, rely=0.3,height=23, relwidth=0.5)
        self.twitter_end_date.configure(background="white")
        self.twitter_end_date.configure(font="TkFixedFont")
        self.twitter_end_date.configure(selectbackground="blue")
        self.twitter_end_date.configure(selectforeground="white")
        self.twitter_end_date.configure(textvariable=gui_support.twitter_end_date)

        self.twitter_max_tweets = tk.Entry(self.Twitter)
        self.twitter_max_tweets.place(relx=0.4, rely=0.617, height=23
                , relwidth=0.5)
        self.twitter_max_tweets.configure(background="white")
        self.twitter_max_tweets.configure(font="TkFixedFont")
        self.twitter_max_tweets.configure(selectbackground="blue")
        self.twitter_max_tweets.configure(selectforeground="white")
        self.twitter_max_tweets.configure(textvariable=gui_support.twitter_max_tweets)

        self.twitter_radius = tk.Entry(self.Twitter)
        self.twitter_radius.place(relx=0.4, rely=0.5,height=23, relwidth=0.5)
        self.twitter_radius.configure(background="white")
        self.twitter_radius.configure(font="TkFixedFont")
        self.twitter_radius.configure(selectbackground="blue")
        self.twitter_radius.configure(selectforeground="white")
        self.twitter_radius.configure(textvariable=gui_support.twitter_radius)

        self.twitter_location = tk.Entry(self.Twitter)
        self.twitter_location.place(relx=0.4, rely=0.417, height=23
                , relwidth=0.5)
        self.twitter_location.configure(background="white")
        self.twitter_location.configure(font="TkFixedFont")
        self.twitter_location.configure(selectbackground="blue")
        self.twitter_location.configure(selectforeground="white")
        self.twitter_location.configure(textvariable=gui_support.twitter_location)

        self.twitter_start_date = tk.Entry(self.Twitter)
        self.twitter_start_date.place(relx=0.4, rely=0.217, height=23
                , relwidth=0.5)
        self.twitter_start_date.configure(background="white")
        self.twitter_start_date.configure(font="TkFixedFont")
        self.twitter_start_date.configure(selectbackground="blue")
        self.twitter_start_date.configure(selectforeground="white")
        self.twitter_start_date.configure(textvariable=gui_support.twitter_start_date)

        self.Youtube = tk.Frame(top)
        self.Youtube.place(relx=0.4, rely=0.0, relheight=1.0, relwidth=0.6)
        self.Youtube.configure(relief='groove')
        self.Youtube.configure(borderwidth="2")
        self.Youtube.configure(relief="groove")

        self.collectYoutube_Btn = tk.Button(self.Youtube)
        self.collectYoutube_Btn.place(relx=0.067, rely=0.75, height=31, width=260)
        self.collectYoutube_Btn.configure(activebackground="#f9f9f9")
        self.collectYoutube_Btn.configure(background="#0fba0f")
        self.collectYoutube_Btn.configure(command=lambda :gui_support.run_youtube(self.youtube_query))
        self.collectYoutube_Btn.configure(text='''Collect Data''')

        self.youtube_keyword = tk.Label(self.Youtube)
        self.youtube_keyword.place(relx=0.333, rely=0.233, height=27, width=100)
        self.youtube_keyword.configure(activebackground="#f9f9f9")
        self.youtube_keyword.configure(text='''Keyword''')

        self.youtube_query = tk.Entry(self.Youtube)
        self.youtube_query.place(relx=0.2, rely=0.367, height=29, relwidth=0.6)

        self.youtube_query.configure(background="white")
        self.youtube_query.configure(font="TkDefaultFont")
        self.youtube_query.configure(selectbackground="blue")
        self.youtube_query.configure(selectforeground="white")
        self.youtube_query.configure(textvariable=gui_support.youtube_query)

        self.Logo = tk.Frame(top)
        self.Logo.place(relx=0.4, rely=0.0, relheight=1.0, relwidth=0.6)
        self.Logo.configure(relief='groove')
        self.Logo.configure(borderwidth="2")
        self.Logo.configure(relief="groove")

        self.twitter_Btn = tk.Button(self.Frame1)
        self.twitter_Btn.place(relx=0.0, rely=0.083, height=31, width=200)
        self.twitter_Btn.configure(activebackground="#f9f9f9")
        self.twitter_Btn.configure(background="#36bcff")
        self.twitter_Btn.configure(command=lambda : gui_support.raiseTwitter(self.Twitter))
        self.twitter_Btn.configure(pady="3m")
        self.twitter_Btn.configure(state='active')
        self.twitter_Btn.configure(text='''Twitter''')

        self.quitBut = tk.Button(self.Frame1)
        self.quitBut.place(relx=0.0, rely=0.75, height=31, width=200)
        self.quitBut.configure(activebackground="#f9f9f9")
        self.quitBut.configure(background="#631818")
        self.quitBut.configure(command=gui_support.checkExit)
        self.quitBut.configure(disabledforeground="#70101d")
        self.quitBut.configure(foreground="#ffffff")
        self.quitBut.configure(text='''Quit''')

        self.youtube_Btn = tk.Button(self.Frame1)
        self.youtube_Btn.place(relx=0.0, rely=0.25, height=31, width=200)
        self.youtube_Btn.configure(activebackground="#f9f9f9")
        self.youtube_Btn.configure(background="#ff2448")
        self.youtube_Btn.configure(command=lambda : gui_support.raiseYoutube(self.Youtube))
        self.youtube_Btn.configure(text='''Youtube''')

        self.logo = tk.Label(self.Logo)
        self.logo.place(relx=0.0, rely=0.0, height=300, width=300)
        self.logo.configure(activebackground="#f9f9f9")
        photo_location = os.path.join(prog_location,"./logo.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.logo.configure(image=_img0)

        self.analyze_Btn = tk.Button(self.Frame1)
        self.analyze_Btn.place(relx=0.0, rely=0.417, height=31, width=200)
        self.analyze_Btn.configure(activebackground="#f9f9f9")
        self.analyze_Btn.configure(background="#40ff73")
        self.analyze_Btn.configure(command=lambda : gui_support.raiseAnalyze(self.Logo))
        self.analyze_Btn.configure(text='''Analyze Data''')

        self.twitter_query.insert(END, "Trump")
        self.twitter_start_date.insert(END, "2020-01-01")
        self.twitter_end_date.insert(END, "2020-07-14")
        self.twitter_location.insert(END, "41.83, -87.62")
        self.twitter_radius.insert(END, "5km")
        self.twitter_max_tweets.insert(END, "1000")

        self.youtube_query.insert(END, "funny")
    def run_twee(self):
            print("yes")
            data=({
                    "query": self.twitter_query.get(),
                    "start_date": self.twitter_start_date.get(),
                    "end_date": self.twitter_end_date.get(),
                    "location": self.twitter_location.get(),
                    "radius": self.twitter_radius.get(),
                    "max_tweets": self.twitter_max_tweets.get()})
            gui_support.run_twitter(data)




if __name__ == '__main__':
    vp_start_gui()





