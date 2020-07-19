import pandas as pd

def analyze(qs):
    a=pd.read_csv(("youtube_output/"+qs+".csv"))
    colName=""
    for col in a.columns:
        colName+=col+"--"
        print(col)
    # print(a['etag'])
    print (a.groupby('snippet.channelTitle')['snippet.title'].nunique())

analyze('funny')