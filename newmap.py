# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:11:30 2020

@author: Oskar_Privatdator
"""

import folium

#Imported for vega
import os 

# Function to load the approriate json file. E.g. GBG = kom_GBG.json
def load_map(data, fn):
    """This function will load the .json file 'fn' , from 'data' location using os package"""
    result = os.path.join(data, fn)
    return result

#Select municipality 
kom_name='Bollnas' 

# select Geojson data using local load_map() function
overlay = load_map('data', 'kom_BOS.json')

#Create map object (with center point at location)
m = folium.Map(location=[62.216915, 15.296679], zoom_start=5)

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
m.save('map.html')

#open map.html in browser