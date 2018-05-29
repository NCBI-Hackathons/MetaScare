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
#ProjectTop="/Users/leblanckh/gitProjects/MetaScare"
ProjectTop="//work/git_repos/MetaScare"
os.chdir(ProjectTop)

AbsDF = pd.read_csv("RePORTER_PRJABS_C_FY2018.csv")
PrjDF = pd.read_csv("RePORTER_PRJ_C_FY2018.csv")

#ComboDF = pd.DataFrame()
#UnMatchedDF = pd.DataFrame()

prjTitle_ComboList = []
prjNumber_ComboList = []
appID_ComboList = []
Abstract_ComboList = []

prjTitle_UnMatchedList = []
prjNumber_UnMatchedList = []
appID_UnMatchedList = []
Abstract_UnMatchedList = []


AppID_List=AbsDF['APPLICATION_ID'].tolist()
AppID_ListLen=len(AppID_List)
print ("The length of the AppID is", AppID_ListLen)
counter = 0

# loop over every Application ID in the full list of Application IDs (currently sourced from Abstract DF)
for AppID in AppID_List:
    #print ("Progress results Counter is ", counter, " out of AppID_ListLen ", AppID_ListLen, " .")
    counter+=1

    #set the *current* loopDF by filtering the PrjDF using the current AppID
    loopDF = PrjDF[PrjDF['APPLICATION_ID'] == AppID]

    #check if loopDF is empty. If yes, append matching AppID line into "Unmatched". If not, append entire loopDF into ComboDF 
    if (loopDF.empty) :
        tmpDF = AbsDF[AbsDF['APPLICATION_ID'] == AppID]
        tmpLen = len(tmpDF)
        if tmpLen >= 2:
            print ("!!!!! WARNING")
            print ("!!!!! WARNING")
            print ("!!!!! WARNING")
            print ("If we are printing this, then our data is not as nicely formatted as we hoped part 1.")
            print ("The length of the Abstract DF is ", tmpLen)
        else:
            #assume exactly 1 hit and format the desired UnMatched DF row
            prjTitle_UnMatchedList.append("NA")
            prjNumber_UnMatchedList.append(-999)
            appID_UnMatchedList.append(tmpDF.iloc[0]['APPLICATION_ID'])
            Abstract_UnMatchedList.append(tmpDF.iloc[0]['ABSTRACT_TEXT'])

            #fullRowDF = pd.DataFrame({'PROJECT_TITLE':[prjTitleValue], 'FULL_PROJECT_NUM':[prjNumberValue],
                        #'APPLICATION_ID':[appID_Value], 'ABSTRACT_TEXT':[Abstract_Value]})
            #print ("In UnMatched fullRowDF is ")
            #print (fullRowDF)

        #if counter%100 == 0:
            #print("No match")
            #print("About to append AbsDF AppID line into UnMatchedDF")
            #print(tmpDF)
        #UnMatchedDF.append(fullRowDF)
    else:
        loopDF_Len = len(loopDF)
        if loopDF_Len >= 2:
            print ("!!!!! WARNING")
            print ("!!!!! WARNING")
            print ("!!!!! WARNING")
            print ("If we are printing this, then our data is not as nicely formatted as we hoped part 2.")
            print ("The length of the loop DF is ", loopDF_Len)
        else:
            #assume exactly 1 hit and format the desired Combo DF row
            tmpDF = AbsDF[AbsDF['APPLICATION_ID'] == AppID]

            prjTitle_ComboList.append(loopDF.iloc[0]['PROJECT_TITLE'])
            prjNumber_ComboList.append(loopDF.iloc[0]['FULL_PROJECT_NUM'])
            appID_ComboList.append(loopDF.iloc[0]['APPLICATION_ID'])
            Abstract_ComboList.append(tmpDF.iloc[0]['ABSTRACT_TEXT'])

            #fullRowDF = pd.DataFrame({'PROJECT_TITLE':[prjTitleValue], 'FULL_PROJECT_NUM':[prjNumberValue],
                        #'APPLICATION_ID':[appID_Value], 'ABSTRACT_TEXT':[Abstract_Value]})
            #print ("In Combo fullRowDF is ")
            #print (fullRowDF)

        #if counter%100 == 0:
            #print("Matched!")
            #print("About to append loopDF into Combo")
            #print(loopDF)
        #ComboDF.append(fullRowDF)
#fullRowDF = pd.DataFrame({'PROJECT_TITLE':[prjTitleValue], 'FULL_PROJECT_NUM':[prjNumberValue],
            #'APPLICATION_ID':[appID_Value], 'ABSTRACT_TEXT':[Abstract_Value]})

#make sure to use the columns parameter to the constructors to prevent alphabetizing the columns
UnMatchedDF = pd.DataFrame({'PROJECT_TITLE':prjTitle_UnMatchedList, 'FULL_PROJECT_NUM':prjNumber_UnMatchedList,
             'APPLICATION_ID':appID_UnMatchedList, 'ABSTRACT_TEXT':Abstract_UnMatchedList}, 
             columns=['PROJECT_TITLE', 'FULL_PROJECT_NUM', 'APPLICATION_ID', 'ABSTRACT_TEXT'])

ComboDF = pd.DataFrame({'PROJECT_TITLE':prjTitle_ComboList, 'FULL_PROJECT_NUM':prjNumber_ComboList,
             'APPLICATION_ID':appID_ComboList, 'ABSTRACT_TEXT':Abstract_ComboList},
             columns=['PROJECT_TITLE', 'FULL_PROJECT_NUM', 'APPLICATION_ID', 'ABSTRACT_TEXT'])

print("The Combo project Title list length is", len(prjTitle_ComboList))
print("The first 5 of Combo project Title list is")
print(prjTitle_ComboList)
print("The Combo project Number list length is", len(prjNumber_ComboList))
print("The first 5 of Combo project Number list is")
print(prjNumber_ComboList)
print("The Combo appID list length is", len(appID_ComboList))
print("The first 5 of Combo application ID list is")
print(appID_ComboList)
print("The Combo Abstract list length is", len(Abstract_ComboList))
print("The first 5 of Combo Abstract list is")
print(Abstract_ComboList)

print("The UnMatched project Title list length is", len(prjTitle_UnMatchedList))
print("The first 5 of UnMatched project Title list is")
print(prjTitle_UnMatchedList)
print("The UnMatched project Number list length is", len(prjNumber_UnMatchedList))
print("The first 5 of UnMatched project Number list is")
print(prjNumber_UnMatchedList)
print("The UnMatched appID list length is", len(appID_UnMatchedList))
print("The first 5 of UnMatched application ID list is")
print(appID_UnMatchedList)
print("The UnMatched Abstract list length is", len(Abstract_UnMatchedList))
print("The first 5 of UnMatched Abstract list is")
print(Abstract_UnMatchedList)

#print ("The ComboDF is")
#print (ComboDF)
#print ("The UnMatchedDF is")
#print (UnMatchedDF)

#write to csv in the MetaScare directory
os.chdir(ProjectTop)
newFileName = "SimpleJoin.tsv"
df = ComboDF.append(UnMatchedDF)
df.to_csv(newFileName, sep="\t")
    
