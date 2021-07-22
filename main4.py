import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.7],
    columns=['lat', 'lon']
)
st.map(df)
