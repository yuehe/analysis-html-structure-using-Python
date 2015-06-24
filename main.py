# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:54:19 2015

@author: yhe
"""
# python 2.x
from __future__ import print_function # must to be the first import
import os, sys
import pandas as pd
import countWordinHTML
import SearchBasedRules

#%%
path =r'C:\Users\yhe\Desktop\week6 - NO.webcrawling\csv folder-html' # the folder store the csv
dirs =  os.listdir(path) # Return a list containing the names of the entries in the directory given by path.

str1='C:\Users\yhe\Desktop\week6 - NO.webcrawling\csv folder-html\\' # the string store the csv
header_row=['webpage','docname','keywords','time', 'time2', 'source'] 
k=0
foldername = ["nokut.no","ntnu.no","regjeringen.no","sintef.no","udir.no","ung.no","utdanning.no","vox.no"]
#foldername = ["fafo.no","fagskolen.info","fagskolene.no",	"gnistweb.no","ks.no",	"lanekassen.no",	"mittyrke.no","nifu.no","nito.no","nmbu.no","nokut.no","ntnu.no","regjeringen.no","sintef.no","udir.no","ung.no","utdanning.no","vox.no"]

for file in dirs:

    location = str1+file
    df = pd.read_csv(location, names=header_row)

    
    ## 17/04    
    # Rule: effekt OR resultat OR virkning  OR Rekruttering
    outp = df[['docname','keywords']]
    re1 = SearchBasedRules.orThree(df,'Resultat','Virkning','Effekt')
    re2 = SearchBasedRules.orOne(df, 'Rekruttering')
    re=re1.intersection(re2)

    l = list(re)
    #urlhead = 'file:///C:/Users/yhe/Documents/Yue%20Interns/Task_6w_identifyKnowledgeGap/' # the folder stored html
    urlhead = 'file:///F:/Backup/studies/' # the folder stored html
    folder = urlhead + foldername[k] + '.html/'+ foldername[k] + '.html/'
    
    if len(l)>0:
        result = ''
        if foldername[k] == 'nokut.no': #F**K, original is wrong!
            
            for i in range(len(l)):
                newl = l[i].replace('nokut','vox')
                url = folder + newl + '.html'
                arr = countWordinHTML.countWordinHTMLparagraph(url)
                tagArr = countWordinHTML.countWordinHTMLtitle(url)
                result += l[i] + '.html  ' + str(arr) +' , '+ str(tagArr) + '\n'
                    
            outputname = foldername[k]+'.txt'        
            file = open(outputname, "w")
            file.write(result)        
            file.close()
            print(foldername[k] + "write file done")
            
            
        else:
                    
            for i in range(len(l)):
                url = folder + l[i] + '.html'
                arr = countWordinHTML.countWordinHTML(url)
                tagArr = countWordinHTML.WordinHTMLtitle(url)
                result += l[i] + '.html  ' + str(arr) +' , '+ str(tagArr) + '\n'
                    
            outputname = foldername[k]+'.txt'        
            file = open(outputname, "w")
            file.write(result)        
            file.close()
            print(foldername[k] + "write file done")
    k=k+1


print('Done')
