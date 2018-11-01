import numpy as np

x, y = np.mgrid[0:5, 0:5]
print (" X is ", x)

#random data
rand_data = np.random.rand(5,5) #By default it creates random numbers bet 0 and 1 with 5cross5 matrix

print ("Random array is ", rand_data)


# X is  [[0 0 0 0 0]
#  [1 1 1 1 1]
#  [2 2 2 2 2]
#  [3 3 3 3 3]
#  [4 4 4 4 4]]
# Random array is  [[0.89314681 0.13580406 0.03848476 0.78959645 0.55346456]
#  [0.14091643 0.98502643 0.55201951 0.99997913 0.04833894]
#  [0.61237239 0.60535312 0.12767516 0.49094446 0.61158066]
#  [0.75288362 0.20543606 0.92005409 0.39690453 0.70218926]
#  [0.24487636 0.86707322 0.81234496 0.55898077 0.49699688]]

#2 cross 2

# Random array is  [[0.84153436 0.08035523]
#  [0.17087867 0.07279672]]
