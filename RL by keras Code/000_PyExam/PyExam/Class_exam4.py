# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 09:33:26 2018

@author: seung eon
"""

class Calc :
    # instance를 통하지 않고 클래스에서 바로 호출 가능
    @staticmethod 
    def add(a, b):
        print(a + b)
        
    @staticmethod
    def mul(a,b):
        print(a * b)
    
Calc.add(10, 20)
Calc.mul(10, 20)

class Person():

    count = 0
    
    def __init__(self):
        Person.count += 1
    # 인스턴스가 만들어질 때 class 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))
    # cls로 class속성에 접근
    
james = Person()
maria = Person()

Person.print_count()