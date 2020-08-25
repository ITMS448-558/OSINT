import sys,os,requests
import pandas as pd
import json
import files
#Default values provided by Prof James
def pullData(chicago_query):

    # Base url for Chicago Open Data Portal crime API; plus addin of date and location filters
    baseurl = "https://data.cityofchicago.org/resource/w98m-zvie.json"

    datebetw = "?$where=date between '"+chicago_query['start_date']+"' and '"+chicago_query['end_date']+"'"

    # syntax for below filter is  'within_box(location_col, NW_lat, NW_long, SE_lat, SE_long)'
    boxurl = 'within_box(location, '+chicago_query['latnw']+', '+chicago_query['longnw']+','+\
                 chicago_query['latse']+',' +chicago_query['longse']+')'

    # Create the overall URL to interogate API with our data and location filters
    ourl = baseurl + datebetw + ' AND ' + boxurl
    
    text =  requests.get(ourl).json()

    # create pandas dataframe dictionary container object 
    df = pd.DataFrame(text)
    dataCSV=df.to_csv()
    with open(files.chicagoData/('data.csv'),'w') as f:
        f.write(dataCSV)
    print(df)
