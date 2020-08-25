#! /usr/bin/env python
import sys
import os
import loginFile
import gui
root=""
top=""
def init(root, top):
    root=root
    top=top
    print("Start the engines on something I suppose")

def login(username,password):
    with open(loginFile.homeDir/('credentials.txt'))as file:
        lines=file.readlines()
        for line in lines:
            line=line.split(',')
            if(username==line[0]):
                if(password==line[1]):
                    gui.create_main(root)
        print("Wrong username or password")