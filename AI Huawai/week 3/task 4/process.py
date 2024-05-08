# Suvival prediction of the Titanic.
import pandas as pd
import numpy as np
import random as rnd

import seaborn as sns  # For data visualization.
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

# Reading train.csv.
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# Combining the lost data.
combined_data = pd.concat([train_data, test_data], ignore_index=True)

# Check for missing value.
print(combined_data.isnull().sum())

# Fill the missing values with data.
train_data["Fare"] = train_data["Fare"].fillna(train_data["Fare"].mode()[0]) # mode() returns the value that we occurs most friquent.
train_data["Embarked"] = train_data["Embarked"].fillna(train_data["Embarked"].mode()[0])
train_data["Age"] = train_data["Age"].fillna(train_data["Age"].mean()) # Fill the lost age as avarege age.

train_data["Sex"] = train_data["Sex"].replace({'male': 0, 'female': 1})
train_data = train_data[["Survived", "Pclass", "Sex", "Age", "SibSp", "Fare"]]
target = train_data["Survived"]


# Model creation.
(train_x, test_x, train_y, test_y)  = train_test_split(train_data, target, test_size=0.05, random_state=42)

logistic_model = LogisticRegression()
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
adda_model = AdaBoostClassifier(n_estimators=100, random_state=42, algorithm='SAMME')

# train models
logistic_model.fit(train_x, train_y)
rf_model.fit(train_x, train_y)
adda_model.fit(train_x, train_y)

logistic_predict = logistic_model.predict(test_x)
rf_predict = rf_model.predict(test_x)
adda_predict = adda_model.predict(test_x)

print("LogisticRegression accuracy:", accuracy_score(test_y, logistic_predict))
print("RandomForestClassifier accuracy:", accuracy_score(test_y, rf_predict))
print("AdaBoostClassifier accuracy:", accuracy_score(test_y, adda_predict))