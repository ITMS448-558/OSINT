import sys,os,requests
import pandas as pd
import json
import matplotlib.pyplot as plt 
import files
import chicago
import datetime
def barh():
    df=pd.read_csv(files.chicagoData/('data.csv'))
    s = df[['primary_type']] #  get a series from data frame
    crime_count = pd.DataFrame(s.groupby('primary_type').size().sort_values(ascending=True).rename('counts'))
    data=crime_count # retrieving select rows by loc method

    print(data[::-1])

    data.plot(kind='barh')
    
    plt.subplots_adjust(left=0.33, right=0.89) 

    # Show graphic
    plt.show()

def weekRange():
    df=pd.read_csv(files.chicagoData/('data.csv'))
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(['primary_type', pd.Grouper(key='date', freq='1w')])\
       .sum()\
       .reset_index()\
       .sort_values('date')
    df['date']=df['date'].apply(lambda x: str(x).split(' ')[0])
    df['date']=df['date'].apply(lambda x: str(x).split('-')[0][2:]+'-'+str(x).split('-')[1]+'-'+str(x).split('-')[2])
    print (df['date'])
    s = df.groupby('date').size()
    s.plot(x='Crime Count',y='Weeks',title='Crimes per week',lw=3,label="Crimes")
    plt.legend()
    plt.show()


def monthRange():
    df=pd.read_csv(files.chicagoData/('data.csv'))
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(['primary_type', pd.Grouper(key='date', freq='1M')])\
       .sum()\
       .reset_index()\
       .sort_values('date')
    df['date']=df['date'].apply(lambda x: str(x).split(' ')[0])
    df['date']=df['date'].apply(lambda x: str(x).split('-')[0][2:]+'-'+str(x).split('-')[1]+'-')
    print (df['date'])
    s = df.groupby('date').size()
    s.plot(x='Crime Count',y='Month',title='Crimes per Month',lw=3,label="Crimes")
    plt.legend()
    plt.show()

def caughtPlot():
    df=pd.read_csv(files.chicagoData/('data.csv'))
    df=df[['primary_type','arrest']]
    free=df.loc[df['arrest'] == False]
    caught=df.loc[df['arrest'] == True]
    free= free.groupby('primary_type').size()
    caught= free.groupby('primary_type').size()
    caughtvsfree=pd.DataFrame((caught,free),index=('True','False'))
    print(caughtvsfree)
    caughtvsfree.plot(kind='barh')

    #df=df.groupby('primary_type').size().sort_values(ascending=True).rename('counts')
        
    plt.legend()
    plt.show()
    

# df=pd.pivot(index=['id'],columns=['date'],)
# df=df.rename(rows=lambda x: x[0].split('T')[0])
#  import matplotlib.pyplot as plt

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()

 