# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 11:20:33 2017

@author: seung eon
"""

def plus_ten(x):
    return x+10

y = list(map(plus_ten,[1, 2, 3]))
print('map을 이용하여 함수에 리스트 입력:',y)

y2 = list(map(float,[1,2,3]))
print('map을 이용하여 리스트안의 값을 float으로 변형:',y2)

y3 = list(map(lambda x: x+10, [1, 2, 3]))
print('map을 통해 lambda를 이용한 함수식에 리스트 입력:',y3)
# lambda에 매개변수를 지정하고, :(콜론)뒤에 반환 값을 지정.
# lambda 표현식 자체가 함수로 동작할 뿐 이름이 없어서,
# Anonymous function 즉, 익명함수라고도 부름.
# 만약 함수 이름이 필요하다면 다음과 같이 해라

f = lambda x: x+10
y4 = list(map(f, [1, 2, 3]))
print('map을 통해 f에 리스트 입력:',y4)

y5 = (lambda x : x**2)(3)
print('lambda 표현식 자체를 호출 가능:',y5)

'''
람다로 매개변수가 없는 함수를 만들때는 lambda 뒤에 아무것도
지정하지 않고 :(콜론)을 붙인다. 단, 콜론 뒤에는 반드시 반환
값이 있어야 한다.
'''

y6 = (lambda : 1)()
print('매개변수가 없고, 출력이 1:',y6)

t = 10
y7 = (lambda : t)()
print('매개변수가 없고, 출력이 외부변수 t:',y7)