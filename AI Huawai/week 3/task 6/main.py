import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# importing needed models.
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# reading data from file.
irish_data = load_iris()
x = irish_data.data
y = irish_data.target

# spliting data into a traing set and test one.
(x_train, x_test, y_train, y_test) = train_test_split(x, y, test_size=0.5)

print(len(x_train), len(x_test), len(y_train), len(y_test))

# building models.
linear_regresion_model = LogisticRegression()
k_neighbors_model = KNeighborsClassifier()
svm_model = SVC()
decision_tree_model = DecisionTreeClassifier()

# fitting models.
linear_regresion_model.fit(x_train, y_train)
k_neighbors_model.fit(x_train, y_train)
svm_model.fit(x_train, y_train)
decision_tree_model.fit(x_train, y_train)

# prediction.
linear_predict = linear_regresion_model.predict(x_test)
k_neighbors_predict = k_neighbors_model.predict(x_test)
svm_predict = svm_model.predict(x_test)
decision_tree_predict = decision_tree_model.predict(x_test)

# accuracy of prediction.
print("Accuracy of LR:", accuracy_score(y_test, linear_predict))
print("Accuracy of KNN:", accuracy_score(y_test, k_neighbors_predict))
print("Accuracy of SVM:", accuracy_score(y_test, svm_predict))
print("Accuracy of DT:", accuracy_score(y_test, decision_tree_predict))