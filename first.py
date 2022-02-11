import pandas as pd
import streamlit as st
import altair as alt
from streamlit_folium import folium_static
import folium
from branca.colormap import linear, LinearColormap

st.header("Climate Changes Between 1980-2020")
st.write("""
Climate change has had highly variable effects in different places.
This dashboard lets you see the climate impacts so far. For each city, you can see changes in
1. Daily high temperatures 
2. Daily low temperatures
3. Total precipitation
Use the map for quick comparisons. Then use the menu at the bottom to drill into single city data.
Results are aggregations of [this raw daily weather data](https://docs.opendata.aws/noaa-ghcn-pds/readme.html). This page doesn't show extreme weather events. Changes in extreme weather are more important, but that topic deserves a more detailed review than this page.
""")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
