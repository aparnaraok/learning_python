#entry point to feature selection

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_wine = pd.read_csv('wine.data',header=None)
y = df_wine.iloc[:,0].values
x = df_wine.iloc[:,1:].values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

lr = LogisticRegression(C=0.1, penalty='l1')
print(lr.fit(x_train,y_train))

sc = StandardScaler() #To standardise
x_train_std = sc.fit_transform(x_train)
x_test_std = sc.transform(x_test)

print('training accuracy', lr.score(x_train_std, y_train))
print('test accuracy', lr.score(x_test_std, y_test))

#normaly training accuracy shoulb be more than testing accuracy.


colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'cyan','purple', 'grey', 'white', 'brown', 'magenta']

weights, params = [], []
for c in np.arange(-4., 6.):
    print (c)
    lr = LogisticRegression(penalty='l1', C=10.**c, random_state=0)
    lr.fit(x_train_std, y_train)
    weights.append(lr.coef_[1]) #13 features with 10 val-->10 cross 13 mat
    params.append(10.**c)
#print("Weigths>>>", weights) #least 0 values and negative values decide the play...since it is deriative...if it is less...then that doesn't matter the function.
#last and 9th and 12th
#color is important for selection.

print('training accuracy', lr.score(x_train_std, y_train))
print('test accuracy', lr.score(x_test_std, y_test))

df_wine.columns = ['Class Label', 'Alcohol','Malic acid','Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',\
'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity'\
 	'Hue', 'OD280/OD315 of diluted wines', 'Proline', 'abxc']
print(df_wine.head())


weights = np.array(weights)
#print("Weihts>>>.", weights)

for column, color in zip(range(weights.shape[1]), colors):
    plt.plot(params, weights[:, column],
             label = df_wine.columns[column + 1],
             color = color)
#print(plt.show())

plt.axhline(0, color='black', linestyle='--', linewidth=3)#0thline is dotted and black
#plt.show( )

plt.xlim([10**(-5), 10**5])
#plt.show()
#ax = plt.subplot(111)
plt.ylabel('weight coefficient')
plt.xlabel('C')
plt.xscale('log')
plt.legend(loc = 'upper left')
#ax.legend(loc='upper center', bbox_to_anchor=(1.38, 1.03),nloc=1, fancybox=True)
plt.show()
plt.savefig('log_regr.png')
