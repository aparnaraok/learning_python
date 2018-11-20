from numpy import array
from sklearn.decomposition import PCA

#Define a matrix
A = array([[1,2], [3,4], [5,6]]) #second row reduces to 0
#A = array([[1,4], [3,2], [5,9]]) #not reduces to zero
print(A)
print(" ")

#Create the PCA instances
pca = PCA(2) #2 reps columns...features means cols

#fit on data
pca.fit(A)

#access values and vectors
print(pca.components_)
print(" ")

print(pca.explained_variance_)
print(" ")

#Transform data
B = pca.transform(A)
print(B)

# [[1 2]
#  [3 4]
# [5
# 6]]
#
# [[0.70710678  0.70710678]
#  [-0.70710678  0.70710678]]
#
# [8. 0.]
#
# [[-2.82842712e+00 - 2.22044605e-16]
#  [0.00000000e+00  0.00000000e+00]    second row reduces to zero.
# [2.82842712e+00
# 2.22044605e-16]]
