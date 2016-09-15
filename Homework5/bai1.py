# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:08:42 2016

"""
list = [1, 2, 3, 4, 5, 6, 7]

def chop(t) :
    del t[0]
    del t[-1]

# print results
print( "The original list:", list)
print( "The value returned by the 'chop' function:" , chop(list))
print( "The modified list resulting from the 'chop' function: " , list)
