import pandas as pd
df1 = pd.DataFrame({'lkey':['a', 'd', 'b'],
                    'data1':range(3)})
df2 = pd.DataFrame({'rkey':['a', 'c', 'a', 'b', 'c', 'c', 'b'],
                    'data2':range(7)})

merge_data = pd.merge(df1, df2, left_on='lkey', right_on='rkey', how='left')
#can merge series(1D data) also..
#how = left ...outer...right(df2 is Nan)
print(merge_data)

#   lkey  data1 rkey  data2
# 0    a      0    a      0
# 1    a      0    a      2
# 2    c      1    c      1
# 3    c      1    c      4
# 4    c      1    c      5
# 5    b      2    b      3
# 6    b      2    b      6

#takes only unique values

#  lkey  data1 rkey  data2
# 0    a      0    a      0
# 1    a      0    a      2
# 2    b      2    b      3
# 3    b      2    b      6

#if doesn't match...prints NAn

# lkey  data1 rkey  data2
# 0    a    0.0    a    0.0
# 1    a    0.0    a    2.0
# 2    d    1.0  NaN    NaN
# 3    b    2.0    b    3.0
# 4    b    2.0    b    6.0
# 5  NaN    NaN    c    1.0
# 6  NaN    NaN    c    4.0
# 7  NaN    NaN    c    5.0

#how = right(df2 is NaN)
#   lkey  data1 rkey  data2
# 0    a    0.0    a      0
# 1    a    0.0    a      2
# 2    b    2.0    b      3
# 3    b    2.0    b      6
# 4  NaN    NaN    c      1
# 5  NaN    NaN    c      4
# 6  NaN    NaN    c      5

#how - left
#   lkey  data1 rkey  data2
# 0    a      0    a    0.0
# 1    a      0    a    2.0
# 2    d      1  NaN    NaN
# 3    b      2    b    3.0
# 4    b      2    b    6.0