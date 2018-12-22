import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(12).reshape((4,3)),
                     index=[['a', 'a', 'b', 'b'], [1,2,1,2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])

print(frame)

#     Ohio     Colorado
#     Green Red    Green
# a 1     0   1        2
#   2     3   4        5
# b 1     6   7        8
#   2     9  10       11


frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
#print(frame)

#            Ohio     Colorado
#           Green Red    Green
# key1 key2
# a    1        0   1        2
#      2        3   4        5
# b    1        6   7        8
#      2        9  10       11


# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2
# a    1        0   1        2
#      2        3   4        5
# b    1        6   7        8
#      2        9  10       11

print("Framing....")
print(frame.swaplevel('key1', 'key2'))
print(frame.sort_index(level=0))
print(frame.sum(level='key1'))
print(frame.sum(level=1)) #2nd index...0(1st index)

# key2
# 1         6   8       10
# 2        12  14       16