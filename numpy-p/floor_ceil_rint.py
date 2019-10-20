import numpy

l = list(map(float, input().split()))
A = numpy.array(l)
numpy.set_printoptions(sign=' ')
print( numpy.floor(A))
print( numpy.ceil(A))
print( numpy.rint(A))



