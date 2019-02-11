# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 09:27:30 2018

@author: seung eon
"""

class Person :
    
    luggage_bag= [] # Class 속성
    
    def __init__(self):
        self.bag = [] # Instance 속성
        
    def put_bag(self, stuff):
        self.bag.append(stuff)
        Person.luggage_bag.append(stuff)
        
james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('여권')

print('james의 가방:',james.bag)
print('jaems의 수화물 가방:',james.luggage_bag)
print('maria의 가방:',maria.bag)
print('maria의 수화물 가방:',maria.luggage_bag)
