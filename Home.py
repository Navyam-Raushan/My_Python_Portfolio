import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/my photo.jpeg")

with col2:
    st.title("Navyam Raushan")
    content = """I am Navyam Raushan, a second year engineering student currently pursuing BTech in Computer Science and 
            Engineering in IIIT Kottayam. I am a Fresher currently improving Python skills to pursue my future goal to 
            become a ML engineer, I am always eager to learn new things and grow with the Technology."""

    st.info(content)

aboutme = """<h4>I am a Python Developer, here are some 
              of my apps. Feel free to contact me.</h4>"""
st.write(aboutme, unsafe_allow_html=True)

# Making the mid part of the page
col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        imgpath = "images/" + row["image"]
        st.image(imgpath)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        imgpath = "images/" + row["image"]
        st.image(imgpath)
        st.write(f"[Source Code]({row['url']})")
