import requests
from bs4 import BeautifulSoup as bs # importing BeautifulSoup
import urllib.request, urllib.error, urllib.parse

# sample youtube video url
#url = "https://www.youtube.com/watch?v=RtSS0SJE8oE"
url = "https://www.youtube.com/results?search_query=funny"

# open-webpage.py
response = urllib.request.urlopen(url)
webContent = response.read()

# get the html content
content = requests.get(url)

# create bs object to parse HTML
try:
    soup = bs(webContent, "html.parser")
    count=soup.find(id="count")
    print(count)
    title = soup.find('meta', {'name': 'title'})
    print(title['content'])

except:
    print("Error retreiving content")
titles=soup.findAll(id='video-title')
print(titles)
# write all HTML code into a file
open("video.html", "w").write(content.text)
open("video.html", "wb").write(webContent)