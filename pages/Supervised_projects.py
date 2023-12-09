
from utils.achievement import *
import streamlit as st

Victor_Bsc = [
        "pages/supervised_projects/figs/Victor_Bsc.png",
        "brief description of victos project",
    ]

st.set_page_config(page_title = "supervised projects", layout="wide")

st.title("Supervised projects")

col1, col2, col3= st.columns(3)

with col1:
    print_info(Victor_Bsc)
