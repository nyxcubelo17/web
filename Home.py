from PIL import Image
import requests

import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.set_page_config(
    page_title="Multipage App",
    page_icon="wave"
)

st.title("Nyx Blog")
with st.container():
    st.subheader("#If you dont take risks,nothing will change. -Arya-")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/me1.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("Hi, I am Nickylette P. Cubelo :heart:")
    st.subheader("A BSCpE Student from Surigao del Norte State University")
    st.write(" ▶Facebook: https://www.facebook.com/nickylette.cubelo")
    st.write(" ▶Instagram: n cubelo")
    st.write(" ▶Email: nickylettecubelo.17@gmail.com")
    st.write(" ▶Contact Number: 09556281405")

    
