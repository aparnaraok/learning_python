import pandas as pd
import numpy as np

ts = pd.Series(np.random.rand(6), index=pd.date_range('1/1/2000', periods=6, freq='M'))
#m - monthly
#d - daily

print(ts)
print(ts.shift(2))
print(ts/(ts.shift(1) - 1))

ts_local = ts.tz_localize('UTC')
#print(ts_local)
# Freq: M, dtype: float64
# 2000-01-31 00:00:00+00:00    0.294866
# 2000-02-29 00:00:00+00:00    0.360746
# 2000-03-31 00:00:00+00:00    0.643564
# 2000-04-30 00:00:00+00:00    0.152536
# 2000-05-31 00:00:00+00:00    0.368251
# 2000-06-30 00:00:00+00:00    0.340916
# Freq: M, dtype: float64


print(" ")
print(ts_local.tz_convert('US/Eastern'))


# 2000-01-30 19:00:00-05:00    0.991441
# 2000-02-28 19:00:00-05:00    0.797358
# 2000-03-30 19:00:00-05:00    0.830730
# 2000-04-29 20:00:00-04:00    0.061298
# 2000-05-30 20:00:00-04:00    0.736971
# 2000-06-29 20:00:00-04:00    0.772811
#



# 2000-01-31    0.154271
# 2000-02-29    0.013299
# 2000-03-31    0.547877
# 2000-04-30    0.199360
# 2000-05-31    0.291728
# 2000-06-30    0.423644
#
# Freq: M, dtype: float64
# 2000-01-31         NaN
# 2000-02-29         NaN
# 2000-03-31    0.154271
# 2000-04-30    0.013299
# 2000-05-31    0.547877
# 2000-06-30    0.199360
#
#
# Freq: M, dtype: float64
# 2000-01-31         NaN
# 2000-02-29   -0.015725
# 2000-03-31   -0.555262
# 2000-04-30   -0.440943
# 2000-05-31   -0.364369
# 2000-06-30   -0.598138
# Freq: M, dtype: float64

