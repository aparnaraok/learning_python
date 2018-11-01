import pandas as pd

obj = pd.Series(["pd", "wh", "sc"], index=[2,7,10])
print(obj.reindex(range(11), method='bfill', limit=2))

print(obj.drop(2))

# 0      pd
# 1      pd
# 2      pd
# 3     NaN
# 4     NaN
# 5      wh
# 6      wh
# 7      wh
# 8      sc
# 9      sc
# 10     sc
# dtype: object
# 7     wh
# 10    sc
# dtype: object