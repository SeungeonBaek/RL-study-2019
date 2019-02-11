# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:37:30 2018

@author: seung eon
"""

# Class inheritance

class Person :
    def greeting(self):
        print('안녕하세요.')
        
class Student(Person):
    def study(self):
        print('공부하기')
        
james = Student()
james.greeting()
james.study()

print(issubclass(Student,Person))
# True로 나옴 왜냐하면 학생이 사람의 파생(derived)클래스 이므로.
# 이때, Person을 기반(base)클래스라고 한다.
print()

class Person2 :
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student2(Person2):
    def __init__(self):
        print('Student __init__')
        super().__init__()
# super()로 base class의 method인 init 호출
# 파생 클래스에도 __init__이 있기 때문에 super()로
# 호출을 안 해주면, 파생 클래스의 __init__만 실행됨ㅇㅇ
        self.school = '파이썬 코딩 도장'
        
james = Student2()
print(james.school)
print(james.hello)

