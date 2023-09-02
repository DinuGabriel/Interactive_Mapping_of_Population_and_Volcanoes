# Import necessary libraries
from turtle import fillcolor  # Unused import, can be removed
import folium
import pandas

# Create a folium map centered at coordinates [38.58, -99.09] with an initial zoom level of 6
# and using "Stamen Terrain" as the base tile layer
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain", min_zoom=3)

# HTML template for volcano information popup on click
html = """<h4>Volcano information:</h4>
Height: %s m
"""

# Read volcano data from a CSV file named "Volcanoes.txt" into a pandas DataFrame
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])

# Define a function to determine marker color based on elevation
def color_producer(elevation):
    if elevation < 2000:
        return "green"
    elif 2000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

# Create feature groups for volcanoes and population data
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

# Loop through the volcano data and add CircleMarkers for each volcano on the map
for lt, ln, el in zip(lat, long, elev):
    # Create an iframe for the popup content with volcano information
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    # Add a CircleMarker for the volcano with appropriate properties
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=folium.Popup(iframe),
                                     fill_color=color_producer(el), color="grey", fill_opacity=0.7))

# Add GeoJson data for world population and apply a style function to determine fill color
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {"fillColor": "green" if x['properties']['POP2005'] < 10000000
                                                       else "orange" if 10000000 <= x['properties']['POP2005'] < 40000000
                                                       else "red"}))

# Add feature groups to the map
map.add_child(fgv)  # Volcanoes layer
map.add_child(fgp)  # Population layer

# Add layer control to the map for toggling layers on/off
map.add_child(folium.LayerControl())

# Save the map as an HTML file
map.save("Map.html")
