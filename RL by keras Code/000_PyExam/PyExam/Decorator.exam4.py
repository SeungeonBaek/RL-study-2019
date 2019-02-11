# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 23:25:45 2018

@author: seung eon
"""

# method에 Decorator를 사용하기도 한다
def trace3(func):
    def wrapper(self, a, b):
        
        r = func(self, a, b)
        print('{0}(a={1}, b={2}) ->{3}'.format(func.__name__,a, b, r))
        
        return r
    return wrapper

class Calc:
    @trace3
    def add(self, a, b):
        return a + b

c = Calc()
print(c.add(10,20))

# 매개변수가 있는 데코레이터 만들기
def is_multiple(x):
    def real_decorator(func):
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else :
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_decorator
# 매개변수가 있는 데코레이터를 만들 때는 함수를 하나 더 만들어야 합니다.
# is_multiple 함수를 만들고, 데코레이터가 사용할 매개변수 x를 지정합니다.
# 그리고 is_multiple 함수 안에서 실제 데코레이터 역할을 하는 real_decorator를 만듭니다.
# FInally is_multiple안에서 실제 decorator역할을 하는 real_decorator를 전과 같이 만들면 뚝딱~
@is_multiple(3)
def add(a, b):
    return a + b

print(add(10, 20))
print(add(2, 5))