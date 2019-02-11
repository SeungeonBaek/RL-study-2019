# 리스트 시작
a = list()
b = list('hello')
print('empty list : ',a)
print('문자열 list : ',b)

# 리스트 참조하기
c = list(range(1,100,11))

print('모든 원소 참조 :',c[:])
print('0 ~ 3 원소 참조',c[:4])
print('4 ~ -2 원소 참조',c[4:-1])

# 리스트 조작하기
c.append(100)

print('뒤에 100붙이기 :',c)

c.append([111, 122])
c.extend([111,122])

print('append와 extend 차이 :',c)

c.insert(len(c),133)
c.remove([111,122])
print('133 마지막에 삽입, [111,122]없애기 : ',c)

# index, count 다루기
print('100은 몇번째 인덱스? :',c.index(100))
print('100은 몇개나 있어? :',c.count(100))

# reverse로 뒤집고 sort로 내림차순해볼까?
b.reverse()
print('reverse로 뒤집어보자 올레! :',b)
c.sort()
print('내림차순 정렬',c)

# clear로 없애볼까
b.clear()
print('깔끔해졋나? - claer :',b)

# del로 없애기도 가능한거 알어?
del c[5:len(c)]

print('index 5부터 del한 c',c)

# 할당과 복사의 차이는 객체에 있다는거 알아?
d = list(range(1,6))
e = d
f = d.copy()
print('d의 의지 :',d)
print('e의 의지 :',e)
print('f의 의지 :',f)

print('d와 e(할당)은 같은 객체인가?',d is e)
print('d와 f(복사)는 같은 객체인가?',d is f)

# 리스트끼리 연산할 수 있다는걸 알고 있나 자네?
g = d + e
h = d*2
print('d와 e를 합쳐보자 :',g)
print('d를 2배하면 똑같지? :',h)

