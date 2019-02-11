# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:42:43 2018

@author: seung eon
"""

''' 이 코드를 Decorater를 통해서 구현할것임.
def hello():
    print('hello 함수 시작')
    print('hello')
    print('hello 함수 끝')
    
def world():
    print('world 함수 시작')
    print('world')
    print('world 함수 끝')
    
hello()
world()
'''

def trace(func):
    def wrapper():
        print(func.__name__,'함수 시작')
        func()
        print(func.__name__,'함수 끝')
    return wrapper

def hello():
    print('hello')
    
def world():
    print('world')
    
trace_hello = trace(hello)
trace_hello()

trace_world = trace(world)
trace_world()