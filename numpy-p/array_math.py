import numpy
N, M = tuple(map(int, input().split()))
a=[]
b=[]
for _ in range(N):
    l = list(map(int, input().split()))
    a.append(l)

for _ in range(N):
    l = list(map(int, input().split()))
    b.append(l)

A = numpy.array(a)
B = numpy.array(b)


print ( A + B )
print (A - B)
print (A * B)
print (A // B)
print (A % B)
print (A ** B)



