# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:18:17 2016

"""

fhand = open(r'C:\Users\imucy_000\Desktop\HK1\Git\Python\Homework5\mbox-short.txt')
numb = []
avg = 0
count = 0
for fh in fhand :
    words = fh.split()
    if len(words) != 0 and words[0] == 'X-DSPAM-Confidence:' :
        numb.append(words)
for num in numb : 
    a = float(num[1])
    avg = avg + a
    count = count+1
    
print('Average spam confidence: ',avg/count)