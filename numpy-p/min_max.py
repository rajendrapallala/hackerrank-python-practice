import numpy
N, M =  tuple(list(map(int, input().split())))

A = numpy.array([list(map(int, input().split())) for _ in range(N)])

B = numpy.min(A, 1)

print( numpy.max(B))


