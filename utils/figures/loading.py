import base64
def add_bg_from_local(image_file):
    """ 
    loading a ffigrue from file to backgrond of the page
    Notice that we also set the background-size property to cover. This way, the background image will cover the entire element. We also set the background-attachment property to fixed so that the entire element is always covered, with no stretching — meaning the image will keep its original proportions.

    you need to convert the image file to a base64 string by using b64.encode (lines 3–4). After that, you use .decode() to decode the base64 string to be used in the HTML element (line 7) and put everything inside the background-image property.
    
    """
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-attachment: fixed;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

