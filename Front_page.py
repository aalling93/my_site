import streamlit as st
from utils.achievement import (
    show_achievement_details,
    show_work_experience,
    show_volunteer_work,
    show_education_entry,
    create_wheel_chart,
    text_to_color
)
from utils.TEXT import *
from utils.CONSTANTS import *
import streamlit as st
import json


# Starting the page.
st.set_page_config(page_title = "home page", layout="wide")


st.image(
    "figures/banners/watercolour/watercolour1.png",
    caption="Credit: Kristian Aalling Sørensen",
    use_column_width="always",
)
st.title("Kristian Aalling Sørensen")

colStart1,colStart2 = st.columns([0.8,0.2])



with colStart1:
    st.write(about_me)
    st.write("Still under construction")
    st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)
    

with colStart2:
    st.image("figures/portraet.png", caption="Kristian Aalling Sørensen",)
    st.markdown(
            text_to_color(f"DISCALIMER. This website is mostly about me advertaining myself.   ", EXTRA_TEXT_COLOR),
            unsafe_allow_html=True,
        )


col0, col1, col2, col3, = st.columns([0.2, 0.7, 0.2, 0.2])
col0, col12, col22, col3 = st.columns([0.2, 0.9, 0.3, 0.2])

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







with col12:
    st.title("In my free time")
    fig = create_wheel_chart(free_time_shortnames, free_time_times, free_time_descriptions, "blue")
    st.plotly_chart(fig)



col21, coll22, col23, col24 , col25 = st.columns([0.1, 0.33, 0.11, 0.33, 0.1])






with coll22:
    st.title("Language Proficiency")

    # Display each language with a progress bar
    for language, proficiency in languages.items():
        label = f"{language}: {'Full' if proficiency == 1.0 else 'Improving' if language == 'German' else ''}"
        st.markdown(f"**{label}**")
        st.progress(proficiency)

with col24:
    st.title("Skill")

    # Display each language with a progress bar
    for language, proficiency in techKills.items():
        st.markdown(f"**{language}**")
        st.progress(proficiency)








# Generate footer content based on contact info
def generate_footer(contact_info):
    footer_links = []
    for platform, url in contact_info.items():
        if url:
            link_html = f"<a href='{url}' target='_blank'>{platform}</a>"
            footer_links.append(link_html)
    
    links_str = " | ".join(footer_links)
    footer_content = f"""
    <div style='background-color: lightgrey; padding: 10px; border-radius: 5px; text-align: center;'>
        <h4>Contact Information</h4>
        <p>{links_str}</p>
        <h4>Quick Links</h4>
        <p><a href='#top' target='_self'>Go to Top</a></p>
        <p>&copy; 2023 Kristian Aalling Sørensen</p>
    </div>
    """
    return footer_content


# ... Your app content ...

# Display footer
footer_html = generate_footer(contact_info)
st.markdown(footer_html, unsafe_allow_html=True)






