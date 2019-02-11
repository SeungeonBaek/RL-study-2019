# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 12:23:14 2017

@author: seung eon
"""

x = 10

def foo():
    x = 20
    print('지역변수 x :',x)
    
foo()
print('전역변수 x :',x)

y = 10

def foo2():
    global y
    y = 20
    print('전역 변수를 사용하겠다고 global 선언한 y :',y)
    
foo2()
print('전역변수 y :',y)

