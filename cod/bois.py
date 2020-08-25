# importing the requests library
from bs4 import BeautifulSoup as bs  # importing BeautifulSoup
import pandas as pd
import os
import subprocess
import funcs as fu

fpath = ""
bois = 'Alabork', 'Warr1oR54', 'RothBane', 'Besttriggrman', 'Pinoguido10', 'duckbutter1887', 'PAYTON-THIRTY4', 'X_iceWolf_X1134', 'sturdyHawg0704', 'rjamesb007', 'LowercaseOyster'


def main():
    # Make files if not there
    for name in bois:
        changeFile(name)
        checkFile()
    #Update htmls
    #fu.update()
    for name in bois:
        print('\n\n\n-------------------------------------------------------')
        myList=fu.updateStats(name)

def changeFile(tag):
    global fpath
    filepath = os.path.dirname(__file__)  # <-- absolute dir the script is in
    filepath += "/bois/"+tag+''
    fpath = filepath

def checkFile():
    if not os.path.exists(fpath):    
        open(fpath,'a').close()
        print("Made file")
    else:
        print("File Exist")

if __name__ == '__main__':
    main()
    print("All done!")
