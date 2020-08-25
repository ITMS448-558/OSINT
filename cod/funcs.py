from bs4 import BeautifulSoup as bs  # importing BeautifulSoup
import os
import subprocess
import pandas as pd
import numpy as np
html=""
fpath="/home/trev/cod/bois/LowercaseOyster"

#reads fpath and returns a string of data to be parsed
#(data will be the html from website)
def readfile(fpath):
    with open(fpath,'r') as file:
        lines=file.readlines()
        data=""
        for line in lines:
            data = data+""+line
        return data

#upS stands for update Soup
def upS(file):
    soupObj=bs(file,features="lxml")
    return soupObj

#strip body of html
def stripBody(htmlData):
    soup=upS(htmlData)
    return str(soup.find('body'))

def updateStats(name):
    #Print current name
    print(name)
    #strip html to only have body
    data=stripBody(readfile(fpath))
    #soupify
    soup=upS(data)
    a=soup.find_all(attrs={'class':"name"})
    b=soup.find_all(attrs={'class':"value"})
    a=pd.Series(a[12:])
    b=pd.Series(b)
    c=pd.DataFrame([a,b]).transpose()
    myList=[]
    myList.append(['Gamertag',name])
    for i in range(len(c)):
        ca=upS(str([c[0][i]])).text[1:-1]
        cb=upS(str(c[1][i])).text
        myList.append([ca,cb])
        print(ca+"::"+ cb)
    return myList
    # print(myList)

    print(len(c))

def getKills():
    print("Kills")
    

def getDeaths():
    print("Deaths")


def getWins():
    print("Wins")

def update():
    print("start")
    os.system('cd ~/cod/bois; ~/cod/grab.sh')
    print("end")

# a=soup.title
# print(a)
# ######################
# a=pd.read_html(fpath,attrs={'class':"name"})
# # b=pd.read_html(fpath,attrs={'class':"value"})
# aa= pd.read_html(str(a))
# print(e)
# print(type(e))
# print(c)
# c = pd.Series(soup.findAll('div',{'class':'number'}))

# print(c)
# print(d)


#  a=bs(str(a))
# print(a.text)

# print(type(a))
# c = pd.Series(a)
# d = pd.Series(b)
# e= pd.Series([a[12:],b]).to_string
# e=bs(e,features="lxml")
# print(e)