#Hierarchial index

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key1':['MH', 'MH', 'MH', 'TN', 'TN'],
                    'key2':[2000, 2001, 2002, 2001, 2002],
                    'data':[3, 2, 5, 6, 9]})
df2 = pd.DataFrame(np.arange(12).reshape((6,2)),
                   index=[['TN', 'TN', 'MH', 'MH', 'MH', 'MH'],
                          [2000, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'event2'])

#print(df2)

#       event1  event2
# TN 2000       0       1
#    2000       2       3
# MH 2000       4       5
#    2000       6       7
#    2001       8       9
#    2002      10      11

print(df2.loc['MH'].loc[2001])

# event1    8
# event2    9
# Name: 2001, dtype: int64

#since df1 and df2 are there...it should contain two keys
print(pd.merge(df1, df2, left_on=['key1','key2'], right_index=True))

#   key1  key2  data  event1  event2
# 0   MH  2000     3       4       5
# 0   MH  2000     3       6       7
# 1   MH  2001     2       8       9
# 2   MH  2002     5      10      11