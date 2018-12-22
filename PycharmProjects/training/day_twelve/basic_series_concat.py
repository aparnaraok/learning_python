import pandas as pd

s1 = pd.Series([0,1], index=['a', 'b'])
s2 = pd.Series([2,3,4], index=['c','d','e'])
s3 = pd.Series([5,6], index=['f', 'g'])
pd.concat([s1, s2, s3])
pd.concat([s1, s2, s3], axis=1)#<Default axis 0>
s4 = pd.concat([s1 * 5, s3])
pd.concat([s1, s4], axis=1) #<Default outer>
pd.concat([s1, s4], axis=1, join='inner')
print(pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']]))

#concat...default outer
#merge..default inner

#      0    1
# a  0.0  0.0
# c  NaN  NaN
# b  1.0  5.0
# e  NaN  NaN