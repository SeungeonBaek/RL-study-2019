# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 23:09:12 2018

@author: seung eon
"""
# 데코레이터는 매개변수와 반환값을 처리할 수도 있다. ㄷㄷ
def trace(func):
    def wrapper(a, b):
        r =  func(a, b)
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))
        return r
    return wrapper

@trace
def add(a, b):
    return a + b

print(add(10, 20)); print()

def trace2(func): # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs): # 가변 인수 함수로 만듦
        r = func(*args, **kwargs) # func에 args, kwargs를 Unpaacking하여 넣어줌.
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs,r))
        # 매개변수와 반환값 출력
        return r # func의 반환값을 반환
    return wrapper # wrapper 함수 반환

@trace2
def get_max(*args):
    return max(args)

@trace2
def get_min(**kwargs):
    return min(kwargs.values())

print(get_max(10, 20)); print()
print(get_min(x=10, y=20, z=30)); print()