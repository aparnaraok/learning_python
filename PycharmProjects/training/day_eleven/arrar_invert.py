import numpy as np

arr = np.array([[3,2],[6,4]])
# print (arr)
#
# np.invert(arr)
# print ("After inverting....")
# print (arr)

#print(np.linalg.inv(arr)) #Singular matrix...determinant is 0...(3*4)-(2*6) = 0

#[6,5]
# [[ 1.66666667 -0.66666667]
#  [-2.          1.        ]]


#idempotent:
#if we mul any mat with org mat..the resulatant mat is same


print ("transpose is ", arr.transpose())
u = np.eye(2) #unit 2cross2  mat : "eye repr I
#I means idempotent

print ("U is ", u)

j = np.array([[0.0, -1.0], [1.0, 0.0]])
print (np.dot(j, j)) #matrix product


# transpose is  [[3 6]
#  [2 4]]
# U is  [[1. 0.]
#  [0. 1.]]
# [[-1.  0.]
#  [ 0. -1.]]
