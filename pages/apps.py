import streamlit as st
from utils.achievement import run_tutorial_module

#st.set_page_config(page_title="Apps", layout="wide")
#st.sidebar.title("Apps")
st.sidebar.markdown("## Select a page")
st.image(
    "figures/banners/watercolour/watercolour3.png",
    caption="Credit: Kristian Aalling Sørensen",
    use_container_width="always",
)


tutorial_modules = {
    "Sentinel TLE planning": "pages.apps.Sentinel_TLE_planning",
    "How is Bunaeset doing?": "pages.apps.bunaeset",
}

app_mode = st.sidebar.selectbox(
    "", ["Front page", "Sentinel TLE planning", "Iceberg or Ship?", "Thyra oil platform", "How is Bunaeset doing?"], key="selector_pps_2"
)

if app_mode in tutorial_modules:
    run_tutorial_module(tutorial_modules[app_mode])
