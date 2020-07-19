import sys,os
from socialreaper import YouTube
from socialreaper.tools import CSV
import numpy as np
import pandas as pd
import json

def run_youtube_click(qs,count=100):
    ytb =YouTube("AIzaSyBArtqQgXKbv4SxG6sWqWYpy1xBN-7ToRo")
    data=ytb.api.search("funny",count)
    # print(data)
    data=pd.Series(data)
    data=data['items']
    CSV(data, file_name='youtube_output/'+qs+'.csv')

def __init__():
    print("Do init things")

