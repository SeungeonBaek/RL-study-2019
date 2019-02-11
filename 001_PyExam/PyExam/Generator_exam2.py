# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:41:10 2018

@author: seung eon
"""

def num_gen():
    x = [1, 2, 3]
    for i in x :
        yield i
        
def num_gen2():
    x = [1, 2, 3]
    yield from x
    
for i in num_gen():
    print(i, end = ' ')
print()
for i in num_gen2():
    print(i, end = ' ')