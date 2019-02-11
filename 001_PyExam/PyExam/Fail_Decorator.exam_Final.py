# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 00:21:13 2018

@author: seung eon
"""
"""
class IsMultiple:
    def __init__(self, x):
        self.x = x
    
    def __call__(self, func):
        def wrapper(a, b):
            r = func(a, b)
            if r % self.x == 0:
                print('{0}의 반환 값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            else :
                print('{0}의 반환 값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r
        return wrapper

@IsMultiple(3)
def add(a, b):
    return a + b

print(add(10, 20))
print(add(2, 5))
"""
# type_check는 함수의 매개변수가 지정된 자료형(클래스)이면 함수를
# 정상적으로 호출하고, 지정된 자료형과 다르면 RuntimeError 예외를
# 발생시키면서, '자료형이 다릅니다.'라는 에러메세지를 출력해야 합니다.
# 여기서 type_check에 지정된 첫 번째 int는 호출할 함수에서 첫 번째 매개
# 변수의 자료형을 뜻하며, 두 번째 int는 호출할 함수에서 두 번째 매개
# 변수의 자료형을 뜻합니다.

def type_check(type_a, type_b):
    def real_decorator(func):
        def wrapper(a, b):
            try :
                if (type(a) is type_a) and (type(b) is type_b) :
                    return func(a + b) #
                else :
                    raise RuntimeError('자료형이 올바르지 않음')
            except Exception as e:
                print(e)
        return wrapper
    return real_decorator #

@type_check(int, int)
def add(a, b):
    return (a + b)

print(add(10, 20))
print(add('hello', 'world'))