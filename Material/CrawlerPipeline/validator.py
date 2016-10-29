from extractor import extract_data
from sklearn import svm
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = extract_data()
clf = svm.LinearSVC()
clf.fit(X_train, y_train)

print("training accuracy: " + str(accuracy_score(y_train, clf.predict(X_train))))
print("testing accuracy: " + str(accuracy_score(y_test, clf.predict(X_test))))
