import pandas as pd

df_wine = pd.read_csv(r'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header = None)
df_wine.columns = ['Type','Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash','Mg', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', '0D280/0D315 of diluted wine', 'Proline' ]
print(df_wine.head()) #head returns first 5 rows and 14 cols

#  Type  Alcohol   ...     0D280/0D315 of diluted wine  Proline
# 0     1    14.23   ...                            3.92     1065
# 1     1    13.20   ...                            3.40     1050
# 2     1    13.16   ...                            3.17     1185
# 3     1    14.37   ...                            3.45     1480
# 4     1    13.24   ...                            2.93      735

#[5 rows x 14 columns]
#first one is just type...data starts from second col oly.

data = df_wine.iloc[:,1:].values  #iloc always takes index val
#loc takes index names
print (data)


#prnts everything in matrix format...

# [[1.423e+01 1.710e+00 2.430e+00 ... 1.040e+00 3.920e+00 1.065e+03]
#  [1.320e+01 1.780e+00 2.140e+00 ... 1.050e+00 3.400e+00 1.050e+03]
#  [1.316e+01 2.360e+00 2.670e+00 ... 1.030e+00 3.170e+00 1.185e+03]
#  ...
#  [1.327e+01 4.280e+00 2.260e+00 ... 5.900e-01 1.560e+00 8.350e+02]
#  [1.317e+01 2.590e+00 2.370e+00 ... 6.000e-01 1.620e+00 8.400e+02]
#  [1.413e+01 4.100e+00 2.740e+00 ... 6.100e-01 1.600e+00 5.600e+02]]
