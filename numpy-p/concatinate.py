import numpy
n,m,p = list(map(int, input().split()))
np = numpy.array( [list(map(int, input().split())) for i in range(n)]  )
mp = numpy.array( [list(map(int, input().split())) for i in range(m)]  )
print(numpy.concatenate((np,mp), axis=0))


