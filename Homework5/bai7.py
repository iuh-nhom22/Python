# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:20:40 2016

"""
fhand = open(r'C:\Users\imucy_000\Desktop\HK1\Git\Python\Homework5\mbox-short.txt')
t=[]
for fh in fhand :
    words = fh.split()
    if len(words) != 0 and words[0] == 'From' :
        w = words[5].split(':')
        t.append(w[0])
        y = words[4]
print(t,' ',y,"\n")