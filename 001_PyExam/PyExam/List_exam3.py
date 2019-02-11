# Unpacking
k=[1,2,3]; x,y,z=k

print(x,y,z)

# 2차원 배열
a = list()

for i in range(3) :
    line = []
    for j in range(2) :
        line.append(0)
    a.append(line)

print('a:',a)

b = [[0 for jj in range(2)] for ii in range(3)]

print('b:',b)

c = [[0]*2 for iii in range(3)]

print('c:',c)