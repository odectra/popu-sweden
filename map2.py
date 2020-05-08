#This will be used to create the map of population for each municipal in sweden
import folium
import pandas as pd
import os

kommun = os.path.join('data', 'kommuner.json')
pop_data = os.path.join('data', 'folkmangd.csv')
kommun_data = pd.read_csv(pop_data)

m = folium.Map(location=[48, -102], zoom-start=3)

m.choropleth(
  geo_data=kommun,
  name='choropleths', 
  data=kommun_data,
  columns=['k_ID', 'ar_2019'],
  key_on='feature.ID',
  fill_color='YlGn',
  fill_opacity=0.7,
  line_opacity=0.1,
  legend_name='Antal invanare'
)

folium.LayerControl().add_to(m)

m.save('map2.html')
