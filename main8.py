import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

text = st.text_input('あなたの趣味を教えてください',)
'あなたの趣味：', text
