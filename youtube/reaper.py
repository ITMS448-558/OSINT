from socialreaper import YouTube
from socialreaper.tools import CSV
import numpy as np
import pandas as pd
import json
ytb =YouTube("AIzaSyBh6WwHBJOmhisBGrDHR6RAhluxIFqsWsw")
data=ytb.api.search("funny",count=10)
# print(data)
data=pd.Series(data)
data=data['items']
CSV(data, file_name='funny.csv')