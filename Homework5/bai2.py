# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:39:12 2016
"""

fhand = open(r'C:\Users\imucy_000\Desktop\HK1\Git\Python\Homework5\mbox-short.txt')
for line in fhand :
    words = line.split()
    if len(words) != 0 and words[0] == 'From' :
        try :
            print (words)
        except :
            print ('No data element at index sub-2')
            continue
    else :
        continue
    #in những line sau From