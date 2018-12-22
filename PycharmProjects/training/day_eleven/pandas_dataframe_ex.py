import pandas as pd

df = pd.DataFrame({'qty' : [12, 11, 19, 10, 15, 19],
                   'fg' : ['wh', 'pd', 'sg', 'pd', 'wh', 'pd'],
                   'st' : ['pb', 'tn', 'mh', 'ka', 'mh', 'wb']},
                    index = [98, 99, 2001, 97, 2002, 2005])

print (df)
#    qty  fg  st
# 0   12  wh  pb
# 1   11  pd  tn
# 2   19  sg  mh
# 3   10  pd  ka
# 4   15  wh  mh
# 5   19  pd  wb

print ("Sum....")
print(df.groupby('fg').sum())
print(" ")
print("Mean.....")
print(df.groupby('fg').mean())

print("")
print("describe...")
print (df.describe())

print(" ")
print("St...")
print(df['st'])
print(" ")
#print("df loc 2...")
#print(df.loc[1])

#Locates the index in Df:
print("Locating index 98....")
print(df.loc[98]) #earlier ix was used instead of loc

# Locating index 98....
# qty    12
# fg     wh
# st     pb
# Sum....
#     qty
# fg
# pd   40
# sg   19
# wh   27
#
# Mean.....
#           qty
# fg
# pd  13.333333
# sg  19.000000
# wh  13.500000
#
# describe...
#              qty
# count   6.000000
# mean   14.333333
# std     3.983298
# min    10.000000
# 25%    11.250000
# 50%    13.500000
# 75%    18.000000
# max    19.000000
#
# St...
# 0    pb
# 1    tn
# 2    mh
# 3    ka
# 4    mh
# 5    wb
# Name: st, dtype: object
#
# df loc 2...
# qty    19
# fg     sg
# st     mh
# Name: 2, dtype: object
#



print(df.drop(99))

#       qty  fg  st
# 98     12  wh  pb
# 2001   19  sg  mh
# 97     10  pd  ka
# 2002   15  wh  mh
# 2005   19  pd  wb

#axis 0 is row and axis 1 is column

print(df.drop('fg', axis=1))
#       qty  st
# 98     12  pb
# 99     11  tn
# 2001   19  mh
# 97     10  ka
# 2002   15  mh
#2005   19  wb

#inplace = True changes the actual obj..so not recommended since all the funcs are returning some new val
