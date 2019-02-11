# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:50:36 2018

@author: seung eon
"""

# Class에서 Method overriding 사용하기. overriding은 무시하다,
# 우선하다 라는 뜻을 가지고 있고, 기반 클래스의 method를 무시하고
# 새로운 method를 만든다는 뜻입니다.

class Person:
    def greeting(self):
        print('안녕하세요.')
        
class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 ACE Lab Freshman입니다.')
        
james = Student()
james.greeting()

# Person의 greeting이 무시됨 혹은 파생 클래스의 greeting이 우선됨.
# 이를 해결하기 위하여!

class Person2:
    def greeting(self):
        print('안녕하세요.')
        
class Student2(Person2):
    def greeting(self):
        super().greeting()
        print('저는 ACE Lab Freshman입니다.')
        
seungeon = Student2()
seungeon.greeting()

# super().greeting()을 통해 기반 클래스의 greeting 실행
# 그 후, Student2의 greeting실행하여 원래기능을 이용해
# 새로운 기능을 만들 수 있다.


