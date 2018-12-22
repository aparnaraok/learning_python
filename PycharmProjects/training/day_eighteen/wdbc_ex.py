from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_bc = pd.read_csv('wdbc.data',header=None)
x = df_bc.loc[:, 2:].values
y = df_bc.loc[:, 1].values
le = LabelEncoder()
y = le.fit_transform(y)
print(le.transform(['M', 'B']))

#[1 0]
#Onlyb2 possible field values it can take....m as 1 and B as 0


'''
y = df_bc.iloc[:,0].values
x = df_bc.iloc[:,1:].values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

lr = LogisticRegression(C=0.1, penalty='l1')
print(lr.fit(x_train,y_train))

sc = StandardScaler() #To standardise
x_train_std = sc.fit_transform(x_train)
x_test_std = sc.transform(x_test)

print('training accuracy', lr.score(x_train_std, y_train))
print('test accuracy', lr.score(x_test_std, y_test))
'''