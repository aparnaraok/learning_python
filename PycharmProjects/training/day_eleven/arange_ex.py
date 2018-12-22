import numpy as np

x = np.arange(0,10,1) #start, stop, step
print (" X is  ", x)

#From 0 to 10,....25 points required to map ...inwhich already 10 is include....so (25-1) is the remaining)
#Formula:
#start + (summation(i=1 to step)((stop - start)/(step-1)))
#1st : 10/(25-1)
#2nd : (10/24) * 2
#5th : (10/24) * 3
line_space = np.linspace(0,10,25)
print ("Line array is ", line_space)
#Line space : size of the array is step size

log_space = np.logspace(0,10,10, base=np.e)
print ("log array is : ", log_space)


#  X is   [0 1 2 3 4 5 6 7 8 9]
# Line array is  [ 0.          0.41666667  0.83333333  1.25        1.66666667  2.08333333
#   2.5         2.91666667  3.33333333  3.75        4.16666667  4.58333333
#   5.          5.41666667  5.83333333  6.25        6.66666667  7.08333333
#   7.5         7.91666667  8.33333333  8.75        9.16666667  9.58333333
#  10.        ]
# log array is :  [1.00000000e+00 3.03773178e+00 9.22781435e+00 2.80316249e+01
#  8.51525577e+01 2.58670631e+02 7.85771994e+02 2.38696456e+03
#  7.25095809e+03 2.20264658e+04]
