import pandas as pd
#Addition similar to Union of set producing sum as a result.

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e','f','g'])

s3 = s1 + s2
print("Sum is ....")
print(s3)

# Sum is ....
# a    5.2
# c    1.1
# d    NaN (Nan + Nan)
# e    0.0
# f    NaN
#g    NaN