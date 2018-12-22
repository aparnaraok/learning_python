import numpy as np
#mat and matrix have same functionality

a = np.array([[1,2],[3,4]])
m = np.mat(a) # convert 2-d array to matrix

m = np.matrix([[1, 2], [3, 4]])
print(a[0])

# result is 1-dimensional
#array([1, 2])
print(m[0])

# result is 2-dimensional
#matrix([[1, 2]])
print(a*a)
# element-by-element multiplication
#array([[ 1, 4], [ 9, 16]])
print(m*m)
# (algebraic) matrix multiplication
#matrix([[ 7, 10], [15, 22]])

print(a**3)
# element-wise power
#array([[ 1, 8], [27, 64]])

print(m**3)
# matrix multiplication m*m*m
#matrix([[ 37, 54], [ 81, 118]])
print(m.T)
# transpose of the matrix
#matrix([[1, 3], [2, 4]])

print(m.H)
# conjugate transpose (differs from .T for complex matrices)
#matrix([[1, 3], [2, 4]])
print(m.I)
# inverse matrix
#matrix([[-2. , 1. ], [ 1.5, -0.5]]


#
#
# [1 2]
# [[1 2]]
# [[ 1  4]
#  [ 9 16]]
# [[ 7 10]
#  [15 22]]
# [[ 1  8]
#  [27 64]]
# [[ 37  54]
#  [ 81 118]]
# [[1 3]
#  [2 4]]
# [[1 3]
#  [2 4]]
# [[-2.   1. ]
#  [ 1.5 -0.5]]