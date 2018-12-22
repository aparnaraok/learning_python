import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(9).reshape((3,3)),
                     index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])

frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

#   Ohio  Texas  California
# a   0.0    1.0         2.0
# b   NaN    NaN         NaN
# c   3.0    4.0         5.0
# d   6.0    7.0         8.0

#states = ['Texas' , 'Utah', 'California']

#frame.reindex(columns = states)

#frame.reindex(index = ['a', 'b', 'c', 'd'],
 #             method='ffill', columns=states)

#print(frame)
