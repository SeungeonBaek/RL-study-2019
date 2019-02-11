# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:08:25 2017

@author: seung eon
"""

def calc():
    a = 3 ; b = 5
    def mul_add(x):
        return a*x + b
    return mul_add

c = calc()
print(c(1), c(2), c(3), c(4), c(5))

# 함수 calc가 끝났는데도 c는 calc의 지역변수 a,b를
# 사용해서 계산을 하고있다. 이렇게 함수를 둘러싼 환경
# (지역변수, 코드 등)을 계속 유지하다가, 함수를 호출할
# 때 다시 꺼내서 사용하는 함수를 closure라고 한다.
# c에 저장된 ax+b라는 함수가 closure이다.

def calc():
    a = 3
    b = 5
    return lambda x : a*x + b

c = calc()
print('lambda로 closure 만들기',c(1), c(2), c(3), c(4), c(5))

def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x) :
        nonlocal total
        total = total + a*x + b
        print('closure의 결과를 calc의 지역변수 total에 누적',total)
    return mul_add

c = calc()
c(1); c(2); c(3)