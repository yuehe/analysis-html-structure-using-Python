# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:19:53 2015
based on the rules (and or), finding the docID who meets them
@author: yhe
"""

import os, sys
import pandas as pd

def AndTwo(tdf,A,B):

    outp = tdf[['docname','keywords']]
    print 'The total docments number in the database is:%d' %len(outp)
    p1 = outp[outp['keywords']==A]
    d1 = set(p1['docname']) 
    print 'There are %d docments contain word:' %len(d1), A
    #print len(d1)    
    p2 = outp[outp['keywords']==B]
    d2 = set(p2['docname'])
    print 'There are %d docments contain word:' %len(d2), B
    re=d1.intersection(d2)
    print 'There are %d docments contain ALL of these words:' %len(re), A,B
    return re
    
def AndThree(tdf,A,B,C):
    re = AndTwo(tdf,A,B)
    outp = tdf[['docname','keywords']]
    p3 = outp[outp['keywords']==C]
    d3 = set(p3['docname'])
    print 'There are %d docments contain word:' %len(d3), C
    re=re.intersection(d3)
    print 'There are %d docments contain ALL of these words:' %len(re), A,B,C
    return re        

    
def orOne(tdf, A):
    outp = tdf[['docname','keywords']]
    p1 = outp[outp['keywords']==A]
    d1 = set(p1['docname'])
    return d1    
    
def orTwo(tdf,A,B):
    outp = tdf[['docname','keywords']]
    d1 = orOne(tdf, A)
    p2 = outp[outp['keywords']==B]
    d2 = set(p2['docname'])
    re=d1.union(d2)
    return re

def orThree(tdf,A,B,C):
    outp = tdf[['docname','keywords']]
    d1 = orTwo(tdf, A,B)
    p3 = outp[outp['keywords']==C]
    d3 = set(p3['docname'])
    re=d1.union(d3)
    return re    



