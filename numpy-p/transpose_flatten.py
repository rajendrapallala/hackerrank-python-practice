import numpy
n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
arr = numpy.array(a)
print(numpy.transpose(arr))
print(arr.flatten() )
