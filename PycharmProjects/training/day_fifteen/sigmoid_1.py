import sklearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import pandas as pd

iris = load_iris()
#print(iris)
x = iris.data[50:150,2:4] #[:100]
y=iris.target[50:150]#[0:100]

# print(x,y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

# print(x_train,x_test,y_train,y_test)
# print(x_train.size)
# print(x_train.shape)

ppn = Perceptron(max_iter=20,eta0=0.1)
print(ppn.fit(x_train,y_train))

y_pred = ppn.predict(x_test)
y_train_pred = ppn.predict(x_train)

print("misclassified in testing",(y_test-y_pred).sum())
print("misclassified in training",(y_train-y_train_pred).sum())

new_data = pd.DataFrame([{'petal length (cm)':4.7,
                          'petal width (cm)':1.4},
                         {'petal length (cm)':5.1,
                          'petal width (cm)':1.8}])

new_data = new_data[['petal length (cm)','petal width (cm)']]

new_pred = ppn.predict(new_data)

new_data['label'] = new_pred

print(new_data)
