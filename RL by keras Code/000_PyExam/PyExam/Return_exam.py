# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 02:09:41 2017

@author: seung eon
"""

def not_ten(a):
    if a == 10:
        return
    print(a, '입니다.', sep=' ')
    
'''
5를 넣으면 함수안의 print 문이 실행됨
10을 넣으면 retrun으로 인해 함수를 빠져나와서 print가
실행이 되지 않음.
'''

def add_sub(a,b) : # return을 두개로 해서 unpacking까지
#    return a + b, abs(a - b)
#    return (a+b,abs(a-b))
    return [a+b,abs(a-b)]
x,y = add_sub(10,20)

print('x는 10과 20의 합인',x,'임')
print('y는 10과 20의 차인',y,'임')