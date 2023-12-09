# Example structure for roboflow_annotation.py
import streamlit as st
import sys
#sys.path.append("../../utils/")
from utils.achievement import *


def run():
    st.title("Roboflow Annotation Tutorial")
    # Your tutorial code goes here
    st.write("Content of Roboflow Annotation tutorial...")
    # More tutorial content
    st.write("Content of Roboflow Annotation tutorial...")
    st.write("Content of Roboflow Annotation tutorial...")


    animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

    animal = st.text_input('Type an animal')

    if st.button('Check availability'):
        have_it = animal.lower() in animal_shelter
        'We have that animal!' if have_it else 'We don\'t have that animal.'


    


    # Example usage
    info_list = [
        "This is some introductory text.",
        "figures/banners/watercolour/watercolour1.png",
        "Some more text here.",
        "figures/banners/watercolour/watercolour1.png"
    ]

    info_list2 = [
        "Different text for column 2.",
        "figures/banners/watercolour/watercolour1.png"
    ]

    col1, col2 = st.columns(2)

    with col1:
        print_info(info_list)

    with col2:
        print_info(info_list2)



