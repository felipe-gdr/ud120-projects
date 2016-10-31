#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

print "Score of Decision Tree after split: {0}".format(clf.score(X_test, y_test))

print "Number of POIs in the test set: {0}".format(len([x for x in y_test if x == 1.0]))

print "Total number of people in the test set: {0}".format(len(y_test))

from sklearn.metrics import confusion_matrix
from numpy import array 
pred = clf.predict(X_test)

print confusion_matrix(array(y_test), pred, labels=["POI", "NPOI"])
print "predicted\t: {0}".format(pred)
print "actual\t\t: {0}".format(array(y_test))

from sklearn.metrics import recall_score
from sklearn.metrics import precision_score


print "Recall score: {0}".format(recall_score(y_test, pred))

print "Precision score: {0}".format(precision_score(y_test, pred))
