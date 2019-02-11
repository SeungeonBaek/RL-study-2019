# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:57:46 2018

@author: seung eon
"""

class A:
    def greeting(self):
        print('안녕하세요. ACE Lab신입생 입니다.')
        
class B(A):
    def greeting(self):
        print('안녕하세요. ACE Lab 11월 신입생 입니다.')
        
class C(A):
    def greeting(self):
        print('안녕하세요. ACE Lab 1월 신입생 입니다.')
        
class D(B, C): # <=이렇게 여러개의 기반클래스를
    # 상속 받는 경우를 다중 상속이라고 한다 땅땅땅
    pass # 빈 클래스를 생성하는 방법임 pass ㅇㅅㅇ
    
seung_eon = D()
seung_eon.greeting()

print(D.mro())
# 이걸 실행해 보면, D다음 B -> C -> A의 순으로
# method를 탐색한다. 그래서 B의 greeting이 호출된다.
# 너무 어려운데...

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
        
    @abstractmethod
    def go_to_school(self):
        pass
    
class Student(StudentBase):
    def study(self):
        print('공부하기')
    
    def go_to_school(self):
        print('학교가기')
        
seung_eon = Student()
seung_eon.study()
seung_eon.go_to_school()

# 추상 클래스는 상속을 위한 용도로만 사용된다.
# 추상 클래스의 method들은 따로 호출될 일이 없으므로
# pass만 넣어서 빈 method를 만들면 되고, 파생 클래스는
# 무조건 추상 method를 구현해야 한다.