# OSINT Application Project ITM 448/558
## Social media web scraping tool.

The overall concept of this project is to create a tool to scrape selected social for the Cyber Security Class ITM 448/548 Summer 2020 at Illinois Institute of Technology.

## What is the tool? 
The tool uses two popular social media paradigms for collecting data
- Monitor twitter streams.
- Scrape Youtube data

The tool also puts the tweets through a machine learning pipeline to estimate the sentiment of the tweets using [nltk](https://www.nltk.org/)
> NOTE: The ML algorithm does not deal well with sarcasm

![osint1](/images/osint1.jpg)

## Twitter
The twitter functionality examines tweets around a specified location and get the usernames of the top twitters users
Parameters:
- Query string
- Start date
- End date
- Location (Longitude, Latitude)
- Radius around location (km)
- Max tweets

![osint2](/images/osint2.jpg)

The model is trained with labeled data from the NLTK and gets 99.6% accuracy using a [Naive-Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
![nltk](/images/nltk1.jpg)

|                     |                 |          |         |          |           |                                                                                                                                                                                               |     |                  |                        |                     |                                                                |           | 
|---------------------|-----------------|----------|---------|----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------|------------------------|---------------------|----------------------------------------------------------------|-----------| 
| date                | username        | to       | replies | retweets | favorites | text                                                                                                                                                                                          | geo | mentions         | hashtags               | id                  | permalink                                                      | sentiment | 
| 2020-07-18 23:59:34 | La_Bete_humaine |          | 1       | 1        | 5         | #TrumpIsALaughingStock Because when America needed a leader @realDonaldTrump FAILED! 9 - more later                                                                                           |     | @realDonaldTrump | #TrumpIsALaughingStock | 1284638977832611846 | https://twitter.com/La_Bete_humaine/status/1284638977832611846 | Negative  | 
| 2020-07-18 23:59:28 | PatrickHenryQ   | cona1960 | 0       | 0        | 0         | The word facts is not one he knows how to deal with @realDonaldTrump is a lying sack of crap and liars can’t keep their facts straight everyday he lies sun up to sun up he’s an evil person  |     | @realDonaldTrump |                        | 1284638951551258624 | https://twitter.com/PatrickHenryQ/status/1284638951551258624   | Negative  | 
| 2020-07-18 23:59:05 | Rob_Robb        | nytimes  | 0       | 0        | 0         | A biden and trump presidency is nowhere near the same. What is this?                                                                                                                          |     |                  |                        | 1284638857808486400 | https://twitter.com/Rob_Robb/status/1284638857808486400        | Negative  | 



## Youtube
The youtube functionality examines videos around a based on a search term and get the usernames of most videos matching

![osint2](/images/osint3.jpg)

|                      |                             |               |             |                      |                          |                                                                                                 |                                                                                                                                                                       |                                                |                                  |                                   |                                                  |                                 |                                  |                                                  |                               |                                |                      |                              |                      | 
|----------------------|-----------------------------|---------------|-------------|----------------------|--------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------|-----------------------------------|--------------------------------------------------|---------------------------------|----------------------------------|--------------------------------------------------|-------------------------------|--------------------------------|----------------------|------------------------------|----------------------| 
| kind                 | etag                        | id.kind       | id.videoId  | snippet.publishedAt  | snippet.channelId        | snippet.title                                                                                   | snippet.description                                                                                                                                                   | snippet.thumbnails.default.url                 | snippet.thumbnails.default.width | snippet.thumbnails.default.height | snippet.thumbnails.medium.url                    | snippet.thumbnails.medium.width | snippet.thumbnails.medium.height | snippet.thumbnails.high.url                      | snippet.thumbnails.high.width | snippet.thumbnails.high.height | snippet.channelTitle | snippet.liveBroadcastContent | snippet.publishTime  | 
| youtube#searchResult | 8ec8Td8z22XvnSBgqxU9MKlWjc8 | youtube#video | I9w841nrIBg | 2020-06-26T12:00:09Z | UCLXo7UDZvByw2ixzpQCufnA | What &quot;defund the police&quot; really means                                                 | It's not as radical as it sounds. Become a Video Lab member! http://bit.ly/video-lab Subscribe to our channel! http://goo.gl/0bsAjO Among those protesting police ... | https://i.ytimg.com/vi/I9w841nrIBg/default.jpg | 120                              | 90                                | https://i.ytimg.com/vi/I9w841nrIBg/mqdefault.jpg | 320                             | 180                              | https://i.ytimg.com/vi/I9w841nrIBg/hqdefault.jpg | 480                           | 360                            | Vox                  | none                         | 2020-06-26T12:00:09Z | 
| youtube#searchResult | mRL-UxAckX5gQJxq8HJd7MGW-sQ | youtube#video | leriZ_yEKY8 | 2020-06-08T14:53:11Z | UCH1oRy1dINbMVp3UFWrKP0w | Mayor of Minneapolis addresses calls to &#39;defund police&#39; l GMA                           | Jacob Frey addresses the Minneapolis City Council's intent to move toward dismantling the city's police department and police reform. Subscribe to GMA's ...          | https://i.ytimg.com/vi/leriZ_yEKY8/default.jpg | 120                              | 90                                | https://i.ytimg.com/vi/leriZ_yEKY8/mqdefault.jpg | 320                             | 180                              | https://i.ytimg.com/vi/leriZ_yEKY8/hqdefault.jpg | 480                           | 360                            | Good Morning America | none                         | 2020-06-08T14:53:11Z | 
| youtube#searchResult | KqqPsuiU7hBto6ASqjqFjVt2vk0 | youtube#video | JHbIzVoeWvc | 2020-07-09T10:53:17Z | UCTrQ7HXWRRxr7OsOtodr2_w | &#39;Defund the police&#39; explained: what it really means for the Black Lives Matter movement | The new demand of the black lives matter movement is to defund the police. For many this is an extreme slogan. So what does it mean? Where does it come ...           | https://i.ytimg.com/vi/JHbIzVoeWvc/default.jpg | 120                              | 90                                | https://i.ytimg.com/vi/JHbIzVoeWvc/mqdefault.jpg | 320                             | 180                              | https://i.ytimg.com/vi/JHbIzVoeWvc/hqdefault.jpg | 480                           | 360                            | Channel 4 News       | none                         | 2020-07-09T10:53:17Z | 


## Output
Sample output CSVs can be viewed [here](/SampleOutput)

## Installation
To install this tool:
1. Clone this repository on to your local linux system
2. Run the bash script [/dependency.sh](/dependency.sh)
3. Run [/gui.py](/gui.py)

## Development setup
This project was rapidly developed in about a week for a Summer OSINT assignment if there are any issues feel free to post in the issues and we will get to it

## To Do 
 - [ ] More social media scraping
 	 - [ ] Instagram
	 - [ ] Facebook
     - [ ] Tik Tok
     - [ ] Linkdin

