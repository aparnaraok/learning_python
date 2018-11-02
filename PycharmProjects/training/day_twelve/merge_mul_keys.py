#Merging with multiple keys

import pandas as pd

left = pd.DataFrame({'st':['KA', 'KA', 'KL', 'TN'],
                     'fg':['pd', 'wh', 'pd', 'pd'],
                     'lqty':[12, 11, 14, 10]})
right = pd.DataFrame({'st':['KA', 'KA', 'KL','KL'],
                     'fg':['pd', 'pd', 'pd', 'cn'],
                     'rqty':[5, 7, 6, 4]})

#print(pd.merge(left, right, on='st')) #takes common ele of fd and matches left and right
#print(pd.merge(left, right, on='st', suffixes=('_left', '_right'))) #takes common ele of fd and matches left and right
print(pd.merge(left, right, on=['st', 'fg'], suffixes=('_left','_right'))) #takes common ele of fd and matches left and right



#fg removed TN (oly pd is common..no wh and cn)
# st_x  fg  lqty st_y  rqty
# 0   KA  pd    12   KA     5
# 1   KA  pd    12   KA     7
# 2   KA  pd    12   KL     6
# 3   KL  pd    14   KA     5
# 4   KL  pd    14   KA     7
# 5   KL  pd    14   KL     6


#  st fg_x  lqty fg_y  rqty
# 0  KA   pd    12   pd     5
# 1  KA   pd    12   pd     7
# 2  KA   wh    11   pd     5
# 3  KA   wh    11   pd     7
# 4  KL   pd    14   pd     6
# 5  KL   pd    14   cn     4



#st

#    st fg_x  lqty fg_y  rqty
# 0  KA   pd    12   pd     5
# 1  KA   pd    12   pd     7
# 2  KA   wh    11   pd     5
# 3  KA   wh    11   pd     7
# 4  KL   pd    14   pd     6
# 5  KL   pd    14   cn     4


#merging(fg,st)

#  st  fg  lqty  rqty
# 0  KA  pd    12     5
# 1  KA  pd    12     7
# 2  KL  pd    14     6


#with suffixes (possible only for one common index others too)

#  st fg_left  lqty fg_right  rqty
# 0  KA      pd    12       pd     5
# 1  KA      pd    12       pd     7
# 2  KA      wh    11       pd     5
# 3  KA      wh    11       pd     7
# 4  KL      pd    14       pd     6
# 5  KL      pd    14       cn     4