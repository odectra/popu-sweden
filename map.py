# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:44:43 2020

@author: Oskar_Privatdator
"""


import folium

#Imported for vega
import os 

#Create map object (with center point at location)
m = folium.Map(location=[62.216915, 15.296679], zoom_start=5)

# Global Tooltip
tooltip = 'Click For More Info'

#Geojson data
overlay = os.path.join('data', 'kom_AVE.json')

# Create markers 
folium.Marker([57.708711, 11.974598], 
		popup='<strong>Göteborg</strong>',
		tooltip=tooltip,
		icon=folium.Icon(color= 'green', icon='leaf')).add_to(m),
		
# Geojson overlay
#folium.GeoJson(overlay, name='alingsas').add_to(m)
folium.GeoJson(overlay, name='Alingsås').add_to(m)

#Generate map - this will create an html-file to display file
m.save('map.html')

#open map.html in browser