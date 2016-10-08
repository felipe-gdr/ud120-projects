#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

data_dict.pop('TOTAL',None)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

highest_sal = 0.0
highest_sal_k = None
for k in data_dict:
    v = data_dict[k]
    if v["salary"] != 'NaN'and v["salary"] > highest_sal and k != 'TOTAL':
        highest_sal = v["salary"]
        highest_sal_k = k
       
print "Highest ---> {0} {1}".format(highest_sal, highest_sal_k)

### your code below
count = 0
for point in data:
    salary = point[0]
    bonus = point[1]
    #print salary, bonus, count
    count += 1
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

