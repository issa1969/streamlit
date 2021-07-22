import streamlit as st
# import pandas as pd
# import numpy as np
# from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start'

latast_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latast_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

latast_iteration = st.empty()
bar = st.progress(0.0)

for i in range(100):
    latast_iteration.text(f'Iteration {99-i}')
    bar.progress(99-i)
    time.sleep(0.1)

'Done!!!'
