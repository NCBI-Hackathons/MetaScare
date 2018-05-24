# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:22:45 2018

@author: leblanckh
"""

import pandas as pd
import numpy as np
import os
import sys

FileDir ="C:/Users/leblanckh/Downloads/ExPORTER_CSVs_2011to2018/RePORTER_FY18"
os.chdir(FileDir)
FileList = os.listdir(FileDir)
#frame = pd.DataFrame()
#dfList = []

df = pd.concat((pd.read_csv(File) for File in FileList))
print (df.head())