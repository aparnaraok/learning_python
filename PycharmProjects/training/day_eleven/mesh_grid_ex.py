#meshgrid is used for 3 D / multi-Dim arrays

import numpy as np
x, y = np.mgrid[1:6, 10:14] #1:6 defines the no of rows
#10:14 defines the no of cols...col is preferred
print ("X is ", x)
print ("Y is ", y)
#Same size is obtained as output..so x + y is possible in meshgrid
#even if we five 1:9 and 10:14

print(np.add(x,y))
print ("Sum is ", x+y)
# Sum is  [[11 12 13 14]
#  [12 13 14 15]
#  [13 14 15 16]
#  [14 15 16 17]
#  [15 16 17 18]]

# X is  [[1 1 1 1]
#  [2 2 2 2]
#  [3 3 3 3]
#  [4 4 4 4]
#  [5 5 5 5]]
# Y is  [[10 11 12 13]
#  [10 11 12 13]
#  [10 11 12 13]
#  [10 11 12 13]
#  [10 11 12 13]]
