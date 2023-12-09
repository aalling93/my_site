# from tutorial_tabs import roboflow_annotation as roboflow_tab
# Your Streamlit app code for dynamically loading tutorials
import streamlit as st
import importlib


st.sidebar.title("Tutorial")
st.sidebar.markdown("## Select a tutorial")
app_mode = st.sidebar.selectbox(
    "", ["Roboflow Annotation", "AI Projects", "Projects", "Tutorials", "Front Page"]
)

tutorial_modules = {
    "Roboflow Annotation": "pages.tutorial_tabs.roboflow_annotation",
    # Add other mappings for your tutorials
}


def run_tutorial_module(module_name):
    module = importlib.import_module(module_name)
    module.run()


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
st.title("Tutorials")
st.write(
    "Welcome to the tutorials page! Here you can find various tutorials on different topics."
)

# Function to display a single tutorial in a grid
def display_tutorial(image, description):
    with st.container():
        st.image(image, width=150)  # Adjust width as needed
        st.write(description)


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
