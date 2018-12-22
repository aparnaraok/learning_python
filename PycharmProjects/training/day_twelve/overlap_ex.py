import pandas as pd
import numpy as np

a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])

b = pd.Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan

print(b[-1])

print(np.where(pd.isnull(a), b, a))
#[0.  2.5 2.  3.5 4.5 nan]

a.combine_first(b) #a has first preference over b
b[:-2].combine_first(a[2:])
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
                 'b': [np.nan, 2., np.nan, 6.],
                 'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
                 'b': [np.nan, 3., 4., 6., 8.]})
print(df1.combine_first(df2))

# nan
#      a    b     c
# 0  1.0  NaN   2.0
# 1  4.0  2.0   6.0
# 2  5.0  4.0  10.0
# 3  3.0  6.0  14.0
# 4  7.0  8.0   NaN
