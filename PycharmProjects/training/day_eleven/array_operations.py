import numpy as np

a = np.arange(4.0)
print ("A is ", a)

print (" ")
b = a * 23.4
print ("B is ", b)

print (" ")
c = b/(a+1)
print ("C is ", c)

print (" ")
c = c+10
print (c)

arr = np.arange(100, 200)
select = [5,25,50,75,-5] #indices to be returned at last
print (arr[select]) #can use integer list as indices

print ("Div by 3......")
arr = np.arange(10, 20)
div_by_3 = arr%3 == 0 #comparison produces boolean array
print(div_by_3)
print(arr[div_by_3]) #can use boolean list as indices

print (" ")
arr = np.arange(10, 20).reshape((2,5))
print ("New array is ", arr)

# A is [0 1 2 3]
#
# B is [0.  23.4 46.8 70.2]
#
# C is [0.   11.7  15.6  17.55]
#
# [10.   21.7  25.6  27.55]
# [105 125 150 175 195]
# Div
# by
# 3......
# [False False  True False False  True False False  True False]
# [12 15 18]
#
# New
# array is [[10 11 12 13 14]
#           [15 16 17 18 19]]



#arange(4.0)

# A is [0. 1. 2. 3.]
#
# B is [0.  23.4 46.8 70.2]
#
# C is [0.   11.7  15.6  17.55]
#
# [10.   21.7  25.6  27.55]
# [105 125 150 175 195]
# Div
# by
# 3......
# [False False  True False False  True False False  True False]
# [12 15 18]
#
# New
# array is [[10 11 12 13 14]
#           [15 16 17 18 19]]


print("Array is ", arr)
print ("Sum is : ", arr.sum())
print ("Mean is : ", arr.mean())
print("Standard deviation sigma is : ", arr.std())
print ("Max is : ", arr.max())
print ("Min is : ", arr.min())
print ("All div by 3 : ", div_by_3.all())
print("Any div by 3 : ", div_by_3.any())
print ("No of ele div by 3 : ", div_by_3.sum())
print ("Indices of ele div by 3 : ", div_by_3.nonzero())

# Sum is :  14950
# Mean is :  149.5
# Standard deviation sigma is :  28.86607004772212
# Max is :  199
# Min is :  100
# All div by 3 :  False
# Any div by 3 :  True
# No of ele div by 3 :  3
# Indices of ele div by 3 :  (array([2, 5, 8]),)

#all arr same

# A is [0. 1. 2. 3.]
#
# B is [0.  23.4 46.8 70.2]
#
# C is [0.   11.7  15.6  17.55]
#
# [10.   21.7  25.6  27.55]
# [105 125 150 175 195]
# Div
# by
# 3......
# [False False  True False False  True False False  True False]
# [12 15 18]

# New
# array is [[10 11 12 13 14]
#           [15 16 17 18 19]]
# Array is [[10 11 12 13 14]
#           [15 16 17 18 19]]
# Sum is: 145
# Mean is: 14.5
# Standard
# deviation
# sigma is: 2.8722813232690143
# Max is: 19
# Min is: 10
# All
# div
# by
# 3: False
# Any
# div
# by
# 3: True
# No
# of
# ele
# div
# by
# 3: 3
# Indices
# of
# ele
# div
# by
# 3: (array([2, 5, 8]),)

