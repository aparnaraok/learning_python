import pandas as pd

obj = pd.Series(["pd", "wh", "sc"], index=[0,4,8])
obj = pd.Series(["pd", "wh", "sc"], index=[2,7,10])
#print(obj)

#print(obj.reindex(range(11), method='ffill'))
print(obj.reindex(range(11), method='bfill', limit=2))
#print(obj.reindex(range(11)))
# 0     pd
# 1     pd
# 2     pd
# 3     pd
# 4     wh
# 5     wh
# 6     wh
# 7     wh
# 8     sc
# 9     sc
# 10    sc
#dtype: object

#if not method :
# 0      pd
# 1     NaN
# 2     NaN
# 3     NaN
# 4      wh
# 5     NaN
# 6     NaN
# 7     NaN
# 8      sc
# 9     NaN
# 10    NaN
# dtype: object

#backward fill: (8-5) [2,7,10]
# 0      pd
# 1      wh
# 2      wh
# 3      wh
# 4      wh
# 5      sc
# 6      sc
# 7      sc
# 8      sc
# 9     NaN
# 10    NaN
#dtype: object


#[2,7,10]

# 0     pd
# 1     pd
# 2     pd
# 3     wh
# 4     wh
# 5     wh
# 6     wh
# 7     wh
# 8     sc
# 9     sc
# 10    sc
# dtype: object
