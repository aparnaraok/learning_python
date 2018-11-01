import pandas as pd
import numpy as np


a34 = np.array([[12,10,-21,7],
                [-17, 18,19,16],
                [13,-7,-18,10]])
#print(a34)

obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())

# a    1
# b    2
# c    3
# d    0

frame = pd.DataFrame(a34, index=['three', 'one', 'two'], columns=['d', 'a', 'b', 'c'])
print(frame)

print(frame.sort_index())

print("axis 1")
print(frame.sort_index(axis=1))
print(frame.sort_index(by='b'))
# dtype: int64
#         d   a   b   c
# three  12  10 -21   7
# one   -17  18  19  16
# two    13  -7 -18  10

#Default.....row wise
#         d   a   b   c
# one   -17  18  19  16
# three  12  10 -21   7
# two    13  -7 -18  10

# axis 1 (col wise)
#         a   b   c   d
# three  10 -21   7  12
# one    18  19  16 -17
# two    -7 -18  10  13



# axis 1
# /home/cisco/PycharmProjects/training/day_eleven/series_sort.py:25: FutureWarning: by argument to sort_index is deprecated, please use .sort_values(by=...)
#   print(frame.sort_index(by='b'))
#         a   b   c   d
# three  10 -21   7  12
# one    18  19  16 -17
# two    -7 -18  10  13
#         d   a   b   c
# three  12  10 -21   7
# two    13  -7 -18  10
# one   -17  18  19  16
