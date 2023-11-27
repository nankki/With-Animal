import streamlit as st
from PIL import Image

def cause():
    image1_path = './Data/1.png'
    image2_path = './Data/2.png'
    image3_path = './Data/3.png'

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image1 = Image.open(image1_path)
        st.image(image1_path, caption='1.png', use_column_width=True)
       
    with col2:
        image1 = Image.open(image1_path)
        st.image(image3_path, caption='3.png', use_column_width=True)
       
    with col3:
        image3 = Image.open(image2_path)
        st.image(image2_path, caption='2.png',use_column_width=True)
