# Suvival prediction of the Titanic.
import pandas as pd
import numpy as np
import random as rnd

import seaborn as sns  # For data visualization.
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC, LinearSVC  # Support Vectors Methods.
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron  # One layer neural network.
from sklearn.linear_model import SGDClassifier  # Stohastic Gradient Desent.
from sklearn.tree import DecisionTreeClassifier

def show_header_and_5_first_last_elements(data):
    print(data.columns)

    print("First 5 elements")
    print(data[:5]) # .head() give the same result.

    print("Last 5 elements")
    print(data[len(data) - 6:])
    print()


def show_data_info(data):
    print(data.info())
    print()

def describe_data(data):
    print(data.describe())
    print()

def describe_char_data(data):
    print(data.describe(include=[object]))
    print()


# Reading train.csv.
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

show_header_and_5_first_last_elements(train_data)
show_header_and_5_first_last_elements(test_data)

# Show data info.
show_data_info(train_data)
show_data_info(test_data)

# Discribe the data.
describe_data(train_data)
describe_data(test_data)

# Character type describtion.
describe_char_data(train_data)
describe_char_data(test_data)

# Survival probability coresponding to each feature.
print(train_data.groupby("Pclass")["Survived"].mean())

# Show if count of sublings are affect to survived persons.
print(train_data.groupby("SibSp")["Survived"].mean().sort_values(ascending=False))

# The survival prob by gender of sublings.
survived_prob_by_sex = train_data.groupby("Sex")["Survived"].mean()
print(survived_prob_by_sex)

# Show histogram of daying people and survived one depends of age.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5)) 
survived_ages = train_data[train_data["Survived"] == 1]["Age"]
unsurvived_ages = train_data[train_data["Survived"] == 0]["Age"]

ax1.hist(survived_ages, bins=20)
ax1.set_title("Setvived = 1")
ax2.hist(unsurvived_ages, bins=20)
ax2.set_title("Setvived = 0")

# plt.show()

# Show histograb acording to Pclass and Survived value.
fig, axes = plt.subplots(3, 2, figsize=(17, 15))
features = [[], [], []]
for i in range(3):
    for j in range(2):
        features[i].append(train_data[(train_data["Survived"] == j) & (train_data["Pclass"] == i + 1)]["Age"])

for i in range(len(features)):
    for j in range(len(features[0])):
        axes[i][j].hist(features[i][j], bins=20)
        axes[i][j].set_title(f"Survived={j} | Pclass={i + 1}")
        axes[i][j].set_xlabel("Age")

plt.show()