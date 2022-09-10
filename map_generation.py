import pandas as pd
import geopandas
import folium
import folium.plugins
import webbrowser
import csv


#webbrowser.register('chrome',
    #None,
    #webbrowser.BackgroundBrowser("file:///Applications/Google-Chrome.app"))
world_map = folium.Map(zoom_start = 6,
                       location =[51.50251806771501, -0.1139855743343121])


data = pd.read_csv("places.csv")
city = data.iloc[0]

for _, city in data.iterrows():
    if city['stayed overnight'] == 'Y':
        folium.Marker(
            location=[city['latitude'], city['longitude']],
            icon=folium.Icon(color='green'),
            popup=city['year'.lstrip('.0')],
            tooltip=city['place'],

        ).add_to(world_map)
    else:
                folium.Marker(
            location=[city['latitude'], city['longitude']],
            icon=folium.Icon(color='orange'),
            popup=city['year'.lstrip('.0')],
            tooltip=city['place'],

        ).add_to(world_map)

#url = 'travel_map.html'
#webbrowser.get('chrome').open_new_tab(url)

world_map.save("travel_map.html")



