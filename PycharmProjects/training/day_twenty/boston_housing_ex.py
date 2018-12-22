import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('housing.data', header=None, sep='\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(df.head())

#sns.set(style='whitegrid', context='notebook')
cols = ['RM', 'TAX', 'PTRATIO', 'LSTAT', 'MEDV']
# sns.pairplot(df[cols], size=2.5)
#plt.tight_layout()
#plt.show()#RM dir prop to MEDV and LSTAT inv prop to MEDV.


cm = np.corrcoef(df[cols].values.T)
# sns.set(font_scale=1.5)
# hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.3f', annot_kws={'size':15}, yticklabels=cols, xticklabels=cols)
#plt.tight_layout()
#plt.show()

x = df[['RM']].values #2d matrix
#print x.shape
y = df['MEDV'].values
def lin_regplot(x, y, model):#x-feature y-target
    plt.scatter(x, y,c='blue')
    plt.plot(x, model.predict(x), color='red')
    return None
slr = LinearRegression()
slr.fit(x, y)
print('Slope : %.3f' %slr.coef_[0])
print('Intercept : %.3f' %slr.intercept_)
lin_regplot(x, y, slr)
plt.xlabel('RM')
plt.ylabel('Price')
plt.show()

# Slope : 9.102
# Intercept : -34.671

#x becomes 0 whn intercept is -34.671.
