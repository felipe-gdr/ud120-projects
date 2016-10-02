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
print "{0}".format(enron_data.itervalues().next())

j_prentice = enron_data["PRENTICE JAMES"] 
print "James Prentice total stock: {0}".format(j_prentice['exercised_stock_options'] + j_prentice['restricted_stock'])

w_colwell = enron_data["COLWELL WESLEY"]
print "Wesley Colwell emails to POIs: {0}".format(w_colwell['from_this_person_to_poi'])

j_skilling = enron_data["SKILLING JEFFREY K"]
print "Jeffrey K Skilling stock options: {0}".format(j_skilling['exercised_stock_options'])

k_lay = enron_data["LAY KENNETH L"]
print "Ken Lay total payments : {0}".format(k_lay['total_payments'])

print "Jeffrey K Skilling total payments: {0}".format(j_skilling['total_payments'])

a_fastow = enron_data["FASTOW ANDREW S"]

print "Andy Fastow total payments: {0}".format(a_fastow['total_payments'])
pois = []

for k in enron_data:
    if enron_data[k]["poi"]:
        pois.append(k)

print "{0} People of Interest in the E+F dataset".format(len(pois))


pois_name_file = sum(1 for line in open('../final_project/poi_names.txt')) - 2

print "{0} People of Interest in the name file".format(pois_name_file)
