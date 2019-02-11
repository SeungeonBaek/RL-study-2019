# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:05:50 2018

@author: seung eon
"""

"""
try :
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print (y)

except :
    print('예외가 발생했습니다.')
"""

try :
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x

except Exception as e :
    print(e)
    
else :
    print(y)
    
finally :
    print('코드 실행이 끝났습니다.')