# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 12:28:04 2017

@author: seung eon
"""
#함수 안에서 함수를 만들어 보자
def calc():
    total = 0
    def add(a, b) :
        nonlocal total
        total = total+a+b
        
    add(10, 20)
    add(30, 40)
    print(total)
        
calc()

# nonlocal은 현재 함수의 지역 변수가 아니라는 뜻이며,
# 바깥 함수의 지역 변수를 사용합니다.
# 매개변수도 함수안에서만 사용할 수 있는 지역 변수이므로
# nonlocal을 통해 이용해야 합니다.

def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
A()

# nonlocal은 함수 바깥의 지역 변수를 찾을 때 가까운
# 함수부터 먼저 찾는다. A와 B의 지역변수 중 B의 지역
# 변수 x를 참조하는 이유이다.