# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 11:34:45 2017

@author: seung eon
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = list(map(lambda x : str(x) if x % 3 == 0 else x, a))

# 1. lambda 안에서 if를 쓸때는 콜론을 붙이지 말아야 한다.
# 2. lambda 안에서 if를 쓰면 else를 사용해야만 한다.
# 3. lambda 안에서 if를 쓸 때, elif는 사용하지 못 한다.
print(x)

b = [1, 2, 3, 4, 5]; c = [2, 4, 6, 8, 10]

prod = list(map(lambda x, y : x*y, a, c))
print(prod)

from random import random as r

d = [int(r()*10) for i in range(10)]
e = list(filter(lambda x: x>=5 and x<=10, d))
# filter는 lambda 또는 함수의 반환값이 True일 때 해당 요소를
# 가져온다. 따라서, True, False가 나오는 조건식을 넣어야 한다.
print('random한 숫자 10개중 5 이상 10이하인것은?:',e)

f = [1, 2, 3, 4, 5]
from functools import reduce
# reduce는 요소 처음부터 순차적으로 지정된 함수를 처리해준다.
g = reduce(lambda x, y : x + y, f)
# 주어진 함수 표현식이 합이므로, f의 1+2=3을 3과 더하고 그 값을
# 또 4와 더하고 또 5와 더한 1+2+3+4+5 = 15가 출력되는 것이다.
print(g)

