import pandas as pd
import numpy as np

arr = np.arange(12).reshape((3,4))
print(np.concatenate([arr, arr], axis=1))

# [[ 0  1  2  3  0  1  2  3]
#  [ 4  5  6  7  4  5  6  7]
#  [ 8  9 10 11  8  9 10 11]]