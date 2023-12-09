# Example structure for roboflow_annotation.py
import streamlit as st

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

