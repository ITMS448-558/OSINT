import os
import pandas as pd
from nltk.tokenize import word_tokenize
import twitter.nlp_test as nlp_test
import numpy as np

def get_sentiment(row):
    text = row['text']
    custom_tokens = nlp_test.remove_noise(word_tokenize(text))
    sentiment = nlp_test.classifier.classify(dict([token, True] for token in custom_tokens))
    return sentiment

def analyze_tweets(query):
    output_dir = "twitter_output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    input_csv = f"{query}_twitter_output.csv"
    input_csv = os.path.join(output_dir, input_csv)

    # read csv in
    df = pd.read_csv(
        input_csv
    )

    # df cleaning , remove blank text and Nan values
    df['text'].replace('', np.nan, inplace=True)
    df.dropna(subset=['text'], inplace=True)
    df = df[df['text'].astype(bool)]

    # add sentament column
    df["sentiment"] = df.apply(lambda row: get_sentiment(row), axis=1)

    # output the sentament to a csv
    out_sentiment_file = f"{query}_twitter_with_sentiment.csv"
    out_sentiment_file = os.path.join(output_dir, out_sentiment_file)
    df.to_csv(out_sentiment_file, index=False)

    # get the percentage of positive vs negative and save in a csv
    username_series = df.groupby("username")["sentiment"].value_counts(normalize=True).mul(100).to_frame()

    out_sentiment__overview_file = f"{query}_sentiment_overview.csv"
    out_sentiment__overview_file = os.path.join(output_dir, out_sentiment__overview_file)
    username_series.to_csv(out_sentiment__overview_file)

    # Dataframes to print to screem
    overall_sentiment = df["sentiment"].value_counts()
    username_df = df["username"].value_counts()
    return username_df.head(10), overall_sentiment

