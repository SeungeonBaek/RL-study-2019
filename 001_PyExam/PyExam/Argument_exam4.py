# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:07:52 2017

@author: seung eon
"""
# 이때, 가변 매개변수는 고정 매개변수보다 뒤에 있어야한다.
def personal_info3(name, **kwargs):
    print(name)
    print(kwargs)
    
personal_info3('홍길동')
personal_info3('홍길동',age=30,adress='서울시 용산구 이촌동')

