# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 07:59:43 2017

@author: seung eon
"""

# argument 즉 인수에 대해

def personal_info(name, age, address) :
    print('이름', name)
    print('나이', age)
    print('주소', address)
    
personal_info('홍길동', 30, '서울시 용산구 이촌동')
# 이렇게 순서를 지켜서 쓰지 않으면 안되는거 빡침
print()
personal_info(address='뚝섬', name='백승언', age=24)
# 이렇게 하면 순서를 지키지 않아도 된다
print()

x = {'name' : '임유림', 'address' : '소사', 'age' : 23}
personal_info(**x); print(1)
#딕셔너리 언패킹을 위해서는 함수의 매개변수 이름과 딕셔너리의
#키 이름이 같아야 하며, 둘의 개수 또한 같아야 한다.
#애스터리스크 *을 두개 쓰는건, 키-값 쌍 중 값을 참조하기 위함이다.

def personal_info2(**kwargs) :
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep=' ')
        
personal_info2(**x); print(2)
personal_info2(**{'이름' : '백장원', '나이' : 22, '주소' : '계산동'})