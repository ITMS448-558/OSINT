import pandas as pd

def analyze_tweets():

    df = pd.read_csv(
        "twitter_output.csv"
    )


    data = df['username'].value_counts().head(10)
    #result = pd.DataFrame(data, columns=['Username', 'Count'])
    return data

