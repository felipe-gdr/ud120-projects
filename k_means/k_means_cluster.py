#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "r", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )



### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)

f1A,f2A = [],[]

max_stock_opt,min_stock_opt,max_sal,min_sal=0.0,999999999.0,0,99999999
for f1, f2 in finance_features:
    if f2 > max_stock_opt:
        max_stock_opt = f2
    if f2 < min_stock_opt and f2 != 0:
        min_stock_opt = f2
  
    if f1 > max_sal:
        max_sal = f1
    if f1 < min_sal and f1 != 0:
        min_sal = f1

    plt.scatter( f1, f2 )

    # add values to 2 dimensional arrays
    f1A.append([f1])
    f2A.append([f2])
    
plt.show()

# create numpy arrays
f1A = numpy.array(f1A)
f2A = numpy.array(f2A)

from sklearn.preprocessing import MinMaxScaler
# Salary Scaling
scaler1  = MinMaxScaler(feature_range=(0,1))
salScale = scaler1.fit_transform(f1A)


print (200000-scaler1.data_min_)/(scaler1.data_max_-scaler1.data_min_)

# Stock Options Scaling
scaler2 = MinMaxScaler()
stockScale = scaler2.fit_transform(f2A)

print (1000000-scaler2.data_min_)/(scaler2.data_max_-scaler2.data_min_)

#print salScale, round(salScale[34][0],2)

print "max stock options={0}. min stock options={1}".format(max_stock_opt,min_stock_opt)

print "max salary={0}. min salary={1}".format(max_sal,min_sal)

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans

pred = KMeans(n_clusters=2,random_state=0).fit(finance_features).predict(finance_features)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters_2.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
