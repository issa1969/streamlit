import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

text = st.sidebar.text_input('あなたの趣味を教えてください',)
'あなたの趣味：', text

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'あなたの調子：', condition
