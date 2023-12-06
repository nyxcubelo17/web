import streamlit as st

st.title("About")
from PIL import Image
import requests

import streamlit as st
from streamlit_lottie import st_lottie 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


import streamlit as st
  
    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open ("images/family.jpg") 
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("A family that prays together, stays forever!")
    st.write("Family means a lot to all of us so too with mine. My family have a lots of ups and downs.")
    st.write("However, its not the hindrance for us to smile everyday for we are thankful as we open our eyes")
    st.write("seeing the beautiful creation by God. That despite of the challenges and hurdles we face we are")
    st.write("still given a chance to change our mistakes. During my elementary life, my parents supported me in my studies.")
    st.write("However, when I reach highschool for almost 6 years. I studied somewhere far away from them in Cebu. A place that will help me to become a better version of myself.")
    st.write("Knowing my purpose in life and reaching my dreams.")

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open ("images/school.jpg") 
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("The Sisters of Mary School-Girlstown,Inc")
    st.write("A place where I dont worry a lot. All I worry is how to get a good grades. Among a thousands of students who take the examination exam in different places in the Philippines.")
    st.write("I was one of the luckiest girl who pass the entrance exam. It is a free education and offer an Intensive Vocational Curicculum")

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open ("images/dormmates.jpg") 
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:
    st.subheader("Dormmates")
    st.write("They become part of my journey with entered in that school. We have different principles and belief. Despite of our differences we still love each other and treat us like a real family.")

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open ("images/classmates.jpg") 
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)
    
with text_column:
    st.subheader("Classmates")
    st.write("I meet a lot of friends with different backgrounds, places and languages. They are my second family even if we are not related by blood.")
    st.write("Family cannot just be called a family because of blood but a family is something that we share our love and care to others.")
    st.write("For almost staying here within 6 years from 2017-2022 I find myself to become a better version of me and an independent woman. I learn a lot of values from this school.")

with st.container():
    st.subheader("My Family")
    st.write("Mother: Juliet C. Ranoco")
    st.write("Father: Willy A. Ranoco")
    st.write("Sisters: Renaly Cubelo")
    st.write("         Nickylou P. Cubelo (twin)")
    st.write("Half-sisters: Rejul ann C. Sarceda")
    st.write("              Maureen S. Mainit")
    st.write("              Kris C. Sarceda")
    st.write("Half-brother: Kevin James C. Sarceda")

    
