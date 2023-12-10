import streamlit as st

from utils.achievement import print_info, print_project_info 
from pages.publications.text import PEER_REVIWED_PUBLICATIONS
from utils.CONSTANTS import *


st.set_page_config(page_title = "Publications", layout="wide")



st.image(
    "figures/banners/watercolour/watercolour4.png",
    caption="Credit: Kristian Aalling Sørensen",
    use_column_width="always",
)


st.header("Peer-reviewed Publications")
col1, col2, col3= st.columns(3)

with col1:
    for i in range(len(PEER_REVIWED_PUBLICATIONS[0 : : 3])):
        print_project_info(PEER_REVIWED_PUBLICATIONS[0 : : 3][i])

with col2:
    for i in range(len(PEER_REVIWED_PUBLICATIONS[1 : : 3])):
        print_project_info(PEER_REVIWED_PUBLICATIONS[1 : : 3][i])

with col3:
    for i in range(len(PEER_REVIWED_PUBLICATIONS[2 : : 3])):
        print_project_info(PEER_REVIWED_PUBLICATIONS[2 : : 3][i])



st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)