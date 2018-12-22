import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12.).reshape(3,4), columns=list('abcd'),
                   index=['tn', 'ka', 'kl'])

print(df1)
s1 = df1.loc['ka']

print(s1)

print(" ")
print("Subtraction..")
print(df1 - s1)

#       a    b    c    d
# tn -4.0 -4.0 -4.0 -4.0
# ka  0.0  0.0  0.0  0.0
# kl  4.0  4.0  4.0  4.0


#4567 is subtacted from 0123
#4567 is subtacted from 4567
#4567 is subtacted from 891011

print(" ")
print("Addition...")
print(df1 + s1)

# Addition...
#        a     b     c     d
# tn   4.0   6.0   8.0  10.0
# ka   8.0  10.0  12.0  14.0
# kl  12.0  14.0  16.0  18.0