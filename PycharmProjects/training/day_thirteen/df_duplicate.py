import pandas as pd
data = pd.DataFrame({'k1':['one']*3+['two']*4,
                     'k2':[1,1,2,3,3,4,4]})
print(data.duplicated('k1'))

print(data.drop_duplicates('k1')) #returns
print(data.drop_duplicates('k1', inplace=True)) #changes in actual place

#Initially 1 is not dup..so it is false...
#then one is repeated 3 times----dup--true

#same reps to two

# 0    False
# 1     True
# 2     True
# 3    False
# 4     True
# 5     True
# 6     True
# dtype: bool

#     k1  k2
# 0  one   1
# 3  two   3
# None


