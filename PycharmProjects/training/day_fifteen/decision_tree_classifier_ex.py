from sklearn.model_selection import train_test_split
#from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

df_wine = pd.read_csv('wine.data',header=None)
y = df_wine.iloc[:,0].values
x = df_wine.iloc[:,1:].values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

ppn = DecisionTreeClassifier(max_depth=1)
print(ppn.fit(x_train,y_train))

y_pred = ppn.predict(x_test)
y_train_pred = ppn.predict(x_train)

print("misclassified in testing",(y_test-y_pred).sum())
print("misclassified in training",(y_train-y_train_pred).sum())


# DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=1,
#             max_features=None, max_leaf_nodes=None,
#             min_impurity_decrease=0.0, min_impurity_split=None,
#             min_samples_leaf=1, min_samples_split=2,
#             min_weight_fraction_leaf=0.0, presort=False, random_state=None,
#             splitter='best')
# misclassified in testing 20
# misclassified in training 36
