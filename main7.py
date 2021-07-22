import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は', option, 'ですね'
