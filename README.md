# Interactive Population and Volcano Map

This project creates an interactive map that displays volcano locations and population data. It uses the Folium library for mapping and visualization, along with pandas for data manipulation.

## Project Overview

The interactive map is designed to visualize the following:

- Volcano locations with elevation information.
- World population data, categorized by population density.

## Features

- Volcano markers with pop-up information.
- Population data with different colors indicating population density.

## Prerequisites

Before running the code, make sure you have the following:

- Python 3.x
- Required Python libraries: Folium, pandas

## Getting Started

1. Clone or download this repository to your local machine.
2. Install the necessary Python libraries using pip:
3. Run the Python script `create_map.py` to generate the interactive map.

## Data Sources

- Volcano data is loaded from a CSV file named `Volcanoes.txt`.
- World population data is sourced from a GeoJSON file named `world.json`.

## Usage

- Open the generated `Map.html` file in a web browser to interact with the map.
- Use the layer control to toggle between volcano locations and population data.

## Customization

You can customize the map by modifying the following:

- Marker colors based on elevation in `color_producer` function.
- Population density color categories in the GeoJson style function.
