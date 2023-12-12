import streamlit as st
import sys
#sys.path.append("../../utils/")
from utils.achievement import *
from utils.CONSTANTS import DIVIDER
import importlib 
import streamlit as st
import folium
from streamlit_folium import folium_static
import branca


def run():
    
    st.title("How is Bunaeset doing?")
    st.write("This page is under construction")
    col1,col2, col3 = st.columns([0.3, 0.7, 0.1])


    st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)
    with col1:

        st.title("\n\n\n\n\n\nLocation")
    with col2:
        center = [59.971870, 12.395627] # Replace with your desired coordinates
        zoom = 15 # Replace with your desired zoom level
        m = folium.Map(location=center, zoom_start=zoom)
        folium_static(m)

    st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)


    col1,col2, col3 = st.columns([0.3, 0.7, 0.1])
    





