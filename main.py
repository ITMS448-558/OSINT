import tkinter as tk
from funcs import *
import twitter_analysis

root = Tk()

frame = Frame(root)
frame.grid(row=0)


def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("Twitter Results")
    newWindow.geometry("200x200")

    results = twitter_analysis.analyze_tweets()
    print(results)
    text = tk.Text(newWindow)
    text.insert(tk.END, str(results))
    text.grid()

def run_twitter(query):
    twitterClick(query)
    openNewWindow()



# label = Label(root,
#               text="This is the main window")
#
# label.grid(row=0, column=1)(pady=10)

newLabel = Label(root, text="OSINT PROJECT")
newLabel.grid(row=0, column=1)

# Twitter
twitter_query = Entry(root)
twitter_start_date = Entry(root)

twitter_query_label = Label(root, text="Twitter Search Term")
twitter_query_label.grid(row=1, column=2)
twitter_query.grid(row=1, column=3)

twitButton = Button(root, text="Twitter", command=lambda: run_twitter(twitter_query.get()))
twitButton.grid(row=1, column=1, pady=10)


webButton = Button(root, text="Grab Youtube Data", command=youtubeClick)
webButton.grid(row=4, column=1, pady=10)
analysisButton = Button(root, text="Analyze Data", command=analyzeClick)
analysisButton.grid(row=6, column=1, pady=10)
button = Button(frame,text="QUIT",fg="red",command=quit)
button.grid(row=4, column=1, pady=10)

root.mainloop()


