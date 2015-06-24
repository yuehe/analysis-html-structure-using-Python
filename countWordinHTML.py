# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:01:23 2015

@author: yhe
"""

#python 2.x
import urllib
import numpy as np
from bs4 import BeautifulSoup
import re
from collections import Counter
#%%%


#url1 = 'file:///C:/Users/yhe/Documents/Yue%20Interns/Task_6w_identifyKnowledgeGap/htmlTest/fafo.no_html5.html'
#url = 'file:///C:/Users/yhe/Documents/Yue%20Interns/Task_6w_identifyKnowledgeGap/htmlTest/utdanning.no_html40588.html'

def countWordinHTMLparagraph(url):
    
    # return the array as the number of "Effekt, resultat, virkning, Læreplass " (ignore upper)
    page =  urllib.urlopen(url).read() # read html file    
    soup = BeautifulSoup(page)
    #Effekt OR resultat OR virkning  + Læreplass
    #keyword='Læreplass' # doesnot work
    #keyword=u'Læreplass' #good!
    countArr = np.array([0,0,0,0])

    for i in range(len(soup.find_all('p'))): # only search keywords in paragraph
        w=soup.find_all('p')[i].get_text()
        word=w.split() # split into several words
        counter = Counter(word)
        count1 = counter[u'Effekt'] + counter[u'effekt']
        count2 = counter[u'Resultat'] + counter[u'resultat']
        count3 = counter[u'Virkning'] + counter[u'virkning']
        count4 = counter[u'Læreplass'] + counter[u'læreplass']
  
        count = np.array([count1,count2,count3,count4])
        countArr += count
  
    return countArr

def countWordinHTMLtitle(url):
    # in html, there is only ONE title attribute
    # return wether the word appear in title "Effekt, resultat, virkning, Læreplass " (ignore upper)
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    page = urllib.urlopen(url).read() # read html file    
    soup = BeautifulSoup(page)   
    titlelist = soup.find('title').string.split()
    if 'Effekt' in titlelist or 'effekt'in titlelist:        
        #print 'something, kw show in title'
        #print soup.find('title').string
        count1 = 1
    if 'Resultat' in titlelist or 'resultat'in titlelist:        
        #print 'something, kw show in title'
        #print soup.find('title').string
        count2 = 1    
    if 'Virkning' in titlelist or 'virkning'in titlelist:        
        #print 'something, kw show in title'
        #print soup.find('title').string
        count3 = 1
    if u'Læreplass' in titlelist or u'læreplass'in titlelist:
        #print 'something, kw show in title'
        #print soup.find('title').string
        count4 = 1
        
    tagArr = np.array([count1,count2,count3,count4])
    return tagArr
    
