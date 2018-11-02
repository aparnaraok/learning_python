#Hierarchial index

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key1':['MH', 'MH', 'MH', 'TN', 'TN'],
                    'key2':[2000, 2001, 2002, 2001, 2002],
                    'data':[3, 2, 5, 6, 9]})
df2 = pd.DataFrame(np.arange(12).reshape((6,2)),
                   index=pd.Index(['TN', 'TN', 'MH', 'MH', 'MH', 'MH'],
                          name='state'),
                   columns=pd.Index(['event1', 'event2'],name='event'))

print(df2)
print(df2.stack())
#tn is repeated twice..so indices assigned 2 times
#mh is repeates 4 times..so indices assigned 4 times

# event  event1  event2
# state
# TN          0       1
# TN          2       3
# MH          4       5
# MH          6       7
# MH          8       9
# MH         10      11



# state  event
# TN     event1     0
#        event2     1
#        event1     2
#        event2     3
# MH     event1     4
#        event2     5
#        event1     6
#        event2     7
#        event1     8
#        event2     9
#        event1    10
#        event2    11
# dtype: int64



df3 = pd.DataFrame(np.arange(12).reshape((6,2)),
                   index=pd.Index(['KL', 'TN', 'KA', 'TS', 'AP', 'MH'],
                          name='state'),
                   columns=pd.Index(['event1', 'event2'],name='event'))
sdf3 = df3.stack()
print(df3)

# event  event1  event2
# state
# KL          0       1
# TN          2       3
# KA          4       5
# TS          6       7
# AP          8       9
#MH         10      11

print(sdf3)

# state  event
# KL     event1     0
#        event2     1
# TN     event1     2
#        event2     3
# KA     event1     4
#        event2     5
# TS     event1     6
#        event2     7
# AP     event1     8
#        event2     9
# MH     event1    10
#        event2    11
# dtype: int64


print(sdf3.unstack(0))     #0 rep x axis (rows)
#   KL  TN  KA  TS  AP  MH
# event
# event1   0   2   4   6   8  10
#event2   1   3   5   7   9  11

print(" ")
print(sdf3.unstack('event'))

# event  event1  event2
# state
# KL          0       1
# TN          2       3
# KA          4       5
# TS          6       7
# AP          8       9
# MH         10      11

print(" col...")
print(sdf3.unstack(1))

#0 does on state ....1 does on event

#  col...
# event  event1  event2
# state
# KL          0       1
# TN          2       3
# KA          4       5
# TS          6       7
# AP          8       9
# MH         10      11

print('state...')
print(sdf3.unstack('state'))


# state...
# state   KL  TN  KA  TS  AP  MH
# event
# event1   0   2   4   6   8  10
# event2   1   3   5   7   9  11


print(df3.rename(index=str.lower, columns=str.title))

# event  Event1  Event2
# state
# kl          0       1
# tn          2       3
# ka          4       5
# ts          6       7
# ap          8       9
# mh         10      11
