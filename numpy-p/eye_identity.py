import numpy
N, M = tuple(map(int, input().split()))
a = str(numpy.eye(N, M, 0)).replace('1', ' 1').replace('0',' 0')
print(a)


