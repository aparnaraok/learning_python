import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12.).reshape(3,4), columns=list('abcd'))
#print(df1)
#     a    b     c     d
# 0  0.0  1.0   2.0   3.0
# 1  4.0  5.0   6.0   7.0
# 2  8.0  9.0  10.0  11.0

df2 = pd.DataFrame(np.arange(20.).reshape(4,5), columns=list('abcde'))
#print(df2)

#      a     b     c     d     e
# 0   0.0   1.0   2.0   3.0   4.0
# 1   5.0   6.0   7.0   8.0   9.0
# 2  10.0  11.0  12.0  13.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0

sum = df1 + df2

#print (sum)

#       a     b     c     d   e
# 0   0.0   2.0   4.0   6.0 NaN
# 1   9.0  11.0  13.0  15.0 NaN
# 2  18.0  20.0  22.0  24.0 NaN
#3   NaN   NaN   NaN   NaN NaN

print(df1.add(df2, fill_value= 0))

#       a     b     c     d     e
# 0   0.0   2.0   4.0   6.0   4.0
# 1   9.0  11.0  13.0  15.0   9.0
# 2  18.0  20.0  22.0  24.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0
print(df1.reindex(columns=df2.columns, fill_value=0))
#
#      a    b     c     d  e
# 0  0.0  1.0   2.0   3.0  0
# 1  4.0  5.0   6.0   7.0  0
# 2  8.0  9.0  10.0  11.0  0