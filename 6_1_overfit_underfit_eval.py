# -*- coding: utf-8 -*-
"""6.1_Overfit_Underfit_Eval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NgDauaeGpe407US8VyjhQ-Lv0ZLkmbQf

# Polynomial Regression -Overfitting

What if your data is actually more complex than a simple straight line? Surprisingly,
you can actually use a linear model to fit nonlinear data. A simple way to do this is to
add powers of each feature as new features, then train a linear model on this extended
set of features. This technique is called Polynomial Regression
"""

# Commented out IPython magic to ensure Python compatibility.
# Some useful Imports

import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
# %matplotlib inline
np.random.seed(42)
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

"""$y = 2 + X + 0.5 * X^2 + noise$"""

# Generate the dataset on which we will test various models.

m = 20
factor = 1.0
X = 6 * np.random.rand(m, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(m, 1)*factor



"""$y = \beta_{0} + \beta_{1}*X$"""

# generate the polynomial features. In this case, since degree is 1, X_poly will be same as X.

degree = 1
poly_features = PolynomialFeatures(degree=degree, include_bias=True)
X_poly = poly_features.fit_transform(X)

# Do the train/test split.

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.20, random_state=42)

# Train the model with the training set.

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Compute the error metrics on the training set.
y_train_hat = lin_reg.predict(X_train)

#Regression Evaluation Metrics
from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_train, y_train_hat))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_train, y_train_hat)))
print('R-squared:', metrics.r2_score(y_train, y_train_hat))

# Compute error metrics on the test set.
y_test_hat = lin_reg.predict(X_test)

print('MAE:', metrics.mean_absolute_error(y_test, y_test_hat))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_test_hat)))
print('R-squared:', metrics.r2_score(y_test, y_test_hat))



"""$y = \beta_{0} + \beta_{1}*X + \beta_{2}* X^2 + ... + \beta_{20}* X^{20}$"""

degree = 20
poly_features = PolynomialFeatures(degree=degree, include_bias=True)
X_poly = poly_features.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.20, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_train_hat = lin_reg.predict(X_train)

print('MAE:', metrics.mean_absolute_error(y_train, y_train_hat))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_train, y_train_hat)))
print('R-squared:', metrics.r2_score(y_train, y_train_hat))

y_test_hat = lin_reg.predict(X_test)

print('MAE:', metrics.mean_absolute_error(y_test, y_test_hat))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_test_hat)))
print('R-squared:', metrics.r2_score(y_test, y_test_hat))



"""$y = \beta_{0} + \beta_{1}*X + \beta_{2}*X^2$"""

degree = 2
poly_features = PolynomialFeatures(degree=degree, include_bias=True)
X_poly = poly_features.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.20, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_train_hat = lin_reg.predict(X_train)

print('MAE:', metrics.mean_absolute_error(y_train, y_train_hat))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_train, y_train_hat)))
print('R-squared:', metrics.r2_score(y_train, y_train_hat))

y_test_hat = lin_reg.predict(X_test)

print('MAE:', metrics.mean_absolute_error(y_test, y_test_hat))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_test_hat)))
print('R-squared:', metrics.r2_score(y_test, y_test_hat))





