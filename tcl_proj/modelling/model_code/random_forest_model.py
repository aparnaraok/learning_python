'''*************************************************************************************************************
@summary  : Script to implement Random Forest Algorithm
@author   : Aparna Rao Kota
*************************************************************************************************************'''
import logging
import logging.config
import os
import pandas
from pandas import read_csv

logging.config.fileConfig("logging.conf")
# create logger
logger = logging.getLogger("modelLogger")


class RandomForestModel:
    def __init__(self):
        '''Initializing
        '''
        print("Initializing the RF model....")

    def perform_random_forest(self):
        '''Performs the Random Forest algorithm
        '''
        logging.info("Performing the Random Forest algorithm..........")
        # path = "C:\\Users\\IT\\PycharmProjects\\my_project\\modelling"
        path = os.getcwd()
        data_set_path = os.path.join(path, "data_set", "iris.csv")
        # headernames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'variety']
        dataset = read_csv(data_set_path)
        dataset.head()
        logging.info("The shape of the data fetched is : : %s", dataset.shape)

        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, 4].values

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

        from sklearn.ensemble import RandomForestClassifier
        classifier = RandomForestClassifier(n_estimators=50)
        classifier.fit(X_train, y_train)

        y_pred = classifier.predict(X_test)

        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        result = confusion_matrix(y_test, y_pred)

        result1 = classification_report(y_test, y_pred)
        return result, result1

# rfm = RandomForestModel()
# rfm.perform_random_forest()