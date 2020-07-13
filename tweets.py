import sys
import GetOldTweets3 as got

def get_tweets():
    """
    Call the twitter get old tweet lib with specified info.
    """
    tweetCriteria = got.manager.TweetCriteria()
    outputFileName = "twitter_output.csv"
    tweetCriteria.querySearch = "covid"  # TODO Get input from user
    tweetCriteria.since = "2020-01-01"  # TODO Get input from user
    tweetCriteria.until = "2020-07-31"  # TODO Get input from user
    tweetCriteria.near = '41.83, -87.62'  # TODO Get input from user
    tweetCriteria.within = "3km" # TODO Get input from user also why is this km?
    tweetCriteria.maxTweets = 100
    print("Downloading tweets...")

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


