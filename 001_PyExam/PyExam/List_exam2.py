# 이건 좀 신세계인데; for 문에서 리스트 참조할 수 있음.
a = [15, 32, 53, 6]

for i in a:
    print('a의 원소가 다나온다ㄷㄷ :', i)

for i in range(len(a)):
    print('a의 원소가 다나옴ㄷㄷ :',a[i])

for index, value in enumerate(a) :
    print('인덱스는? :',index,'값은? :',value)

# 야 리스트안에 원소가 있는지를 in이냐 not in으로 알 수 있음
# 이거 While문의 조건문으로 써라 리얼
TorF = 21 in a
print('21은 a 안에 있니? :',TorF)
TorF = 15 in a
print('15는 a 안에 있니? :',TorF)
TorF = 32 not in a
print('32는 a 안에 없니? :',TorF)

# min, max, sum은 MATLAB과 거의 똑같은 것 같다.
print('a에서 가장 작은 값은? :',min(a))
print('a에서 가장 큰 값은? :',max(a))
print('a의 합은? :',sum(a))

# Python 누가 쉽다고 했냐; 조금 쉬운것 같기도 한데..
# Python의 특이한 점인 list comprehension이다.
b = [i for i in range(10)]
print('for 문을 이용해 만든 b를 보여줭 :',b)
b = [i+3 for i in range(10)]
print('range(10)의 원소에 +3 :',b)
b = [i+2 for i in range(10) if i%2==0]
print('range(10)의 짝수 원소에 +2:',b)
# Highlight
b = [i*j for i in range(1,4) for j in range(1,5)]
print('[1 2 3]*[1 2 3 4] :',b)

# map 함수가 기억 안나는데...
c = [1.2, 2.8, 3.5, 4.2]
print('c는 원래 이래~',c)
c = list(map(int,c))
print('map을 이용해 c의 요소를 int 함수 처리 :',c)