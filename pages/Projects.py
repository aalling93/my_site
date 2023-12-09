import streamlit as st


st.set_page_config(page_title="Kristian Aalling Sørensen - Satellite AI Expert", page_icon="🛰️")
st.markdown("# somthing")
st.sidebar.markdown("# something 2")



col1, col2, col3 = st.columns([0.3, 0.3, 0.3])

with col1:
    st.markdown("# something 3")


with col2:
    st.markdown("# something 5")


with col3:
    st.markdown("# something 7")
 
