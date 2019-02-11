# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 10:18:35 2017

@author: seung eon
"""

def hello(count) :
    if count==0:
        return
    
    print('Hello, world!',count)
    
    count-=1
    hello(count)
    
hello(5)

def factorial_real(num) :
        
    if num==1:
        return 1
    
    num -=1
    return (num+1) *factorial_real(num)
    
print(factorial_real(4))