from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig

#Define a matrix
A = array([[1,2], [3,4], [5,6]])
print("Array is >>>>", A)
print(" ")

#Calculate the mean of each column
M = mean(A.T, axis=1)
print("Mean is >>>")
print(M)
print(" ")

#Center column by subtracting column means
C = A - M
print(C.T)
print("")

#Calculate covariance matrix of centered matrix
V = cov(C.T)
print(V)
print(" ")

#eigen decomposition of covariance matrix
values, vectors = eig(V)
print("Values>>>", values)
print("Vectors>>>", vectors)
print("")

#project data
P = vectors.T.dot(C.T)
print(P.T)
print(" ")

# Array is >> >> [[1 2]
#                 [3 4]
# [5
# 6]]
#
# Mean is >> >
# [3. 4.]
#
# [[-2.  0.  2.]
#  [-2.  0.  2.]]
#
# [[4. 4.]
#  [4. 4.]]
#
# Values >> > [8. 0.]
# Vectors >> > [[0.70710678 - 0.70710678]
#               [0.70710678  0.70710678]]
#
# [[-2.82842712  0.]
#  [0.          0.]
# [2.82842712
# 0.]]
