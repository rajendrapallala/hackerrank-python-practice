import numpy
N, M = tuple(map(int, input().split()))
A = numpy.array([input().split() for _ in range(N)], float)
numpy.set_printoptions(sign=' ')
print(numpy.mean(A, 1))
print(numpy.var(A, 0))
print(numpy.round(numpy.std(A),12))


