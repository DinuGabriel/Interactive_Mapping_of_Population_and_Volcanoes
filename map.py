from turtle import fillcolor
import folium
import pandas 

map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain", min_zoom = 3)

html = """<h4>Volcano information:</h4>
Height: %s m
"""

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 2000:
        return "green"
    elif 2000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

fgv = folium.FeatureGroup(name = "Volcanoes")
fgp = folium.FeatureGroup(name = "Population")

for lt, ln, el in zip(lat, long, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 10, popup=folium.Popup(iframe), fill_color = color_producer(el), color = "grey", fill_opacity = 0.7))

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function = lambda x: {"fillColor":"green" if x['properties']['POP2005'] < 10000000 
else "orange" if 10000000 <= x['properties']['POP2005'] < 40000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")