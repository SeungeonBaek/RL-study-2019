# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:33:34 2017

@author: seung eon
"""
# 클래스 이름의 첫자는 대문자, method의 첫 매개변수는
# 항상 self 빈 class를 만들 때는 pass를
class Maan:
    pass

class Person:
    def greeting(self):
        print('Hello')
    def hello(self):
        self.greeting()
# self.method() 형식으로 클래스 안의 메서드를 호출
 
James = Person()
James.hello()

# 특정 클래스의 instance인지 확인하기
print('James가 Person의 instance인가?:',isinstance(James, Person))