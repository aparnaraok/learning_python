from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


iris = load_iris()
x = iris.data[:150]
y = iris.target[:150]

print(x)
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

# lr = LogisticRegression(C=0.1, penalty='l1')
# print(lr.fit(x_train,y_train))

sc = StandardScaler() #To standardise
x_train_std = sc.fit_transform(x_train)
x_test_std = sc.transform(x_test)

pca = PCA(n_components=5)
print("Standardised data", x_train_std)
print(" ")

x_train_pca = pca.fit_transform(x_train_std)
x_test_pca = pca.transform(x_test_std)
print("Principal data >>>", x_train_pca)


lr = LogisticRegression() #l1 and c=0.1
lr.fit(x_train_pca, y_train)

y_pred = lr.predict(x_test_pca)
y_train_pred = lr.predict(x_train_pca)

print("Misclassified in testing >>>", (y_test-y_pred).sum())
print("Misclassified in training >>>", (y_train-y_train_pred).sum())

#Calculate scores
print(lr.score(x_test_pca, y_test))
print(lr.score(x_train_pca, y_train))
