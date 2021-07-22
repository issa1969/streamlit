import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

left_column, right_column = st.beta_columns(2)

button = left_column.checkbox('右のカラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
