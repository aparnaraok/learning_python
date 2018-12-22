from numpy import nan as NA
import pandas as pd

data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())

print(" ")
print(data[data.notnull()])

data = pd.DataFrame([[1.,6.5,3.], [1.,NA,NA],[NA, NA, NA], [NA, 6.5, 3.]])
print(data)
#passing how = 'all' to dropna will only drop rows that are all NA

print(data.dropna()) #delete wherever NA is present
print(data.dropna(how = 'all')) #delete only if NA is present is the entire row





# 0    1.0
# 2    3.5
# 4    7.0
# dtype: float64
#
# 0    1.0
# 2    3.5
# 4    7.0
# dtype: float64
#
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0  NaN  NaN
# 2  NaN  NaN  NaN
# 3  NaN  6.5  3.0
#
#
#     0    1    2
# 0  1.0  6.5  3.0
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0  NaN  NaN
# 3  NaN  6.5  3.0
