# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:36:59 2018

@author: Jessica
"""
import pandas as pd
import folium

specie = pd.read_csv('asterina_gibbosa.csv')
specie1= pd.read_csv('octopus_vulgaris.csv')

lon, lat = specie['decimalLongitude'], specie['decimalLatitude']
lon1, lat1 = specie1['decimalLongitude'], specie1['decimalLatitude']

dates = specie['eventDate'].astype('str')
dates1 = specie1['eventDate'].astype('str')

m = folium.Map(location=[50, 10], zoom_start=2, tiles='Mapbox Bright', control_scale=True)

feature_group = folium.FeatureGroup(name='Asterina_gibbosa')
feature_group1 = folium.FeatureGroup(name='Octopus_vulgaris')

for lon, lat, dates in zip(lon, lat, dates):
    feature_group.add_child(folium.Marker(location=[lat, lon], popup=dates, icon=folium.Icon(color='pink', icon= 'asterisk')))
for lon1, lat1, dates1 in zip(lon1, lat1, dates1):
    feature_group1.add_child(folium.Marker(location=[lat1, lon1], popup=dates1, icon=folium.Icon(color='green', icon='asterisk')))
    
m.add_child(feature_group)
m.add_child(feature_group1)


folium.LayerControl().add_to(m)

m.save('mapa_oc_ast.html')