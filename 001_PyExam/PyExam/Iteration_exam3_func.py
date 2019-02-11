# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:13:04 2018

@author: seung eon
"""
#iter 함수는 객체의 __init__ 메서드를 호출해준다.
it = iter(range(3))

#next는 객체의 __next__ 메서드를 호출해주는것과 똑같다.
print(next(it), end=' ')
print(next(it), end=' ')
print(next(it), end=' ')
# print(next(it), end=' ') 요소가 3개여서 StopIteration에러 발생

#iter의 사용법은 iter(호출가능한객체, 반복을끝낼값)입니다.
#이때, 반복을 끝낼 값은 sentinel입니다.

import random as r

it_r = iter(lambda : r.randint(0, 5), 2)
# 0부터 5까지가 랜덤하게 나오며, 2가 나오면 끝난다.
print(next(it_r), end=' ')

