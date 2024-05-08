import numpy as np
import random
import matplotlib.pyplot as plt

def create_y(item):
    return 2 * item + 3 * random.uniform(0.8, 1.0)

# Generating x and y.
x = np.random.rand(10)
y = np.array([create_y(item) for item in x])

# Model of linear regression.
def linear_regression(w, b, x):
    return w * x + b

def mean_squared_error(y_pred, y_true):
    return np.mean((y_pred - y_true) ** 2)

def gradient_descent(w, x, b, y_true, learning_rate=0.01):
    y_pred = linear_regression(w, b, x)
    
    dw = np.mean((y_pred - y_true) * x)
    db = np.mean(y_pred - y_true)
    
    w -= learning_rate * dw
    b -= learning_rate * db
    
    return w, b

# Initialize parameters randomly
w = 1
b = 1

# Perform gradient descent
for _ in range(1000):
    w, b = gradient_descent(w, x, b, y)
    y_pred = linear_regression(w, b, x)
    print(mean_squared_error(y_pred, y))

# Plot the final regression line
plt.scatter(x, y)
plt.plot(x, linear_regression(w, b, x), color='red')
plt.show()
