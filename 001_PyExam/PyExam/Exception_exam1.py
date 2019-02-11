# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:40:30 2018

@author: seung eon
"""

#지금까지 Exception에 예외 메시지를 넣어서 예외를 발생시켜 왔지요?
#이번에는 예외를 직접 만들어보겠습니다. 그 방법은, Exception을 상속받아서
#새로운 '예외' 클래스를 만드는 것입니다. 그 다음, __init__ 메서드에
#기반 클래스인 Exception의 __inin__메서드를 호출 후 에러 메시지를 넣는것입니다.

class NotThreeMultipleError(Exception) :
    def __init__(self):
        super().__init__('3의 배수가 아닌데....')
        
def three_multiple():
    try :
        x = int(input('3의 배수를 입력해줘! '))
        if x % 3 != 0:
            raise NotThreeMultipleError
            
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.',e)
        
three_multiple()