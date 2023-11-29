import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, confusion_matrix


def decision_tree(datapath):
    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    classifier = DecisionTreeClassifier(random_state=0)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    return cm, r2_score(y_test, y_pred)


def knn(datapath):
    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    return cm, r2_score(y_test, y_pred)


def kernel_svm(datapath):

    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    classifier = SVC(kernel='rbf', random_state=0)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    return cm, r2_score(y_test, y_pred)


def random_forest(datapath):
    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    return cm, r2_score(y_test, y_pred)


def svm(datapath):
    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    classifier = SVC(kernel='linear', random_state=0)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    return cm, r2_score(y_test, y_pred)


def logistic_reg(datapath):
    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    classifier = LogisticRegression(random_state=0)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    return cm, r2_score(y_test, y_pred)


def naive_bayes(datapath):

    dataset = pd.read_csv(datapath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    return cm, r2_score(y_test, y_pred)


data = "C:/Users/sethg/Documents/Python Lessons/5_Data analysist courses/Machine learning course/Selecting the best model/Classification/Data.csv"

decTree = decision_tree(data)
k = knn(data)
kernel = kernel_svm(data)
ranFor = random_forest(data)
s = svm(data)
logReg = logistic_reg(data)
nBay = naive_bayes(data)

print("Decision tree:\nConfusion matrix\n", decTree[0], "\nAccuracy:", decTree[1])
print("\nKNN:\nConfusion matrix\n", k[0], "\nAccuracy", k[1])
print("\nKernel SVM:\nConfusion matrix\n", kernel[0], "\nAccuracy:", kernel[1])
print("\nRandom Forest:\nConfusion matrix\n", ranFor[0], "\nAccuracy:", ranFor[1])
print("\nSVM:\nConfusion matrix\n", s[0], "\nAccuracy:", s[1])
print("\nLogistic Regression:\nConfusion matrix\n", logReg[0], "\nAccuracy:", logReg[1])
print("\nNaive Bays:\nConfusion matrix\n", nBay[0], "\nAccuracy:", nBay[1])
