import tkinter as tk
from funcs import *
import twitter_analysis

root = Tk()
root.title("OSINT ITMS-548")

def openNewWindow(search_term):
    newWindow = Toplevel(root)
    newWindow.title(search_term)
    newWindow.geometry("250x250")

    results = twitter_analysis.analyze_tweets(search_term)
    text = tk.Text(newWindow)
    text.insert(tk.END, str(results[0]))
    text.insert(tk.END, "\n")
    text.insert(tk.END, str(results[1]))
    text.grid()

def run_twitter(query):
    twitterClick(query)
    openNewWindow(query['query'])

def main():
    frame = Frame(root)
    frame.grid()

    newLabel = Label(root, text="OSINT PROJECT")
    newLabel.grid(row=0, column=1)

    # Twitter
    twitter_query = Entry(root)
    twitter_query.insert(END, "Trump")
    twitter_start_date = Entry(root, width=15)
    twitter_start_date.insert(END, "2020-01-01")
    twitter_end_date = Entry(root, width=15)
    twitter_end_date.insert(END, "2020-07-14")
    twitter_location = Entry(root, width=15)
    twitter_location.insert(END, "41.83, -87.62")
    twitter_radius = Entry(root, width=15)
    twitter_radius.insert(END, "5km")
    twitter_max_tweets = Entry(root, width=15)
    twitter_max_tweets.insert(END, "1000")

    twitter_query_label = Label(root, text="Twitter Search Term")
    twitter_query_label.grid(row=1, column=2)
    twitter_query.grid(row=1, column=3)

    twitter_start_date_label = Label(root, text="Start Date")
    twitter_start_date_label.grid(row=2, column=2)
    twitter_start_date.grid(row=2, column=3)

    twitter_end_date_label = Label(root, text="End Date")
    twitter_end_date_label.grid(row=2, column=5)
    twitter_end_date.grid(row=2, column=6)

    twitter_location_label = Label(root, text="Location")
    twitter_location_label.grid(row=3, column=2)
    twitter_location.grid(row=3, column=3)

    twitter_end_date_label = Label(root, text="Radius")
    twitter_end_date_label.grid(row=4, column=2)
    twitter_radius.grid(row=4, column=3)

    twitter_location_label = Label(root, text="Max Tweets")
    twitter_location_label.grid(row=4, column=5)
    twitter_max_tweets.grid(row=4, column=6)

    twitButton = Button(root, text="Twitter", command=lambda: run_twitter({
        "query": twitter_query.get(),
        "start_date": twitter_start_date.get(),
        "end_date": twitter_end_date.get(),
        "location": twitter_location.get(),
        "radius": twitter_radius.get(),
        "max_tweets": twitter_max_tweets.get()}))
    # dict needs to be called in lambda to allow update when button clicked.
    twitButton.grid(row=1, column=1, pady=10)


    webButton = Button(root, text="Grab Youtube Data", command=youtubeClick)
    webButton.grid(row=4, column=1, pady=10)
    analysisButton = Button(root, text="Analyze Data", command=analyzeClick)
    analysisButton.grid(row=6, column=1, pady=10)
    button = Button(frame,text="QUIT",fg="red",command=quit)
    button.grid(row=4, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()


