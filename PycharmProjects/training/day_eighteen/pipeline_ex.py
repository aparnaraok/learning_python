import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df_bc = pd.read_csv('wdbc.data',header=None)
x = df_bc.loc[:, 2:].values
y = df_bc.loc[:, 1].values
le = LabelEncoder()
y = le.fit_transform(y)
print(le.transform(['M', 'B']))


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)
pipe_lr = Pipeline([('scl', StandardScaler()),
                    ('pca' , PCA(n_components=4)),
                    ( 'clf', LogisticRegression(random_state=1, penalty='l1'))])

pipe_lr.fit(x_train, y_train)
print("Training Accuracy %.3f" %pipe_lr.score(x_train, y_train))
print("Testing Accuracy %.3f" %pipe_lr.score(x_test, y_test))

y_pred = pipe_lr.predict(x_test)
print("Misclassified", (y_pred!=y_test).sum()) #Summation

print(confusion_matrix(x_train, y_pred) )
#Inc TPR and dec FPR

#TPR : True Positive
#FPR : False Positive

# [1 0]
# Training Accuracy 0.971
# Testing Accuracy 0.965
# Misclassified 4