# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 02:54:08 2017

@author: seung eon
"""

# argument 즉 인수에 대해

# 
def print_numbers2(*args):
    for arg in args:
        print(arg,end = ' ')
        
print('입력이 두개여도 걍가능')
print_numbers2(10,20); print(); print()

print('입력이 네개여도 걍가능')
print_numbers2(10,20,30,40); print(); print()

def print_numbers3(a, *args):
    print(a, end = ' ')
    print(args)

print('이거 잘봐둬1')    
print_numbers3(1); print()

print('이거 잘봐둬2')    
print_numbers3(1,10,20); print()

print('이거 잘봐둬3')    
print_numbers3(*[1, 10, 20]); print()