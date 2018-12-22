# import pandas as pd
# import numpy as np
#
# #Series ----------->Acts like an ordered dict
#
# stocks = pd.Series([12,10,8,-6,4], index=["fennel", "corriander", "tamarind", "pepper", "cumin", "quanitit"])
# print(stocks.index)
# print(stocks['corriander'])
#
# #index refers to keys and [] refers to values
#
# if stocks['tamarind'] > 5:
#     print("Safe")
# else:
#     print("Alert")

#
# #Adding new elements
# stocks['leaves'] = 15
# print(stocks)
#
#
# print("Stocks greater than 5....")
# print(stocks[stocks>5])
# print(" ")
#
# print(stocks.values)
#
# print("Mul by 2....")
# print(2*stocks[stocks>0])
#
import pandas as pd

df = pd.DataFrame({'spice' : ['turmeric', 'cumin', 'coriander', 'turmeric', 'coriander', 'salt'],
                   'brand' : ['tur_brand', 'cumin_brand', 'cor_brand', 'tam_brand', 'mir_brand', 'salt_brand'],
                   'price' : [1000, 2000, 3000, 4000, 5000, 6000],
                   'qty': [1, 2, 3, 4, 5, 6]})


#print (df.groupby('spice'))

grouped = df['price'].groupby(df['spice'])
#print(grouped.mean())

means = df['price'].groupby([df['spice'], df['brand']]).mean()
#print(means)

print(" ")
print("size.....")
size = df.groupby(['price', 'brand']).size()
#print(size)

#all group keys
#for name, group in df.groupby('price'):
#    print ("Name..", name)
#    print("Group..", group)

#Selecting a column
print(df.groupby('price')['spice'])



# spice
# coriander    4000
# cumin        2000
# salt         6000
# turmeric     2500
# Name: price, dtype: int64
# spice      brand
# coriander  cor_brand      3000
#            mir_brand      5000
# cumin      cumin_brand    2000
# salt       salt_brand     6000
# turmeric   tam_brand      4000
#            tur_brand      1000
# Name: price, dtype: int64


# size.....
# price  brand
# 1000   tur_brand      1
# 2000   cumin_brand    1
# 3000   cor_brand      1
# 4000   tam_brand      1
# 5000   mir_brand      1
# 6000   salt_brand     1
# dtype: int64



# Name.. 1000
# Group..        brand  price  qty     spice
# 0  tur_brand   1000    1  turmeric
# Name.. 2000
# Group..          brand  price  qty  spice
# 1  cumin_brand   2000    2  cumin
# Name.. 3000
# Group..        brand  price  qty      spice
# 2  cor_brand   3000    3  coriander
# Name.. 4000
# Group..        brand  price  qty     spice
# 3  tam_brand   4000    4  turmeric
# Name.. 5000
# Group..        brand  price  qty      spice
# 4  mir_brand   5000    5  coriander
# Name.. 6000
# Group..         brand  price  qty spice
# 5  salt_brand   6000    6  salt
