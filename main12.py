import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

expander1 = st.beta_expander('Q1：あああああ？')
expander1.write('A1：あああああ')
expander2 = st.beta_expander('Q2：いいいいい？')
expander2.write('A2：いいいいい')
expander3 = st.beta_expander('Q3：ううううう？')
expander3.write('A3：ううううう')
