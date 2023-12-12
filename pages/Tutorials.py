import streamlit as st
from utils.achievement import run_tutorial_module, display_tutorial

st.set_page_config(page_title="tutorials", layout="wide")


st.image(
    "figures/banners/watercolour/watercolour2.png",
    caption="Credit: Kristian Aalling Sørensen",
    use_column_width="always",
)
st.title("Placeholder page. Not implemented..")

st.write("Page for tutorials, theory, and other stuff")


st.sidebar.title("Pages")
st.sidebar.markdown("## Select a pages")

app_mode = st.sidebar.selectbox(
    "", ["Roboflow Annotation", "AI Projects", "Projects", "Front Page"], key="tutorials_selector"
)

tutorial_modules = {
    "Roboflow Annotation": "pages.tutorial_tabs.roboflow_annotation",
    # Add other mappings for your tutorials
}


if app_mode in tutorial_modules:
    run_tutorial_module(tutorial_modules[app_mode])


# Dummy data for tutorials (Replace with your actual data)
tutorials = [
    {
        "image": "figures/banners/watercolour/watercolour1.png",
        "description": "Tutorial 1 Description",
    },
    {
        "image": "figures/banners/watercolour/watercolour1.png",
        "description": "Tutorial 2 Description",
    },
    {
        "image": "figures/banners/watercolour/watercolour1.png",
        "description": "Tutorial 3 Description",
    },
    {
        "image": "figures/banners/watercolour/watercolour1.png",
        "description": "Tutorial 4 Description",
    },
    {
        "image": "figures/banners/watercolour/watercolour1.png",
        "description": "Tutorial 1 Description",
    },
    {
        "image": "figures/banners/watercolour/watercolour1.png",
        "description": "Tutorial 2 Description",
    },
    {
        "image": "figures/banners/watercolour/watercolour1.png",
        "description": "Tutorial 3 Description",
    },
    {
        "image": "figures/banners/watercolour/watercolour1.png",
        "description": "Tutorial 4 Description",
    },
    # Add more tutorials as needed
]

# Page title and some introductory text

st.write(
    "Welcome to the tutorials page! Here you can find various tutorials on different topics."
)


st.title("Tutorials..")


# Create a 4xN grid
num_cols = 4
num_rows = len(tutorials) // num_cols + (1 if len(tutorials) % num_cols else 0)

for row in range(num_rows):
    cols = st.columns(num_cols)
    for idx, col in enumerate(cols):
        tutorial_index = row * num_cols + idx
        if tutorial_index < len(tutorials):
            with col:
                display_tutorial(
                    tutorials[tutorial_index]["image"],
                    tutorials[tutorial_index]["description"],
                )
