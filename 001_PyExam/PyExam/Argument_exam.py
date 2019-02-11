# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 02:47:34 2017

@author: seung eon
"""

#argument 즉 인수에 대해

def print_numbers(a,b,c):
    print(a,end=' ')
    print(b,end=' ')
    print(c)

print('그냥 넣은거'); print_numbers(10,20,30)

x = [10, 20, 30]

print('\n애스터리스크 *을 이용해 넣은거')
print_numbers(*x)

print('\n애스터 리스크*을 이용해 이렇게도 넣음')
print_numbers(*[10, 20, 30])
