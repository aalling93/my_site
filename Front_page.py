# import sys
# sys.path.append("../my_site")
# sys.path.append("../src")
# import streamlit.components.v1 as components
#

import streamlit as st
from streamlit_timeline import st_timeline
from utils.achievement import (
    show_achievement_details,
    show_work_experience,
    show_volunteer_work,
    show_education_entry,
)


from utils.TEXT import *
from utils.CONSTANTS import *

st.image(
    "/Users/kaaso/Documents/coding/portfolio/src/my_site/figures/banners/watercolour/watercolour1.png",
    caption="Sunrise by the mountains",
    use_column_width="always",
)


st.title("Kristian Aalling Sørensen")
st.subheader("Some would even call me a Satellite and AI Expert")
st.write(about_me)


col1, col2 = st.columns([0.9, 0.3])
col12, col22 = st.columns([0.9, 0.3])

with col1:
    st.title("Work Experience")
    for experience in work_experiences:
        show_work_experience(
            experience["title"],
            experience["role"],
            experience["period"],
            experience["bullet_points"],
            experience.get("more_info"),
            experience.get("link"),
            experience.get("uploaded_info"),
        )


with col2:
    st.subheader("My Achievements")
    # Display buttons for each achievement
    for title, details in achievements.items():
        show_achievement_details(title, details)

    st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)
    st.subheader("Volunteer work")

    for work in volunteer_works:
        show_volunteer_work(
            work["title"],
            work["year"],
            work["description"],
            work["icon"],
            HEADLINES_COLOR,
        )
    st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)

with col12:
    st.title("Education")
    for edu in education_data:
        show_education_entry(**edu)
        st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)
