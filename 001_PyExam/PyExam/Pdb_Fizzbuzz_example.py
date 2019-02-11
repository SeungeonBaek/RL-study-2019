# i=1
#
# while i<=100:
#     if i%3==0 and i%5==0 :
#         print('FizzBuzz')
#     elif i%3==0 :
#         print('Fizz')
#     elif i%5==0 :
#         print('Buzz')
#     else :
#         print(i)
#     i=i+1
import pdb
for i in range(1,101) :
    pdb.set_trace()
    print('Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or i)
    
    #pdb.set_trace()를 사용하면 break point같은 역할을 해줌
    #c를 입력하면 계속 실행됨ㅇㅇ