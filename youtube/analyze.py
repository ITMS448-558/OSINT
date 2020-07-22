import pandas as pd

def analyze(qs):
    a=pd.read_csv(("youtube_output/"+qs+".csv"))
    colName=""
    for col in a.columns:
        colName+=col+"--"
        #print(col)
    # print(a['etag'])
    result=a.groupby('snippet.channelTitle')['snippet.title'].nunique().sort_values(ascending=False)
    print(type(result))
    resultIndex=result.index.tolist()
    resultList=result.tolist()
    myList=[]
    for k,v in zip(resultIndex,resultList):
        myList.append([k,v])
    # for each in result:
    #     myList.append(result[result==each])
    # print(myList)
    return myList
