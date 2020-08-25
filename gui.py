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

import threading as th
import os.path
import gui_support
import twitter.twitter_analysis as twitter_analysis
import files

def create_main(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_main(root, *args, **kwargs)' .'''
    global w, root
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
    def run_twitter_command(self):
        print("Twitter thread starting")
        data=({
                "query": self.twitter_query.get(),
                "start_date": self.twitter_start_date.get(),
                "end_date": self.twitter_end_date.get(),
                "location": self.twitter_location.get(),
                "radius": self.twitter_radius.get(),
                "max_tweets": self.twitter_max_tweets.get()})
        gui_support.run_twitter(data)
        
    def run_youtube_command(self):
        print("Youtube thread starting")
        gui_support.run_youtube(self.youtube_query.get(),self.youtube_count.get())

    def run_chicago_command(self):
            print("Chicago thread starting")
            data=({
                    "start_date": self.chicago_startDate.get(),
                    "end_date": self.chicago_endDate.get(),
                    "latnw": self.chicago_latnw.get(),
                    "longnw": self.chicago_longnw.get(),
                    "latse": self.chicago_latse.get(),
                    "longse": self.chicago_longse.get(),
                    "analysis": self.chicago_analysis.current()
                    })
            gui_support.run_chicago(data)
            
            
    def run_twitter_thread(self):
        self.tt.start()
        self.tt = th.Thread(target=self.run_twitter_command, args=())

    def run_youtube_thread(self):
        self.yh.start()
        self.yh = th.Thread(target=self.run_youtube_command,args=())

    def run_chicago_thread(self):
        self.ct.start()
        self.ct = th.Thread(target=self.run_chicago_command,args=())

    def __init__(self, top=None):
        self.yh = th.Thread(target=self.run_youtube_command,args=())
        self.tt = th.Thread(target=self.run_twitter_command, args=())
        self.ct = th.Thread(target=self.run_chicago_command, args=())
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
        self.collectTweets.configure(command=self.run_twitter_thread)
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
        self.collectYoutube_Btn.configure(command=self.run_youtube_thread)
        self.collectYoutube_Btn.configure(text='''Collect Data''')

        self.youtube_keyword = tk.Label(self.Youtube)
        self.youtube_keyword.place(relx=0.333, rely=0.133, height=27, width=100)
        self.youtube_keyword.configure(activebackground="#f9f9f9")
        self.youtube_keyword.configure(text='''Keyword''')

        self.youtube_query = tk.Entry(self.Youtube)
        self.youtube_query.place(relx=0.2, rely=0.267,height=29, relwidth=0.6)
        self.youtube_query.configure(background="white")
        self.youtube_query.configure(font="TkDefaultFont")
        self.youtube_query.configure(selectbackground="blue")
        self.youtube_query.configure(selectforeground="white")
        self.youtube_query.configure(textvariable=gui_support.youtube_query)

        self.youtube_count = tk.Entry(self.Youtube)
        self.youtube_count.place(relx=0.2, rely=0.533,height=29, relwidth=0.6)
        self.youtube_count.configure(background="white")
        self.youtube_count.configure(font="TkDefaultFont")
        self.youtube_count.configure(selectbackground="blue")
        self.youtube_count.configure(selectforeground="white")
        self.youtube_count.configure(textvariable=gui_support.youtube_count)

        self.youtube_count_Label = tk.Label(self.Youtube)
        self.youtube_count_Label.place(relx=0.333, rely=0.4, height=27
                , width=100)
        self.youtube_count_Label.configure(activebackground="#f9f9f9")
        self.youtube_count_Label.configure(text='''Count''')

        self.Chicago = tk.Frame(top)
        self.Chicago.place(relx=0.4, rely=0.0, relheight=1.0, relwidth=0.6)
        self.Chicago.configure(relief='groove')
        self.Chicago.configure(borderwidth="2")
        self.Chicago.configure(relief="groove")

        self.Logo = tk.Frame(top)
        self.Logo.place(relx=0.4, rely=0.0, relheight=1.0, relwidth=0.6)
        self.Logo.configure(relief='groove')
        self.Logo.configure(borderwidth="2")
        self.Logo.configure(relief="groove")

        self.twitter_Btn = tk.Button(self.Frame1)
        self.twitter_Btn.place(relx=0.0, rely=0.083, height=31, relwidth=1)
        self.twitter_Btn.configure(activebackground="#f9f9f9")
        self.twitter_Btn.configure(background="#36bcff")
        self.twitter_Btn.configure(command=lambda : gui_support.raiseTwitter(self.Twitter))
        self.twitter_Btn.configure(pady="3m")
        self.twitter_Btn.configure(text='''Twitter''')

        self.quitBut = tk.Button(self.Frame1)
        self.quitBut.place(relx=0.0, rely=0.833, height=31, relwidth=1)
        self.quitBut.configure(activebackground="#f9f9f9")
        self.quitBut.configure(background="#631818")
        self.quitBut.configure(command=gui_support.checkExit)
        self.quitBut.configure(disabledforeground="#70101d")
        self.quitBut.configure(foreground="#ffffff")
        self.quitBut.configure(text='''Quit''')

        self.youtube_Btn = tk.Button(self.Frame1)
        self.youtube_Btn.place(relx=0.0, rely=0.25, height=31, relwidth=1)
        self.youtube_Btn.configure(activebackground="#f9f9f9")
        self.youtube_Btn.configure(background="#ff2448")
        self.youtube_Btn.configure(command=lambda : gui_support.raiseYoutube(self.Youtube))
        self.youtube_Btn.configure(text='''Youtube''')

        self.chicago_Btn = tk.Button(self.Frame1)
        self.chicago_Btn.place(relx=0.0, rely=0.417, height=31, relwidth=1)
        self.chicago_Btn.configure(activebackground="#f9f9f9")
        self.chicago_Btn.configure(background="#d8d847")
        self.chicago_Btn.configure(command=lambda : gui_support.raiseChicago(self.Chicago))
        self.chicago_Btn.configure(text='''Chicago Crime''')

        self.chicago_startDate_Label = tk.Label(self.Chicago)
        self.chicago_startDate_Label.place(relx=0.1, rely=0.083, height=21, width=100)
        self.chicago_startDate_Label.configure(activebackground="#f9f9f9")
        self.chicago_startDate_Label.configure(anchor='w')
        self.chicago_startDate_Label.configure(text='''Start Date:''')

        self.chicago_latse_Label = tk.Label(self.Chicago)
        self.chicago_latse_Label.place(relx=0.1, rely=0.517, height=21, width=100)
        self.chicago_latse_Label.configure(activebackground="#f9f9f9")
        self.chicago_latse_Label.configure(anchor='w')
        self.chicago_latse_Label.configure(text='''Lat SE:''')

        self.chicago_latnw_Label = tk.Label(self.Chicago)
        self.chicago_latnw_Label.place(relx=0.1, rely=0.35, height=21, width=100)
        self.chicago_latnw_Label.configure(activebackground="#f9f9f9")
        self.chicago_latnw_Label.configure(anchor='w')
        self.chicago_latnw_Label.configure(text='''Lat NW:''')

        self.chicago_longse_Label = tk.Label(self.Chicago)
        self.chicago_longse_Label.place(relx=0.5, rely=0.517, height=21, width=100)
        self.chicago_longse_Label.configure(activebackground="#f9f9f9")
        self.chicago_longse_Label.configure(anchor='w')
        self.chicago_longse_Label.configure(text='''Long SE:''')

        self.chicago_endDate_Label = tk.Label(self.Chicago)
        self.chicago_endDate_Label.place(relx=0.5, rely=0.083, height=21, width=100)
        self.chicago_endDate_Label.configure(activebackground="#f9f9f9")
        self.chicago_endDate_Label.configure(anchor='w')
        self.chicago_endDate_Label.configure(text='''End Date:''')

        self.chicago_longnw_Label = tk.Label(self.Chicago)
        self.chicago_longnw_Label.place(relx=0.5, rely=0.35, height=21, width=100)
        self.chicago_longnw_Label.configure(activebackground="#f9f9f9")
        self.chicago_longnw_Label.configure(anchor='w')
        self.chicago_longnw_Label.configure(text='''Long NW''')

        self.chicago_analysis = ttk.Combobox(self.Chicago)
        self.chicago_analysis.place(relx=0.1, rely=0.733, relheight=0.07, relwidth=0.5)
        self.chicago_analysis.configure(values=['Crime Type','Crime a week','Crime a month','Arrest Record'])
        self.chicago_analysis.set('Crime Type')
        self.chicago_analysis.configure(takefocus="")

        self.collectChicago = tk.Button(self.Chicago)
        self.collectChicago.place(relx=0.067, rely=0.833, height=31, width=260)
        self.collectChicago.configure(activebackground="#f9f9f9")
        self.collectChicago.configure(background="#0fba0f")
        self.collectChicago.configure(command=self.run_chicago_thread)
        self.collectChicago.configure(padx="1")
        self.collectChicago.configure(pady="3")
        self.collectChicago.configure(text='''Collect''')

        self.chicago_startDate = tk.Entry(self.Chicago)
        self.chicago_startDate.place(relx=0.1, rely=0.15, height=23
                , relwidth=0.333)
        self.chicago_startDate.configure(background="white")
        self.chicago_startDate.configure(font="TkFixedFont")
        self.chicago_startDate.configure(selectbackground="blue")
        self.chicago_startDate.configure(selectforeground="white")

        self.chicago_longnw = tk.Entry(self.Chicago)
        self.chicago_longnw.place(relx=0.5, rely=0.417,height=23, relwidth=0.333)
        self.chicago_longnw.configure(background="white")
        self.chicago_longnw.configure(font="TkFixedFont")
        self.chicago_longnw.configure(selectbackground="blue")
        self.chicago_longnw.configure(selectforeground="white")

        self.chicago_endDate = tk.Entry(self.Chicago)
        self.chicago_endDate.place(relx=0.5, rely=0.15, height=23, relwidth=0.367)

        self.chicago_endDate.configure(background="white")
        self.chicago_endDate.configure(font="TkFixedFont")
        self.chicago_endDate.configure(selectbackground="blue")
        self.chicago_endDate.configure(selectforeground="white")

        self.chicago_longse = tk.Entry(self.Chicago)
        self.chicago_longse.place(relx=0.5, rely=0.583,height=23, relwidth=0.333)
        self.chicago_longse.configure(background="white")
        self.chicago_longse.configure(font="TkFixedFont")
        self.chicago_longse.configure(selectbackground="blue")
        self.chicago_longse.configure(selectforeground="white")

        self.chicago_latse = tk.Entry(self.Chicago)
        self.chicago_latse.place(relx=0.1, rely=0.583,height=23, relwidth=0.333)
        self.chicago_latse.configure(background="white")
        self.chicago_latse.configure(font="TkFixedFont")
        self.chicago_latse.configure(selectbackground="blue")
        self.chicago_latse.configure(selectforeground="white")

        self.chicago_latnw = tk.Entry(self.Chicago)
        self.chicago_latnw.place(relx=0.1, rely=0.417,height=23, relwidth=0.333)
        self.chicago_latnw.configure(background="white")
        self.chicago_latnw.configure(font="TkFixedFont")
        self.chicago_latnw.configure(selectbackground="blue")
        self.chicago_latnw.configure(selectforeground="white")

        self.chicago_geoFenceLabel = tk.Label(self.Chicago)
        self.chicago_geoFenceLabel.place(relx=0.3, rely=0.283, height=21, width=150)
        self.chicago_geoFenceLabel.configure(activebackground="#f9f9f9")
        self.chicago_geoFenceLabel.configure(anchor='w')
        self.chicago_geoFenceLabel.configure(text='''Area of Interest''')

        self.analyze_Btn = tk.Button(self.Frame1)
        self.analyze_Btn.place(relx=0.0, rely=0.583, height=31, relwidth=1)
        self.analyze_Btn.configure(activebackground="#f9f9f9")
        self.analyze_Btn.configure(background="#40ff73")
        self.analyze_Btn.configure(command=lambda : gui_support.raiseAnalyze(self.Logo))
        self.analyze_Btn.configure(text='''Analyze Data''')

        self.logo = tk.Label(self.Logo)
        self.logo.place(relx=0.0, rely=0.0, height=300, width=300)
        self.logo.configure(activebackground="#f9f9f9")
        photo_location = os.path.join(prog_location,"./logo.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.logo.configure(image=_img0)

        self.twitter_query.insert(tk.END, "Trump")
        self.twitter_start_date.insert(tk.END, "2020-01-01")
        self.twitter_end_date.insert(tk.END, "2020-07-14")
        self.twitter_location.insert(tk.END, "41.83, -87.62")
        self.twitter_radius.insert(tk.END, "5km")
        self.twitter_max_tweets.insert(tk.END, "1000")

        self.chicago_latnw.insert(tk.END, "41.975121")
        self.chicago_latse.insert(tk.END, "41.978260")
        self.chicago_longnw.insert(tk.END, "-87.791649")
        self.chicago_longse.insert(tk.END, "-87.763931")
        self.chicago_startDate.insert(tk.END, "2019-01-01T12:00:00")
        self.chicago_endDate.insert(tk.END, "2019-07-16T14:00:00")

        self.youtube_query.insert(tk.END, "funny")
        self.youtube_count.insert(tk.END,10)
    



