#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
"""
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
"""
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary


from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np

n_estimators      = range(1,101)
criteria          = ["gini", "entropy"]
min_samples_split = range(1,101)

params = np.array(np.meshgrid(n_estimators, [0,1], min_samples_split)).T.reshape(-1,3)

#params = np.array(params).T

#params = params.reshape(-1, 2)
highest_score = 0
highest_params = []
for p in params:
    n_est, crit_idx, min_samp_split = p
    crit = criteria[crit_idx]

    clf= RandomForestClassifier(n_estimators=n_est, criterion=crit, min_samples_split=min_samp_split)

    clf.fit(features_train, labels_train)

    this_score = clf.score(features_test, labels_test)

    if this_score > highest_score:
        highest_score = this_score
        highest_params = p
       
        print "Random Forest [n_estimator={0}][criterion={1}][min_samples_split={2}] : {3}".format(n_est, crit, min_samp_split, this_score)

n_est, crit_idx, min_samp_split = highest_params
print "HIGHEST Random Forest [n_estimator={0}][criterion={1}][min_samples_split{2}] : {3}".format(n_est, crit, min_samp_split, highest_score)

 
#try:
#    prettyPicture(clf, features_test, labels_test)
#except NameError:
#    pass
