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

## 量測值元件
st.subheader('量測值元件', divider='rainbow')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
#
st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")

## 進階的圖表
st.subheader('進階的圖表', divider='rainbow')
# 先製作一個資料表
df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
# 透過 st.dataframe 來展示這個資料表
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)