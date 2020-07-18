import sys
import GetOldTweets3 as got
import os

def get_tweets(tweet_query):
    """
    Call the twitter get old tweet lib with specified info.
    """
    output_dir = "twitter_output"

    tweetCriteria = got.manager.TweetCriteria()
    outputFileName = tweet_query['query'] + "_twitter_output.csv"
    tweetCriteria.querySearch = tweet_query['query']
    tweetCriteria.since = tweet_query['start_date']
    tweetCriteria.until = tweet_query['end_date']
    tweetCriteria.near = tweet_query['location']
    tweetCriteria.within = tweet_query['radius']
    tweetCriteria.maxTweets = int(tweet_query['max_tweets'])
    print("Downloading tweets...")


    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    outputFileName = os.path.join(output_dir, outputFileName)

    outputFile = open(outputFileName, "w+", encoding="utf8")
    outputFile.write('date,username,to,replies,retweets,favorites,text,geo,mentions,hashtags,id,permalink\n')
    cnt = 0

    def receiveBuffer(tweets):
        nonlocal cnt

        for t in tweets:
            data = [t.date.strftime("%Y-%m-%d %H:%M:%S"),
                    t.username,
                    t.to or '',
                    t.replies,
                    t.retweets,
                    t.favorites,
                    '"' + t.text.replace('"', '""') + '"',
                    t.geo,
                    t.mentions,
                    t.hashtags,
                    t.id,
                    t.permalink]
            data[:] = [i if isinstance(i, str) else str(i) for i in data]
            outputFile.write(','.join(data) + '\n')

        outputFile.flush()
        cnt += len(tweets)

        if sys.stdout.isatty():
            print("\rSaved %i" % cnt, end='', flush=True)
        else:
            print(cnt, end=' ', flush=True)

    got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)


