# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:16:25 2018

@author: seung eon
"""

try :
    x = int(input('3의 배수를 입력하세요 : '))
    if x % 3 !=0:
        raise Exception('3의 배수를 입력하라고')

except Exception as e :
    print('? 예외가 발생했는데;',e)

else :
    print(x,'은(는) 3의 배수가 맞습니다.')