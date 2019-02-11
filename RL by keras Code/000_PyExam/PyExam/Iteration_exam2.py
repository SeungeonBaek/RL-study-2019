# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:03:17 2018

@author: seung eon
"""

class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            
            r = self.current
            self.current += 1
            return r
        else :
            
            raise StopIteration
            
for i in Counter(5):
    print(i, end = ' ')