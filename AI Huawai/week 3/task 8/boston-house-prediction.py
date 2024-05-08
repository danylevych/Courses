import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import seaborn as sns

from scipy.stats import norm

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score
# from sklearn.datasets import load_boston # load_boston was removed

from sklearn.linear_model import RidgeCV, LassoCV, LinearRegression, ElasticNet
from sklearn.svm import SVR

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor


# Load dataset.
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
x = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
y = raw_df.values[1::2, 2]

print(y)

data_df = pd.DataFrame(x, columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])
target_df = pd.DataFrame(y)

print(data_df.head())

target_values = np.array(y)

# sns.set(style="whitegrid")

# Create a figure and axis objects
plt.figure(figsize=(8, 6))

# Plot histogram with density curve
sns.histplot(target_values, kde=True, bins=40, color='g', stat='density')

# Show plot
plt.title('Distribution of Label')
plt.xlabel('Label')
plt.ylabel('Density')
#plt.show()

# Spliting the data.
(x_train, x_test, y_train, y_test) = train_test_split(x, y, test_size=0.3)

scaler = StandardScaler()
x = scaler.fit_transform(x, y)[:5]
print(x[:3])

# Define regression models
linear_regression_model = LinearRegression()
ridge_model = RidgeCV()
lasso_model = LassoCV()
random_forest_model = RandomForestRegressor()  # Changed to RandomForestRegressor
gbdt_model = GradientBoostingRegressor()  # Changed to GradientBoostingRegressor
elastic_net_model = ElasticNet()
xg_model = XGBRegressor()

# Fit the models
linear_regression_model.fit(x_train, y_train)
ridge_model.fit(x_train, y_train)
lasso_model.fit(x_train, y_train)
random_forest_model.fit(x_train, y_train)  # Use RandomForestRegressor
gbdt_model.fit(x_train, y_train)  # Use GradientBoostingRegressor
elastic_net_model.fit(x_train, y_train)
xg_model.fit(x_train, y_train)

# Predict using the trained models
linear_predict = linear_regression_model.predict(x_test)
ridge_predict = ridge_model.predict(x_test)
lasso_predict = lasso_model.predict(x_test)
random_forest_predict = random_forest_model.predict(x_test)
gbdt_predict = gbdt_model.predict(x_test)
elastic_net_predict = elastic_net_model.predict(x_test)
xg_predict = xg_model.predict(x_test)

# Evaluate and print results
print("LinearRegression R^2 Score: ", r2_score(y_test, linear_predict))
print("RidgeCV R^2 Score: ", r2_score(y_test, ridge_predict))
print("LassoCV R^2 Score: ", r2_score(y_test, lasso_predict))
print("RandomForestRegressor R^2 Score: ", r2_score(y_test, random_forest_predict))
print("GradientBoostingRegressor R^2 Score: ", r2_score(y_test, gbdt_predict))
print("ElasticNet R^2 Score: ", r2_score(y_test, elastic_net_predict))
print("XGBRegressor R^2 Score: ", r2_score(y_test, xg_predict))

param_grid = {
    'kernel': ['rbf', 'poly', 'sigmoid'],
    'C': [0.1, 1, 10],
    'gamma': ['scale', 'auto']
}

# Initialize SVR model
svr = SVR()

# Initialize GridSearchCV
grid_search_model = GridSearchCV(estimator=svr, param_grid=param_grid, cv=2, n_jobs=-1)

# Perform grid search
grid_search_model.fit(x_train, y_train)

# Print the best parameters
print("Optimal parameter list:", grid_search_model.best_params_)

# Get the best model
best_model = grid_search_model.best_estimator_
print("Optimal model:", best_model)

# Evaluate the best model on the test set and print the R2 score
y_pred = best_model.predict(x_test)
r2 = r2_score(y_test, y_pred)
print("Optimal R2 value:", r2)
