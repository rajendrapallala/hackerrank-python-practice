import numpy
A = list(map(float, input().split()))
x =float(input())
print(numpy.polyval(A,x))
#print(numpy.polyval(list(map(float,input().split())),float(input())))

