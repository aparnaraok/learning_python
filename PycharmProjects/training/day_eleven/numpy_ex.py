#List could be of any data type whereas array if of homogenous data type

import numpy as np
#a1 = np.array([12, -9, 10, 8,'aaa', -13]) #string accepts U21 as a1.dtype#float means everything is float
#a1 = np.array([12, -9, 10, 8,-12.5, -13]) #string accepts U21 as a1.dtype#float means everything is float
a1 = np.array([12, -9, 10, 8, 14])
#Since float is larger dt than int
a2 = np.array([-6, 17, 5, 12, 14])

print ("Array A1 is " , a1)
print ("Type of a1 is ", type(a1))
print("Data type of a1 is ", a1.dtype) #dtype is the datatype of individual ele
#[ 12  -9  10   8 -13] #no commas
#<class 'numpy.ndarray'>
#int64

if type(a1) is np.ndarray:
    print ("An array")
if a1.dtype == np.int32:
    print ("An array of numbers")

#float:
# [ 12.   -9.   10.    8.  -12.5 -13. ]
# <class 'numpy.ndarray'>
# float64
# An array

# Array A1 is  [ 12.   -9.   10.    8.  -12.5 -13. ]
# Type of a1 is  <class 'numpy.ndarray'>
# Data type of a1 is  float64
# An array

#####Multiply

print ("Product is ", a1 * 0.4) #Multiplies each ele by 0.4
#Product is  [ 4.8 -3.6  4.   3.2 -5.  -5.2]

print ("Addition is : ", a1 + a2)
print ("Subtraction is : ", a1 - a2)
print ("Product is  : ", a1 * a2)
print ("Division is : ", a1 / a2)

#Both arrays need to be of same size
# Addition is :  [ 6  8 15 20 28]
# Subtraction is :  [ 18 -26   5  -4   0]
# Product is  :  [ -72 -153   50   96  196]
# Division is :  [-2.         -0.52941176  2.          0.66666667  1.        ]