#a diagonal matrix

import numpy as np

diag_mat = np.diag([1,2,3])
print ("Diagonal matrix is ")
print(diag_mat)

# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]

num_zero = np.zeros(5)
print ("Num of Zeroes ", num_zero)
#Num of Zeroes  [0. 0. 0. 0. 0.] #Returns float by default

print ("Type is ", num_zero.dtype)
#Type is  float64

n =1000
my_int_array = np.zeros(n, dtype=np.int) #specifically int since default is float
print ("My int data type is ", my_int_array.dtype)

#My int data type is  int64

c = np.ones((3,3))
#c = np.ones[[3,3]] #Both are smae either list or tup
print ("c is : ", c)
# c is :  [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

