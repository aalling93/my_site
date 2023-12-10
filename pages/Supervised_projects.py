import streamlit as st

from utils.achievement import print_info, print_project_info 
from pages.supervised_projects.text import SUPERVISED_BSC_PROJECTS, SUPERVISED_MSC_PROJECTS
from utils.CONSTANTS import *


st.set_page_config(page_title = "supervised projects", layout="wide")

st.image(
    "figures/banners/watercolour/watercolour5.png",
    caption="Credit: Kristian Aalling Sørensen",
    use_column_width="always",
)

st.title("Supervised projects")


st.write("I have supervised a number of projects at both BSc. and MSc. level. The projects are listed below. If you are interested in doing a project with me, please contact me at. ")


st.header("Supervised Msc. Eng. projects")
col1, col2, col3= st.columns(3)

with col1:
    for i in range(len(SUPERVISED_MSC_PROJECTS[0 : : 3])):
        print_project_info(SUPERVISED_MSC_PROJECTS[0 : : 3][i])

with col2:
    for i in range(len(SUPERVISED_MSC_PROJECTS[1 : : 3])):
        print_project_info(SUPERVISED_MSC_PROJECTS[1 : : 3][i])

with col3:
    for i in range(len(SUPERVISED_MSC_PROJECTS[2 : : 3])):
        print_project_info(SUPERVISED_MSC_PROJECTS[2 : : 3][i])



st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)


st.header("Supervised BSc. Eng. projects")
col1, col2, col3= st.columns(3)



with col1:
    for i in range(len(SUPERVISED_BSC_PROJECTS[0 : : 3])):
        print_project_info(SUPERVISED_BSC_PROJECTS[0 : : 3][i])

with col2:
    for i in range(len(SUPERVISED_BSC_PROJECTS[1 : : 3])):
        print_project_info(SUPERVISED_BSC_PROJECTS[1 : : 3][i])

with col3:
    for i in range(len(SUPERVISED_BSC_PROJECTS[2 : : 3])):
        print_project_info(SUPERVISED_BSC_PROJECTS[2 : : 3][i])



