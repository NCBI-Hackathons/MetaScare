# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:22:45 2018

@author: leblanckh
"""

import pandas as pd
#import numpy as np
import os
#import sys

#FileDirList = r"C:\Users\leblanckh\gitRepos\MetaScare\RePORTER_PRJ_C_FY2018"
#ProjectTop=r"C:\Users\leblanckh\gitRepos\MetaScare"
ProjectTop="/Users/leblanckh/gitProjects/MetaScare"

dirNameList = ["RePORTER_PRJ_C_FY2018", "RePORTER_PRJABS_C_FY2018"]
for Name in dirNameList:
    Dir = ProjectTop + "/" + Name
    os.chdir(Dir)
    FileList = os.listdir(Dir)

    #cool one-line for each to not make an intermediate list object
    df = pd.concat((pd.read_csv(File, encoding="ISO-8859-1") for File in FileList))
    #print (df.head())

    #write to csv in the MetaScare directory
    #os.chdir(r"C:\Users\leblanckh\gitRepos\MetaScare")
    os.chdir(ProjectTop)
    newFileName = Name + ".csv"
    df.to_csv(newFileName)
    print("Column Labels:")
    print(df.columns.values.tolist())
    print("Column Head:"
    print(df.head())
