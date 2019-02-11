# Dictionary 입니당. 키1: 값1, 키2: 값2 이렇게 표현해용
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 100 : 'e'}
print(x[100])

x1 = dict(a=10, b=20, c=30, d='e') # d자리에 100넣으면 왜않되?
print('x1 :',x1)

x2 = dict(zip(['a','b','c'],[10,20,30]))
print('x2 :',x2)

x3 = dict({'a':10, 'b':20, 'c':30})
print('x3 :',x3)

x4 = dict(zip(['a','b',30],[i for i in range(10,40,10)]))
print('x4 :',x4)

x4['d']=40 # 키: 값 추가하는법 개 쉽지?
print('modified x4 :',x4)

# 키 값을 할당해 줄 수 있음ㅇㅇ
x4[30]='c'
print('modified x4 :',x4)

# 키 개수 구할 수 있음ㅇㅇ
# len으로 구할 수 있음 예제 필요하냐? ㅇㅋ
print(len(x1))

# 키 값을 update 해주는 법은 다음과 같다ㅎㅎ
# x4 = {'a': 10, 'b': 20, 30: 'c', 'd': 40} 일때
x4['a']=100
print('updated(1) x4:',x4)
x4.update(a=10)
print('updated(2) x4:',x4)

# 키-값 쌍을 삭제하는 법은 다음과 같다ㅎㅎ
print(x4.pop(30),x4)
# 30의 키를가진 'c'가 반환되었고, x4에 30 : 'c'쌍이 빠진걸 볼 수 있다.
del x4['a']
print('deleted x4:',x4)
x4.clear()
print('cleared x4:',x4)

# get으로 특정 키의 값 가져오는법 보실?
# x3 = {'a': 10, 'b': 20, 'c': 30} 임 이제 얘로할거
print('키 a의 값은? :',x3.get('a'))

# 딕셔너리에 키와 값을 추가해볼까?
x3.setdefault('d') # 값 추가안하면 None이 들어감ㅋ.ㅋ
x3.setdefault('e',50)
print('setdefualt로 추가한 딕셔너리 x3 :',x3)

# 딕셔너리를 파헤쳐보자
print('x3의 키-값 쌍',x3.items()); print('x3의 키는?',x3.keys())
print('x3의 값은?',x3.values())

# key가 주어질때 딕셔너리를 만드는방법
keys = ['a','b','c','d']
x5 = dict.fromkeys(keys)
x6 = dict.fromkeys(keys,[i for i in range(10,50,10)]) # 실패
print('x5는 뭐냐? :',x5)
print('x6은 뭐냐? :',x6)