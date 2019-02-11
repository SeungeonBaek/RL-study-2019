# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:33:02 2018

@author: seung eon
"""
# range 같은 역할을 해주는 제너레이터
def num_generator(stop):
    n = 0
    while n < stop :
        yield n
        n += 1
        
for i in num_generator(int(input('숫자너바라 '))):
    print(i)

print()

def upper_generator(string):
    for i in string:
        yield i.upper()

fruits = ['apple', 'grape', 'banana', 'melon']

for i in upper_generator(fruits):
    print(i)