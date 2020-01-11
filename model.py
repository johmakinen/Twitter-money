
import sklearn

from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn import tree
import pandas as pd
import numpy as np
import os

tweetsWithDifferences = pd.read_csv('dataSet_differences.csv')
X = tweetsWithDifferences[['0', '1', '2', '3', '4', '5']]
y = tweetsWithDifferences[['AAL','ACB','AMD','BA','GD','GOOG','LMT','MU','NOC','NRT','RTN','USO','ZN','^GSPC']]

partIndex = np.floor(0.8*X.shape[0])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)


reg = LinearRegression(fit_intercept=False) 
reg = reg.fit(x_train, y_train)

training_error = mean_squared_error(y_test, reg.predict(x_test))
optimal_weight = reg.coef_
optimal_weight = optimal_weight.reshape(-1,1)
print(optimal_weight)
print("\nThe resuling training error is ",training_error)



KNN_model = KNeighborsRegressor(n_neighbors=5)
KNN_model.fit(x_train, y_train)
KNN_predict = KNN_model.predict(x_test)
training_error = mean_squared_error(y_test, KNN_predict)
print("\nThe KNN training error is ",training_error)
# get accuracy of the prediction w.r.t y_test.

model_tree = tree.DecisionTreeRegressor()
model_tree.fit(x_train, y_train)
tree_predict = model_tree.predict(x_test)
training_error = mean_squared_error(y_test, tree_predict)
print("\nThe tree training error is ",training_error)
# get accuracy of the prediction w.r.t y_test.