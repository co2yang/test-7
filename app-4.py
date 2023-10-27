import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'col1': [1, 2, 3],
  'col2': ['A', 'B', 'C']
})
st.write(df)

st.write("""
# This is a header
## This is a sub-header
Here's some **bold** text and *italic* text.
""")

st.write("<h2>HTML Header</h2>", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import altair as alt
import random

## 標題跟子標題
st.subheader('這是標題', divider='rainbow')
st.subheader('這是子標題')

## 文字與字串效果
st.subheader('文字與字串效果', divider='rainbow')
st.write('Hello, *World!* :sunglasses:')
st.write(':blue[cool] :sunglasses:')
st.write(1234)
st.write('1 + 1 = ', 2)

## 數據框
st.subheader('數據框', divider='rainbow')
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))
#
st.write('Below is a DataFrame:', pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}), 'Above is a dataframe.')
#
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)

## 圖表
st.subheader('圖表', divider='rainbow')
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)