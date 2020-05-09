# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:13:10 2020

@author: Oskar_Privatdator
"""


import json

#path=r'data/kom_ALI.json'

#with open(path) as data_file:
#    data = json.load(data_file)

# Print kom_namn from json file properties
#print(data['features'][0]['properties']['kom_namn'])

# Print coordinate from json file properties
#print(data['features'][0]['properties']['geo_point_2d'])

def load_json(path, prop_name):
    """This function will load json file from 'path' in format r'data/kom_ALI.json' and the property name 'prop_name' """
    data_file= open(path)
    data = json.load(data_file)
    prop = data['features'][0]['properties'][prop_name]
    return prop

print(load_json(r'data/kom_ALI.json', 'geo_point_2d'))
