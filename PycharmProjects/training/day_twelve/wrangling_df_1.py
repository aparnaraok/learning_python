import pandas as pd
df1 = pd.DataFrame({'key':['a', 'c', 'b'],
                    'data1':range(3)})
df2 = pd.DataFrame({'key':['a', 'c', 'a', 'b', 'c', 'c', 'b'],
                    'data2':range(7)})

merge_data = pd.merge(df1, df2, on='key')
#can merge series(1D data) also..

print(merge_data)

#   key  data1  data2
# 0   a      0      0
# 1   a      0      2
# 2   c      1      1
# 3   c      1      4
# 4   c      1      5
# 5   b      2      3
# 6   b      2      6


