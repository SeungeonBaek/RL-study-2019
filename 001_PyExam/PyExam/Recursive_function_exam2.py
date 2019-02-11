# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 10:36:45 2017

@author: seung eon
"""
import math as m
def is_palindrome(word):
    
    if len(word)<2:
        return True
    elif word[0]==word[-1]:
        return is_palindrome(word[1:-1])
    else :
        return False
    
print('회문입니까? :',is_palindrome('asasa'))

def Fibonacci_series(num):
    
    if num<1 or num-m.floor(num)!=.0:
        return ValueError('자연수를 입력하시오')
    elif num==1:
        return 1
    else :
        return num+Fibonacci_series(num-1)

print('피보나치 수열의 값 :',Fibonacci_series(2.3))