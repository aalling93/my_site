import streamlit as st
import base64


def encode_local_image(image_path):
    with open(image_path, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"


st.set_page_config(page_title="tutorials", layout="wide")


st.image(
    "figures/banners/watercolour/watercolour3.png",
    caption="Credit: Kristian Aalling Sørensen",
    use_container_width="always",
)
st.title("Placeholder page. Not implemented..")


st.sidebar.title("Pages")
st.sidebar.markdown("## Select a pages")
app_mode = st.sidebar.selectbox("", ["Overview", "AI theory", "Remote Sensing theory", "Tutorials"])


col1, col2, col3 = st.columns([0.45, 0.1, 0.45])
