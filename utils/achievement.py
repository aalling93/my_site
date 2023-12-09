import streamlit as st
from .CONSTANTS import *
from .TEXT import *


def click_button():
    st.session_state.clicked = True


def show_achievement_details(achievement_title, details):
    """
    Function to show details of an achievement in a modal-like box.
    """
    if st.button(achievement_title, key=f"button_{achievement_title} details "):
        with st.container():
            st.write(details)
            if st.button(
                "Close", key=f"close_{achievement_title}", on_click=click_button
            ):
                st.experimental_rerun()
                st.button("Click me", key=f"click_{achievement_title}")


def show_volunteer_work(title, year, description, icon, color):
    """
    Function to display volunteer work with a Font Awesome icon before the title.
    """
    colored_title = text_to_color(title, color)
    st.markdown(
        f"<h5 style='margin-bottom:0;'><i class='fas {icon}'></i> {colored_title}</h5>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='color: gray; margin-top:0;'>{year}</p>", unsafe_allow_html=True
    )
    st.write(description)


def show_education_entry(
    year,
    education,
    university,
    gpa,
    focus,
    thesis,
    link,
    extra_info,
    images,
    files,
    skills,
    bullets,
):
    """
    Display an education entry with skills and extra details inside an expander.
    """
    st.markdown(f"<h4>{year} - {education}</h4>", unsafe_allow_html=True)

    # Display bullet points
    for bul in bullets:
        st.markdown(f"- {bul}")

    col1, col2, col3, col4 = st.columns(4)
    col = [col1, col2, col3, col4]
    # for each skill, plotting in its column
    for i in range(len(skills)):
        # when i = 0, if whould be plotted in col1, and when i = 1, col2 etc, so need to map them to the columns
        # if there are more then 4 skills, they should be plotted in a new line..
        col[i].metric("", "", skills[i])

    # Expander for showing extra info
    with st.expander("More about"):
        st.markdown(
            f"<strong>University:</strong> {university}", unsafe_allow_html=True
        )
        st.markdown(f"<strong>GPA:</strong> {gpa}", unsafe_allow_html=True)
        st.markdown(f"<strong>Focus:</strong> {focus}", unsafe_allow_html=True)
        st.markdown(f"<strong>Thesis:</strong> {thesis}", unsafe_allow_html=True)
        if link:
            st.markdown(
                f"<a href='{link}' target='_blank'>More Information</a>",
                unsafe_allow_html=True,
            )
        if extra_info:
            st.markdown(extra_info, unsafe_allow_html=True)
        for image in images:
            if image:
                st.image(image, width=300)
        for file in files:
            if file:
                st.markdown(
                    f"<iframe src='{file}' width='100%' height='600' frameborder='0'></iframe>",
                    unsafe_allow_html=True,
                )


def show_work_experience(
    title, role, period, bullet_points, more_info=None, link=None, uploaded_files=None
):
    """
    Function to display a single work experience entry with additional details.
    """
    with st.container():
        # st.markdown(f"**{title}** - {role} ({period})")
        st.markdown(
            text_to_color(f"**{title}** - {role} ({period})", HEADLINES_COLOR),
            unsafe_allow_html=True,
        )

        for point in bullet_points:
            st.markdown(f"- {point}")

        if more_info or link or uploaded_files:
            with st.expander("See more"):
                if more_info:
                    st.write(more_info)
                if link:
                    st.markdown(f"[More Information]({link})")
                if uploaded_files:
                    for file_name in uploaded_files:
                        st.write(
                            file_name
                        )  # You can modify this to display the files differently


def text_to_color(text, color):
    """
    Return text wrapped in HTML with specified color.
    """
    return f"<span style='color: {color};'>{text}</span>"
