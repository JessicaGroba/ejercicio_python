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

m = folium.Map(location=[50, 10], zoom_start=2, tiles='Mapbox Bright')