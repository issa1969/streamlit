import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Streamlit 超入門')

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open(
        '/Users/isao/Documents/selfpy/work/streamlit/image_400x400.jpg')
    st.image(img, caption='Isao', use_column_width=True)
