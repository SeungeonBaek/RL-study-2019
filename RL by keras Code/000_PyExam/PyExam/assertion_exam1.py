# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:38:36 2018

@author: seung eon
"""

x = int(input('3의 배수를 입력하세요: '))
assert x % 3 == 0, '3의 배수가 아닙니다.'
print(x)