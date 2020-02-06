
import sklearn

from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.linear_model import LinearRegression
# Import train_test_split function
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn import tree
import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

tweetsWithDifferences = pd.read_csv('dataSet_differences.csv')
X = tweetsWithDifferences[['0', '1', '2', '3', '4', '5']]
y = tweetsWithDifferences[['AAL', 'ACB', 'AMD', 'BA', 'GD',
                           'GOOG', 'LMT', 'MU', 'NOC', 'NRT', 'RTN', 'USO', 'ZN', '^GSPC']]
y = tweetsWithDifferences[['^GSPC']]

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2)


linReg_model = LinearRegression(fit_intercept=False)
linReg_model.fit(x_train, y_train)
linReg_predict = linReg_model.predict(x_test)
MSE = mean_squared_error(y_test, linReg_predict)
# optimal_weight = reg.coef_
# optimal_weight = optimal_weight.reshape(-1, 1)
# print(optimal_weight)
print("\nThe LinReg training error is ", MSE)


KNN_model = KNeighborsRegressor(n_neighbors=5)
KNN_model.fit(x_train, y_train)
KNN_predict = KNN_model.predict(x_test)
MSE = mean_squared_error(y_test, KNN_predict)
print("\nThe KNN training error is ", MSE)


model_tree = tree.DecisionTreeRegressor()
model_tree.fit(x_train, y_train)
tree_predict = model_tree.predict(x_test)
MSE = mean_squared_error(y_test, tree_predict)
print("\nThe DTree training error is ", MSE)


# Plot for fun
x = np.arange(0, len(y_test), 1)
f, axes = plt.subplots(2, 2, figsize=(10, 10), sharex=True)
axes[0, 0].plot(x, y_test, label='y_test')
axes[0, 0].plot(x, linReg_predict, label='y_predict')
axes[0, 0].set_title('Linear Regression')
axes[0, 0].legend()
axes[0, 1].plot(x, y_test, label='y_test')
axes[0, 1].plot(x, KNN_predict, label='y_predict')
axes[0, 1].set_title('KNN Regression')
axes[0, 1].legend()
axes[1, 0].plot(x, y_test, label='y_test')
axes[1, 0].plot(x, tree_predict, label='y_predict')
axes[1, 0].set_title('Decision Tree Regression')
axes[1, 0].legend()
plt.tight_layout()
plt.show()
