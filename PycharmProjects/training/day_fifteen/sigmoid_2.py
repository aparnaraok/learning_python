from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import pandas as pd

df_wine = pd.read_csv('wine.data',header=None)
y = df_wine.iloc[:,0].values
x = df_wine.iloc[:,1:].values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

ppn = Perceptron(max_iter=20,eta0=0.1)
print(ppn.fit(x_train,y_train))

y_pred = ppn.predict(x_test)
y_train_pred = ppn.predict(x_train)

print("misclassified in testing",(y_test-y_pred).sum())
print("misclassified in training",(y_train-y_train_pred).sum())