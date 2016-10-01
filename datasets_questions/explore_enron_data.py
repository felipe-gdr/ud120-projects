#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "{0} people in the dataset".format(len(enron_data))
print "{0} features per person".format(len(enron_data.itervalues().next()))
#print "{0}".format(enron_data.itervalues().next())

pois = []
for k in enron_data:
    if enron_data[k]["poi"]:
        pois.append(k)

print "{0} People of Interest in the E+F dataset".format(len(pois))


pois_name_file = sum(1 for line in open('../final_project/poi_names.txt')) - 2

print "{0} People of Interest in the name file".format(pois_name_file)
