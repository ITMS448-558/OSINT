import sys,os
from socialreaper import YouTube
from socialreaper.tools import CSV
import numpy as np
import pandas as pd
import json
import youtube.api_key as ap

def run_youtube_click(qs,count=100):
    ytb =YouTube(ap.api_key)
    data=ytb.api.search(qs,count)
    # print(data)
    data=pd.Series(data)
    data=data['items']
    CSV(data, file_name='youtube_output/'+qs+'.csv')

def __init__():
    print("Do init things")

