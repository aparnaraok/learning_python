import pandas as pd
#Series ----------->Acts like an ordered dict

stocks = pd.Series([12,10,8,-6,4], index=["fennel", "corriander", "tamarind", "pepper", "cumin"])
print(stocks.index)
print(stocks['corriander'])

#index refers to keys and [] refers to values

if stocks['tamarind'] > 5:
    print("Safe")
else:
    print("Alert")

#Adding new elements
stocks['leaves'] = 15
print(stocks)

# Index(['fennel', 'corriander', 'tamarind', 'pepper', 'cumin'], dtype='object')
# 10
# Safe
# fennel        12
# corriander    10
# tamarind       8
# pepper        -6
# cumin          4
# leaves        15
# dtype: int64


print("Stocks greater than 5....")
print(stocks[stocks>5])
print(" ")

print(stocks.values)

print("Mul by 2....")
print(2*stocks[stocks>0])


# Stocks greater than 5....
# fennel        12
# corriander    10
# tamarind       8
# leaves        15
#
# dtype: int64
#
# [12 10  8 - 6  4 15]
#
# Mul by 2....
# fennel        24
# corriander    20
# tamarind      16
# cumin          8
# leaves        30
# dtype: int64
