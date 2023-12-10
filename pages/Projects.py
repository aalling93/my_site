import streamlit as st



st.set_page_config(page_title = "project", layout="wide")


st.image(
    "figures/banners/watercolour/watercolour3.png",
    caption="Credit: Kristian Aalling Sørensen",
    use_column_width="always",
)
st.title("project")







col1, col2, col3 = st.columns([0.3, 0.3, 0.3])

with col1:
    st.markdown("Dark ships")


with col2:
    st.markdown("Bifrost")


with col3:
    st.markdown("Oil Spill")
 
