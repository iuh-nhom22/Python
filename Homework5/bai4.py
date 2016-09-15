# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:12:46 2016

"""
fhand = open(r'C:\Users\imucy_000\Desktop\HK1\Git\Python\Homework5\mbox-short.txt')
count = 0
for fh in fhand :
    words = fh.split()
    if len(words) != 0 and words[0] == 'From' :
        print (words[1])
        count=count+1
        
print ("There were" , count, "lines in the file with From as the first word")      
