import streamlit as st
import numpy as np
import pandas as pd

"""
# サンプル
5 x 5の表データを表示する
"""

dataframe = pd.DataFrame(
    np.random.randn(5, 5),
    columns=('col %d' % i for i in range(5)))
st.table(dataframe)