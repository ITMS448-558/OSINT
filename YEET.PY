import requests
from bs4 import BeautifulSoup as bs # importing BeautifulSoup

# sample youtube video url
video_url = "https://www.youtube.com/watch?v=RtSS0SJE8oE"
# get the html content
content = requests.get(video_url)
# create bs object to parse HTML
soup = bs(content.content, "html.parser")
# write all HTML code into a file
open("video.html", "w", encoding='utf8').write(content.text)