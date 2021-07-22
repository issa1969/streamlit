import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
# st.line_chart(df)
# st.area_chart(df)
st.bar_chart(df)
