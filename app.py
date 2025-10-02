# app.py
import streamlit as st

# --- Global page frame (runs on every rerun) ---
st.set_page_config(page_title="Site", layout="wide")
# with st.sidebar:
#    st.markdown("### Navigation")

# --- Declare only the pages you want visible now ---
# ROOT
frontpage = st.Page("Front_page.py", title="Home", icon="🏠")

# TOP-LEVEL PAGES (pages/*.py)
projects = st.Page("pages/Projects.py", title="Projects", icon="🧪")
publications = st.Page("pages/Publications.py", title="Publications", icon="📚")
# learning = st.Page("pages/Learning.py", title="Learning", icon="🎓")
supervised = st.Page("pages/Supervised_projects.py", title="Supervised projects", icon="👥")
# tutorials = st.Page("pages/Tutorials.py", title="Tutorials", icon="🧭")

# apps_wrapper = st.Page("pages/apps.py", title="Apps", icon="🧩")


# --- Build the navigation menu (only listed pages appear) ---
nav = st.navigation(
    [
        frontpage,
        projects,
        publications,
        supervised,
    ],
    position="sidebar",
)  # or "top"

# --- Run the selected page ---
nav.run()
