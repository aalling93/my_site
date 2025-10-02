import streamlit as st
from utils.CONSTANTS import DIVIDER


st.set_page_config(page_title="project", layout="wide")


st.image(
    "figures/banners/watercolour/watercolour3.png",
    caption="Credit: Kristian Aalling Sørensen",
    use_container_width="always",
)
st.title("My Projects")
st.write("If any projects are of interest, please contact me for more information")


col1, col2 = st.columns([0.7, 0.21])
with col1:
    st.image("pages/projects/darkship.png")
with col2:
    st.image("pages/projects/darkship1.png")
    st.image("pages/projects/darkship2.png")

# descripption about the dark ship prject
st.write(
    """ In the realm of maritime surveillance, the Dark Ship project stands out as a cutting-edge initiative aimed at enhancing the security of our seas. Its primary objective is to identify and monitor 'dark ships'—vessels that navigate waters without transmitting Automatic Identification System (AIS) signals, often for reasons like evading detection in illegal activities.

At the heart of this project lies the innovative use of Synthetic Aperture Radar (SAR) satellite imagery. SAR's capability to provide high-resolution, all-weather, day-and-night imagery makes it an invaluable tool for monitoring vast ocean areas. This technology overcomes the limitations of traditional optical imaging, especially in challenging weather conditions or during nighttime.

Complementing SAR's capabilities, the project harnesses the power of Artificial Intelligence (AI). We train sophisticated machine learning models to analyze the SAR data meticulously. These AI algorithms specialize in identifying vessel signatures, effectively distinguishing between ships with active AIS signals and those without.  """
)

st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)


col1, col2 = st.columns([0.21, 0.7])
with col2:
    st.image("pages/projects/bifrost.png")
with col1:
    st.image("pages/projects/bifrost1.png")
    st.image("pages/projects/bifrost2.png")

# descripption about the dark ship prject
st.write(
    """  The Bifrost Project is an innovative initiative in the realm of maritime technology, aiming to revolutionize shipboard operations and security. Its core feature is the integration of advanced Artificial Intelligence (AI) systems directly onto vessels. This project is named 'Bifrost,' metaphorically representing a bridge connecting traditional maritime practices with the future of autonomous and intelligent navigation.

At the forefront of the project is the development and deployment of AI algorithms onboard ships. These algorithms are designed to perform a variety of tasks, from real-time navigation assistance to predictive maintenance of ship components. The AI systems continuously analyze data from various onboard sensors and external sources, such as weather reports and maritime traffic data, to make informed decisions. """
)
st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)


col1, col2 = st.columns([0.24, 0.6])
with col2:
    st.image("pages/projects/trajectory2.png")
with col1:
    st.image("pages/projects/trajectory1.png")


# descripption about the dark ship prject
st.write(
    """  

The AIS Trajectory Prediction Initiative is a groundbreaking project dedicated to enhancing maritime navigation and safety using predictive analytics. The core of this project is centered around the sophisticated analysis of Automatic Identification System (AIS) data, which provides real-time information about a vessel's position, course, and speed.
"""
)

st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)


st.image("pages/projects/anomalies.png")
st.write(
    """ 
OceanGuard is an innovative project designed to address the challenge of illegal activities at sea, such as smuggling, illegal fishing, and unauthorized vessel movements. At the core of this initiative is the use of Automatic Identification System (AIS) data, which is instrumental in monitoring maritime traffic and identifying suspicious behaviors.

Key Features:

AIS Data Analysis: Utilizing AIS data to track vessel movements, speeds, and patterns. The system identifies anomalies or deviations from standard maritime practices, which may indicate illegal activities.
Pattern Recognition: Advanced algorithms and machine learning techniques are employed to recognize patterns typical of illegal operations, such as irregular course changes, loitering in a specific area, or unusual speed variations.
Collaboration with Authorities: The project collaborates with maritime authorities and law enforcement agencies, providing them with real-time alerts and detailed reports on potential illegal activities.
"""
)


st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)
