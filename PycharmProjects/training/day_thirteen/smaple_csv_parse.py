import pandas as pd

data_read  = pd.read_csv('data.csv', header = None)
print(data_read.head()) #head returns first 5 rows and 14 cols

#    0   1   2   3      4
# 0  1   2   3   4  hello
# 1  5   6   7   8  world
# 2  9  10  11  12    foo

#setting the col values
data_read.columns = ['id1','id2', 'id3', 'id4', 'id5']
print(data_read.head()) #head returns first 5 rows and 14 cols

print(" ")
print("After setting the index......")
#setting the index...
var = data_read.set_index('id5')
print(var)



# After setting the index......
#        id1  id2  id3  id4
# id5
# hello    1    2    3    4
# world    5    6    7    8
# foo      9   10   11   12



#if any data missing in csv, replaces by Nan
# After setting the index......
#        id1  id2  id3  id4
# id5
# hello    1    2  3.0    4
# world    5    6  7.0    8
# foo      9   10  NaN   12


data = data_read.iloc[:,1:].values  #iloc always takes index val

print(data)

# [[2 3.0 4 'hello']
#  [6 7.0 8 'world']
#  [10 nan 12 'foo']]




