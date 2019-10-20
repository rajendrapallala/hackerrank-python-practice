import numpy
N, M = tuple(map(int, input().split()))

A = numpy.array([list(map(int, input().split())) for _ in range(N)])

B = numpy.sum(A,0)
#print(B)
print(numpy.prod(B))



