import pandas as pd
from nltk.tokenize import word_tokenize
import nlp_test
import numpy as np

def get_sentiment(row):
    text = row['text']
    custom_tokens = nlp_test.remove_noise(word_tokenize(text))
    sentiment = nlp_test.classifier.classify(dict([token, True] for token in custom_tokens))
    return sentiment

def analyze_tweets():

    df = pd.read_csv(
        "twitter_output.csv"
    )

    # df cleaning , remove blank text and Nan values
    df['text'].replace('', np.nan, inplace=True)
    df.dropna(subset=['text'], inplace=True)
    df = df[df['text'].astype(bool)]

    # add sentament column
    df["sentiment"] = df.apply(lambda row: get_sentiment(row), axis=1)
    #
    df.to_csv('twitter_with_sentiment.csv', index=False)

    #username_series = df.groupby("username")["sentiment"].value_counts(normalize=True).mul(100)
    username_series = df.groupby("username")["sentiment"].value_counts(normalize=True).mul(100).to_frame()
    username_series.to_csv('tweet_sentiment_overview.csv', index=False)


    username_df =  df["username"].value_counts()
    return username_df.head(10)

    #nlp_test.classifier.classify(dict([token, True] for token in nlp_test.remove_noise(word_tokenize(df["text"]))

