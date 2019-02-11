# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 00:06:42 2018

@author: seung eon
"""

# Class로도 데코레이터를 만들 수 있다. 그 방법의 핵심은, 인스턴스를
# 함수처럼 호출하게 해주는 __call__ method의 구현이다.

class Trace:
    def __init__(self, func):
        self.func = func # init 메서드로 호출할 함수를 초깃값으로 받는다.
                         # 매개변수로 받은 함수를 속성으로 저장한다.
    def __call__(self):
        print(self.func.__name__, '함수 시작')
        self.func()
        print(self.func.__name__, '함수 끝')
        
@Trace
def hello():
    print('hello')
    
hello();

print()###########################################################

class Trace2:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        r = self.func(*args, **kwargs)
        
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        
        return r
    
@Trace2
def add(a ,b):
    return a + b

print(add(10, 20))
print(add(a=10, b=20))