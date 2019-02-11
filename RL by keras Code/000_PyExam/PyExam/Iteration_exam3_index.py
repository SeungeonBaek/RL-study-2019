# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:10:51 2018

@author: seung eon
"""

class Counter:
    def __init__(self, stop):
        self.stop = stop
        
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else :
            raise IndexError
    
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end = ' ')

#get item메서드를 이용하여 인덱스로 접근 가능한 이터레이션 생성