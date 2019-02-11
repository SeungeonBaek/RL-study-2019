x = {'a': 0, 'b': 10, 'c': 20, 'd': 30}

y = x

print('y :',y,'\nx :',x)
# x와 y의 개체가 같냐? 그러면 값은 같냐?
print(x is y, x == y)

z = x.copy()
print(x is z, x == z) # 카피하면 값은 같되, 객체는 다름

for i in x :
    print(i, end =' ') # 키만 출력된다 ㅠ
print()
for key,  value in x.items() : # items()를 통해 키-값 쌍 출력
    print(key,value, end =' ')
print()

print('a' in x)

# value와 key의 자리를 바꿔보자!
y = {value: key for key, value in x.items()}
print('value와 key를 바꾸면? :',y)
# dictionary에서 key-값 쌍을 삭제하는건 위와 비슷한 방법으로 한다.
z = {key : value for key, value in x.items() if value!=20}
print('value가 20인 \'c\':20 쌍 제거 :',z)

# 살짝 심화 ㅎ 2차원 리스트마냥 딕셔너리 안에 딕셔너리 가능하다!
terrestrial_planet = { 'Mercury' : { 'mean_R' : 2439.7,
    'mass' : 3.3022E+23, 'orbital_p' : 87.969 }, 'Venus' :{
    'mean_R' : 6051.8, 'mass' : 4.876E+24, 'orbital_p' : 224.70069,
}}
print(terrestrial_planet)

