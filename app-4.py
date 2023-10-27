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