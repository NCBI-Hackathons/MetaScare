# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:22:45 2018

@author: leblanckh
"""

import pandas as pd
#import numpy as np
import os
#import sys

FileDir = r"C:\Users\leblanckh\gitRepos\MetaScare\RePORTER_FY18"
os.chdir(FileDir)
FileList = os.listdir(FileDir)

#Simple Test with just 2 dataFrames
#frame1 = pd.read_csv(FileList[0], encoding="ISO-8859-1")
#frame2 = pd.read_csv(FileList[1], encoding="ISO-8859-1")
#dfList = [frame1, frame2]
#print("Point 3", dfList)
#df = pd.concat(dfList)

#cool one-line for each to not make an intermediate list object
df = pd.concat((pd.read_csv(File, encoding="ISO-8859-1") for File in FileList))
print (df.head())

#write to csv in the MetaScare directory
os.chdir(r"C:\Users\leblanckh\gitRepos\MetaScare")
df.to_csv("RePORTER_PRJ_C_FY2018.csv")