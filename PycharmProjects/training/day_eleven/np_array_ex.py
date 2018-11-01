#row : col
import numpy as np

a34 = np.array([[12,10,-21,7],
                [-17, 18,19,16],
                [13,-7,-18,10]])
print ("A34 is ", a34)

# A34 is  [[ 12  10 -21   7]
#  [-17  18  19  16]
#  [ 13  -7 -18  10]]

print ("Size is ", a34.size)
print ("Shape is ", a34.shape)

# Size is  12
# Shape is  (3, 4)


print ("Second row is ", a34[1])
#Second row is  [-17  18  19  16]

print ("First column is ", a34[:,0]) #: denotes entire row
#First column is  [10 18 -7]

#Slicing:
print (a34[1, 2])
print (a34[1, 1:3])

# 19
# [18 19]

