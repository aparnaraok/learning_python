import pandas as pd
import numpy as np

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100] #bins must increase monotonically
cats = pd.cut(ages, bins)
print(cats.codes)
print(pd.value_counts(cats))

# cisco@cisco-ThinkPad-T430:~/PycharmProjects/training/day_thirteen$ python discrete_bind.py
# [0 0 0 1 0 0 2 1 3 2 2 1]
# (18, 25]     5 #includes 25
# (35, 60]     3
# (25, 35]     3
# (60, 100]    1
# dtype: int64

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins, labels=group_names)
data = np.random.rand(20)
print(pd.cut(data, 4, precision=2))

# [(0.68, 0.89], (0.68, 0.89], (0.47, 0.68], (0.27, 0.47], (0.47, 0.68], ..., (0.47, 0.68], (0.27, 0.47], (0.061, 0.27], (0.061, 0.27], (0.061, 0.27]]
# Length: 20
# Categories (4, interval[float64]): [(0.061, 0.27] < (0.27, 0.47] < (0.47, 0.68] < (0.68, 0.89]]
#
