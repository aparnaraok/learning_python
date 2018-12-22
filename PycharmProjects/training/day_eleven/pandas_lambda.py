import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12.).reshape(3,4), columns=list('abcd'),
                   index=['tn', 'ka', 'kl'])

s1 = df1.loc['ka']

print(df1) #(8-0)

f = lambda x : x.max() - x.min()
print(df1.apply(f)) #four val
print(df1.apply(f, axis = 1)) #only 3 val

# a    8.0
# b    8.0
# c    8.0
# d    8.0
# dtype: float64

#In each col...takes which value is max and which is min
