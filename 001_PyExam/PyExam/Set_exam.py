# 집합은 영어로 Set이지. Set는 그 집합 맞다ㅇㅇ
fruits = {'strawberry','grape','orange','pineapple'}

print('fruits의 종류는~?',fruits)

# 집합은 원소 겹치는거 무시하는거 기억남? 중1때 오졋고~
A = {'A+','A+','B+','B0','C+'}
print('내 이번학기 성적은 어떤가요?:',A)
# 앗 A+이 두개인데 1개만 출력됬다 맙소사;

# 출력해보면 알겠지만, 요서가 unordered 이기 때문에 매번 다른 순서로 출력됨ㅇㅇ
# 셋트는 fruits[0]의 방식으로 요소 참조가 불가능

# set에는 '반복 가능한 객체'가 들어간다.
a = set('apple')
print(a) # => 'a' 'p' 'l' 'e' 이렇게 4개만 드러감

# Set는 특이하게 Set안에서 Set을 사용할 수 없음.

'''ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ'''

# 집합 연산 사용하기 => 합집합 | 교집합 % 차집합 - 대칭차집합 ^
a = {1,2,3,4}; b = {3,4,5,6}; c = a.copy(); d = b.copy()
print('a와 b의 합집합? :',a|b)
print('a와 b의 교집합? :',a&b)
print('a와 b의 차집합? :',a-b)
print('a와 b의 대칭차집합? :',a^b)

a |= {5}; b-={5}
print('a에 {5}를 추가 :',a,'b에서 {5}를 제거 :',b)

# 연산자도 있지만 method도 제공 한다는 것~
print('합집합 :',set.union(c,d),end =' ')
print('교집합 :',set.intersection(c,d))
print('차집합 :',set.difference(c,d),end =' ')
print('대칭 차집합 :',set.symmetric_difference(c,d))

# update는 현재 세트에 다른 세트를 더함
c.update({5}); print('c에 {5}추가',c)
c.difference_update({5}); print('c에서 {5} 다시뺌ㅇㅇ',c)

# 현재 세트가 다른 세트의 부분집합 or 상위집합인지 확인
'''c = {1,2,3,4} d = {3,4,5,6}'''
print('c가 {1,2,3,4,5}의 부분집합임?',c.issubset({1,2,3,4,5}))
print('d가 {5,6}의 상위 집합임?',d.issuperset({5,6}))
print('c와 d는 겹치는 부분이 없니?',c.isdisjoint(d))

# 조금만 더 이번엔 요소를 가꼬 놀아보자!
print('c의 길이를 말해바바',len(c))
c.add(5); print('c에다 원소 5를 더해바',c)
c.remove(5); print('c에서 원소 5를 제거해봐',c)
c.discard(5); print('c에서 원소 5를 버려봐',c)
c.pop(); print('pop으로 임의요소 제거',c)
c.clear(); print('clear로 모두 제거',c)
'''remove와 discard의 차이점은 remove는 5가
없으면 error, discard는 그런거 없음'''

# 요소 in set, 요소 not in set 이용법은 알제? ㅇㅋ

# for 문으로 set 만들어 바바바~
e = {i for i in 'pineapple'}
print('pineapple중에 뭐가 e에 들어갈까? :',e)
e = {i for i in 'pineapple' if i not in 'ni'}
print('n과 i는 없었으면 좋겟어!',e)

