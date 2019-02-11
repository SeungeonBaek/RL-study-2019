# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:58:15 2018

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

@trace #Decorater
def hello():
    print('hello')
@trace #Decorater
def world():
    print('world')
    
hello(); world(); print()

def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper

@decorator1 #Decorator는 다중으로 사용이 가능하다.
@decorator2 #그때, 실행 순서는 위에서 아래이다. ^^
def hello2():
    print('hello2')

hello2()

# @를 사용하지 않는다면, 위의 코드는 다음과 같다고 할 수 있다.
'''
decorated_hello = decorator1(decorator2(hello))
decorated_hello() # 가독성 지렸쥬?
'''