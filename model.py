
import sklearn

from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.neighbors import KNeighborsRegressor
from sklearn import tree
import pandas as pd
import numpy as np
import os



x_train = np.array([])
y_train = np.array([])
x_test = np.array([])
y_test = np.array([])


svm_model = svm.SVR()
svm_model.fit(x_train, y_train)
svm_predict = svm_model.predict(x_test)
# get accuracy of the prediction w.r.t y_test.
svm_accuracy = round(accuracy_score(svm_predict, y_test) * 100, 2)

KNN_model = KNeighborsRegressor(n_neighbors=5)
KNN_model.fit(x_train, y_train)
KNN_predict = KNN_model.predict(x_test)
# get accuracy of the prediction w.r.t y_test.
KNN_accuracy = round(accuracy_score(KNN_predict, y_test) * 100, 2)

model_tree = tree.DecisionTreeRegressor()
model_tree.fit(x_train, y_train)
tree_predict = model_tree.predict(x_test)
# get accuracy of the prediction w.r.t y_test.
tree_accuracy = round(accuracy_score(tree_predict, y_test) * 100, 2)
