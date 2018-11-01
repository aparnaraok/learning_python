import numpy as np

arr = np.array([4.5, 2.3, 6.7, 1.2, 1.8, 5.5])
print ("After sorting...")
print(arr.sort())
print (arr)

print (" ")
x = np.array([4.5, 2.3, 6.7, 1.2, 1.8, 5.5])
print ("Numpy sorting....")
print (np.sort(x))

print(x)

print (" ")
s = x.argsort() #Gives the indices of the ele after sorting
print ("After arg sort.....indices of the ele is ")
print (s)

print (x[s])
print (x[s][::-1])

# After
# sorting...
# None
# [1.2 1.8 2.3 4.5 5.5 6.7]
#
# # Numpy
# # sorting....
# # [1.2 1.8 2.3 4.5 5.5 6.7]
# # [4.5 2.3 6.7 1.2 1.8 5.5]
# #
# # After
# # arg
# # sort.....indices
# # of
# # the
# # ele is
# # [3 4 1 0 5 2]
# # [1.2 1.8 2.3 4.5 5.5 6.7]
#[6.7 5.5 4.5 2.3 1.8 1.2]
