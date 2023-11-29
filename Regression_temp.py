import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


def multiple_linear_regression(datapath):
    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    return r2_score(y_test, y_pred)


def polynomial_regression(datapath):
    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X_train)
    regressor = LinearRegression()
    regressor.fit(X_poly, y_train)

    y_pred = regressor.predict(poly_reg.transform(X_test))

    return r2_score(y_test, y_pred)


def svr(datapath):
    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    y = y.reshape(len(y), 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    y_train = sc_y.fit_transform(y_train)

    regressor = SVR(kernel='rbf')
    regressor.fit(X_train, y_train)

    y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(X_test)))

    return r2_score(y_test, y_pred)


def decision_tree(datapath):
    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    return r2_score(y_test, y_pred)


def random_forest(datapath):
    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    regressor = RandomForestRegressor(n_estimators=10, random_state=0)
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    return r2_score(y_test, y_pred)




data = "C:/Users/sethg/Documents/Python Lessons/5_Data analysist courses/Machine learning course/Selecting the best model/Regression/Data.csv"
print("Linear regression:", multiple_linear_regression(data))
print("Polynomial regression : ", polynomial_regression(data))
#print("SVR: ", svr(data))
print("Decision tree: ", decision_tree(data))
print("Random forest: ", random_forest(data))
