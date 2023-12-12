import streamlit as st
from utils.achievement import run_tutorial_module, display_tutorial, click_button
from utils.CONSTANTS import DIVIDER
import base64
import streamlit as st
from st_clickable_images import clickable_images


def encode_local_image(image_path):
        with open(image_path, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
        return f"data:image/jpeg;base64,{encoded}"


st.set_page_config(page_title="tutorials", layout="wide")


st.image(
    "figures/banners/watercolour/watercolour2.png",
    caption="Credit: Kristian Aalling Sørensen",
    use_column_width="always",
)
st.title("Placeholder page. Not implemented..")


st.sidebar.title("Pages")
st.sidebar.markdown("## Select a pages")
app_mode = st.sidebar.selectbox(
    "", ["Overview", "AI theory", "Remote Sensing theory", "Tutorials"]
)



col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

with col1:
    st.write('This is a buttonThis is a buttonThis is a buttonThis is a buttonThis is a buttonThis is a buttonThis is a button')
with col3:
    st.header("AI ")
    image = encode_local_image("figures/learning/ai/overall_ai.png")
    clicked = clickable_images(
        [image],
        titles="test",
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "400px"},
    )
    if clicked == 0:
         st.write("You clicked the image!")
         st.image("figures/learning/ai/overall_ai.png")

st.write(f"{DIVIDER(height=0.2,dot_spacing=40)}", unsafe_allow_html=True)


col1, col2, col3 = st.columns([0.45, 0.1, 0.45])
with col1:
    image = encode_local_image("figures/learning/ai/overall_remote_sensing.png")
    clicked = clickable_images(
        [image],
        titles="test",
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "400px"},
    )
    if clicked == 0:
         st.write("You clicked the image!")
         st.image("figures/learning/ai/overall_ai.png")

with col3:
     st.header("Remote Sensing ")
     st.write('This is a buttonThis is a buttonThis is a buttonThis is a buttonThis is a buttonThis is a buttonThis is a button')