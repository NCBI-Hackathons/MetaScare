# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:22:45 2018

@author: leblanckh
"""

import pandas as pd
#import numpy as np
import os
#import sys

#If on Windows, switch ProjectTop
#ProjectTop=r"C:\Users\leblanckh\gitRepos\MetaScare"
ProjectTop="/Users/leblanckh/gitProjects/MetaScare"
os.chdir(ProjectTop)

AbsDF = pd.read_csv("RePORTER_PRJABS_C_FY2018.csv")
PrjDF = pd.read_csv("RePORTER_PRJ_C_FY2018.csv")

ComboDF = pd.DataFrame()
UnMatchedDF = pd.DataFrame()

for AppID in AbsDF['APPLICATION_ID'].tolist():
    loopDF = PrjDF[PrjDF['APPLICATION_ID'] == AppID]
   #check if loopDF is empty. If yes, append matching AppID line into "Unmatched". If not, append entire loopDF into ComboDF 
    

#write to csv in the MetaScare directory
os.chdir(ProjectTop)
newFileName = Name + ".csv"
df.to_csv(newFileName)
    
