# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:11:30 2020

@author: Oskar_Privatdator
"""

import folium

#Imported for vega
import os 
import json

# Function to load the approriate json file. E.g. GBG = kom_GBG.json
def load_map(data, fn):
    """This function will load the .json file 'fn' , from 'data' location using os package"""
    result = os.path.join(data, fn)
    return result

def load_prop(path, prop_name):
    """This function will load property name 'prop_name' from json 
    file in 'path' as 'path/to/your/file' and return property name """
    data_file= open(path)
    data = json.load(data_file)
    prop = data['features'][0]['properties'][prop_name]
    return prop

# INPUT - but use input instead 
path = 'data/kom_BOS.json'
path2 = 'kom_BOS.json'

# find geo_point_2d
geo_point = load_prop(path, 'geo_point_2d')

# municipality id
kom_name= load_prop(path, 'id')

# select Geojson data using local load_map() function
overlay = load_map('data', path2)

#Create map object (with center point at location)
m = folium.Map(location=geo_point, zoom_start=6)

# Global Tooltip
tooltip = 'Click For More Info'

# Create marker at Gothenburg
folium.Marker([57.708711, 11.974598], 
		popup='<strong>Göteborg</strong>',
		tooltip=tooltip,
		icon=folium.Icon(color= 'green', icon='heart')).add_to(m),
		
# Geojson overlay
folium.GeoJson(overlay, name='selected map', tooltip=tooltip).add_to(m).add_child(folium.Popup(kom_name)).add_to(m)

#Generate map - this will create an html-file to display file
m.save('newmap.html')

#open map.html in browser