# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:38:59 2017

@author: seung eon
"""

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        #hello등이 바로 class의 속성이다.
        self.name = name
        self.age = age
        self.address = address
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
        
James = Person('제임스', 24, '뚝섬')
James.greeting()
# James가 인스턴스 이다.